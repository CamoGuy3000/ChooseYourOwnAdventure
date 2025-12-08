
class Choice:
    def __init__(self,
                 box: str | tuple[list[str], int],
                 choice: list[str],
                 next_choices: list[Choice],
                 ):
        
        # Handle box text: support simple string OR (list, index) format
        if isinstance(box, str):
            self.box_text = ([box], 0)
        else:
            self.box_text = box
            
        self.choices: list[(list[str], int)] = choice
        self.next_choices: list[str] = next_choices


STORY_CHOICES: dict[str, Choice] = {

    "Template": Choice(
        box=[[""], 0],
        choice=[
            ([""], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "",
            "",
            "",
            ""
        ]
    ),
    "Start": Choice(
        # box="BEEP ^ ^ ^ ^ BEEP ^ ^ ^ ^ BEEP\n\n ^ ^ ^ ^BEEP ^ ^ ^ ^ BEEP ^ ^ ^ ^ BEEP\n\n ^ ^ ^ ^The Mundane ^ ^ ^ ^     ",
        box="welcome",
        choice=[
            (["Wake Up"], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Wake Up",
            "",
            "",
            "Snooze"
        ]
    ), 
    "Wake Up": Choice(
        box=[[
            "With bleary eyes and an ache in my left leg, I turn myself upright. Still seated and unsure if I want to complete the motion of standing, take a look around my surroundings.",
            "Back to looking around my room."
            ], 0],
        choice=[
            (["Nightstand"], 0),
            (["Desk"], 0),
            (["Bathroom"], 0),
            (["Leave to the Living Room"], 0)
        ],
        next_choices=[
            "Nightstand",
            "Desk",
            "Bathroom",
            "To The Living Room"
        ]
    ),

    "Nightstand": Choice(
        box=[["Looking at my nightstand, there are only a few things I could possibly interact with.", "Still my nightstand."], 0],
        choice=[
            (["Watch"], 0),
            (["Light"], 0),
            (["Phone"], 0),
            (["Back to my room"], 0)
        ],
        next_choices=[
            "Watch",
            "Light",
            "Phone",
            "Wake Up"
        ]
    ),
        "Watch": Choice(
            box=[[
                "As I don my watch, cold steel makes my skin wince, the added weight pulls my hardly awake arm back to my side. A rhythmic tick soothes me until the realization hits that I will need to muster the strength to stand.",
                "I look at my watch wrapped around my wrist. That bruise is still there isn\'t it... ^ ^ ^ ^ I thought it would be gone by now.",
                "It\'s still there. Counting the wasted moments. Still ticking.",
                "Still ticking...",
                "Still ticking...",
                "Still ticking...",
                "Still ticking...",
                "Still ticking...",
                "Still ticking...",
                "Will it ever stop ticking? Should it? What fun is looking at a watch for you? Should I?",
                "Still ticking...",
                ], 0],
            choice=[
                (["Back to the rest of the Nightstand"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Nightstand",
                "",
                "",
                ""
            ]
        ),
        "Light": Choice(
            box=[[
                "It\'s morning, what's the light going to do for me? You decide to reach for it anyway and turn it on, my retinas recoil as my eyelids jump to their defense, blurring my already hindered vision. Even if I didn\'t want to get up, at this point I will, if only to get away from this photonic bombardment.",
                "Turning it off now to save my eyes fills me with gratitude… what a gratuitous action.",
                "It turns back on. And still works well.",
                "I decided to leave it off; better to save electricity.",
                "You contemplate turning it on again. Though I decide against it, it is better to save electricity."
                ], 0],
            choice=[
                (["Back to the nightstand"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Nightstand",
                "",
                "",
                ""
            ]
        ),
        "Phone": Choice( # TODO: Add more content here
            box="",
            choice=[
                ([""], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "",
                "",
                "",
                ""
            ]
        ),

    "Desk": Choice(
        box=[[
            "Here is my desk, cluttered as always with various items strewn about.",
            ], 0],
        choice=[
            (["Laptop"], 0),
            (["Pack Bag"], 0),
            (["Drawer"], 0),
            (["Back to Room"], 0)
        ],
        next_choices=[
            "Laptop",
            "Pack Bag",
            "Drawer",
            "Wake Up"
        ]
    ),
        "Laptop": Choice(
            box=[["Opening my laptop, the screen whines on. Typing in my password opens the screen to my incomplete assignments and unread emails.","My laptop..."], 0],
            choice=[
                (["Assignments"], 0),
                (["Emails"], 0),
                (["Close Assignments","Close Mail","Close Messages","Close Notes","Close the Rest","My Desktop"], 0),
                (["Power Down"], 0)
            ],
            next_choices=[
                "Assignments",
                "Emails",
                "Laptop",
                "Wake Up"
            ]
        ),
                "Laptop Desktop": Choice(
                    box=[["And this brings me to my desktop. The picture that greets me does so with a petrifying effect. It\'s a digitized version of a picture of my mom and dad. Him sitting in the pilot seat of a small plane, his arm bending around the canopy to reach hers. Her\'s reaching up to meet his, while gazing at the meeting point.","Time doesn\'t need to exist right now. The watch's face staring at me while its hands mean nothing.","Time doesn\'t need to exist right now"], 0],
                    choice=[
                        (["Keep Looking"], 0),
                        (["Back to my Laptop"], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Laptop Desktop",
                        "Laptop",
                        "",
                        ""
                    ]
                ),
            "Assignments": Choice(
                box=[["I open up my assignments"], 0],
                choice=[
                    (["Paper"], 0),
                    (["Math"], 0),
                    (["Music"], 0),
                    (["Enough of these"], 0)
                ],
                next_choices=[
                    "Paper",
                    "Math",
                    "Music",
                    "Laptop"
                ]
            ),
                "Paper": Choice(
                    box=[["That's the paper I need to finish, you don't have time for that right now..."], 0],
                    choice=[
                        (["Yeah you're right"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Assignments",
                        "",
                        "",
                        ""
                    ]
                ),
                "Math": Choice(
                    box=[["Ugh, my math homework. Definitely not in the mood for that... and trust me, not worth your time"], 0],
                    choice=[
                        (["I believe you"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Assignments",
                        "",
                        "",
                        ""
                    ]
                ),
                "Music": Choice( #TODO: add music
                    box=[["My music project, I guess we could give it a listen"], 0],
                    choice=[
                        (["Listen"], 0),
                        (["Don't Listen"], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Listen",
                        "Assignments",
                        "",
                        ""
                    ]
                ),
            "Email": Choice( #TODO: add email content
                box=[[""], 0],
                choice=[
                    ([""], 0),
                    ([""], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "",
                    "",
                    "",
                    ""
                ]
            ),
        "Pack Bag": Choice(
            box=[["Grabbing my laptop, charger, water bottle, and a few scattered pens from across my desk, my bag is packed.", "My bag is already packed... I don't have anything else to put in it", "My bag is already packed"], 0],
            choice=[
                (["Not very much stuff..."], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Desk",
                "",
                "",
                ""
            ]
        ),
        "Drawer": Choice(
            box=[["a"], 0],
            choice=[
                (["a"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "WIP",
                "",
                "",
                ""
            ]
        ),
            "Drawer Opened": Choice(
                box=[["Unlocking the desk drawer, you see what you locked away: your gun. Unloaded and barrel blocked with a code controlled cable lock. What could you possibly want to do with this", "There it sits"], 0],
                choice=[
                    (["Entertain the idea"], 0),
                    ([""], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Gun Stuff",
                    "",
                    "",
                    ""
                ]
            ),
                "Gun Stuff": Choice(
                    box=[["There is a magazine sitting next to the gun"], 0],
                    choice=[
                        (["Pick up the magazine", "Enter the code", "Take out the cable lock", "Load the magazine", "Cock the gun", "Point it"], 0),
                        ([""], 0),
                        (["Leave it alone"], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Gun Stuff",
                        "Hold onto it",
                        "Leave it alone",
                        ""
                    ]
                ),
                "Hold onto it": Choice(
                    box=[["For reasons beyond my understanding. You deem it necessary to keep a gun with you."], 0],
                    choice=[
                        (["Go back to the desk"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Desk",
                        "",
                        "",
                        ""
                    ]
                ),
                "Point It": Choice( # TODO
                    box=[["Congrats"], 0],
                    choice=[
                        ([""], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "",
                        "",
                        "",
                        ""
                    ]
                ),
                "Leave it alone": Choice(
                    box=[["You leave the gun alone."], 0],
                    choice=[
                        (["Fine."], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Desk",
                        "",
                        "",
                        ""
                    ]
                ),

    "Bathroom": Choice(
        box=[[
            "The bathroom is as I left it last night, toothbrush in the holder, toothpaste cap screwed on tight.",
            ], 0],
        choice=[
            (["Brush Teeth"], 0),
            (["Wash Face"], 0),
            (["Take a leak"], 0),
            (["Back to my bedroom"], 0)
        ],
        next_choices=[
            "Brush Teeth",
            "Wash Face",
            "Take a leak",
            "Wake Up"
        ]
    ),
        "Brush Teeth": Choice(
            box=[["The routine continues, another day, another dental hygienist to make proud.", "But not that proud..."], 0],
            choice=[
                (["Back to the bathroom"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Bathroom",
                "",
                "",
                ""
            ]
        ),
        "Wash Face": Choice(
            box=[["The cold water wakes me up a little bit. Refreshing sure, but I would rather be asleep.", "Yeah I\'m awake enough, don\'t need an ice plunge", "Once again the water calls you, but give in? I won\'t."], 0],
            choice=[
                (["Back to the bathroom"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Bathroom",
                "",
                "",
                ""
            ]
        ),
        "Take a leak": Choice(
            box=[["I do so, no more detail needed then that.", "I… just did? I don\'t know what you expect of me", "Okay so know this is just a joke huh", "No more of this thank you"], 0],
            choice=[
                (["Back to the bathroom"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Bathroom",
                "",
                "",
                ""
            ]
        ),
    
    "To The Living Room": Choice(
        box=[[""], 0],
        choice=[
            (["Nevermind, back to my bedroom"], 0),
            (["Continue"], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Wake Up",
            "Living Room",
            "",
            ""
        ]
    ),

}




TEST_STORY_CHOICES: dict[str, Choice] = {
    "Start": Choice(
        box="This is a work in progress",
        choice=[
            (["Dock"], 0),
            (["Start"], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Dock",
            "Start",
            "",
            ""
        ]
    ),
    
    "Dock": Choice(
        box="You are on a dock looking at a boat",
        choice=[
            (["Go on the boat"], 0),
            (["Turn aroud to the harbor"], 0),
            (["Jump in the water"], 0),
        ],
        next_choices=[
            "Board",
            "Harbor",
            "Water",
        ]
    ),
    "Board": Choice(
        box=[["You board the boat", "still on the boat"], 0],
        choice=[
            (["Sail the boat"], 0),
            (["Sleep on the boat"], 0),
            (["Board 1", "Board 2", "Board 3"], 0),
            (["Wait for someone"], 0),
        ],
        next_choices=[
            "Start",
            "Start",
            "Board",
            "Start"
        ]
    ),
    "Harbor": Choice(
        box="You are on the harbor",
        choice=[
            (["Back to the boat"], 0),
            (["Look around"], 0),
        ],
        next_choices=[
            "Dock",
            "Start",
        ]
    ),
    "Water": Choice(
        box="You jump in the water",
        choice=[
            (["Swim"], 0),
        ],
        next_choices=[
            "Start",
        ]
    ),
}


# Choice(
#     name="",
#     box="",
#     choice=[
#         "",
#         "",
#         "",
#     ],
#     next_choices=[
#         "",
#         "",
#         "",
#         ""
#     ]
# ),