
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
    "Snooze": Choice(
        box=[["You hit the snooze button, stealing a few more moments of rest.", "Still snoozing."], 0],
        choice=[
            (["Snooze Again"], 0),
            (["Wake Up"], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Snooze",
            "Wake Up",
            "",
            ""
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
        "Phone": Choice(
            box=[[
                "A great morning habit", "Still a great morning habit..."
                ], 0],
            choice=[
                (["YouTube"], 0),
                (["TikTok"], 0),
                (["Something more productive"], 0),
                (["Put it down"], 0)
            ],
            next_choices=[
                "Scroll",
                "Scroll",
                "Productive",
                "Nightstand"
            ]
        ),
            "Scroll": Choice(
                box=[[
                    "Cat videos, nice. Oh that guy really should have hit the breaks. More cat videos. There was a heist? Cool. You don\'t need to get back into politics."
                ], 0],
            choice=[
                (["Keep scrolling"], 0),
                ([""], 0),
                ([""], 0),
                (["Its time to stop"], 0)
            ],
            next_choices=[
                "Scroll",
                "",
                "",
                "Phone"
            ]
        ),
            "Productive": Choice(
                box=[[
                    "I guess this isn't as bad as scrolling through mindless videos."
                ], 0],
            choice=[
                (["Mail"], 0),
                (["Texts"], 0),
                (["Discord"], 0),
                (["Get off your phone"], 0)
            ],
            next_choices=[
                "Phone Mail",
                "Texts",
                "Discord",
                "Nightstand"
            ]
        ),
                "Phone Mail": Choice(
                    box=[["No new emails."], 0],
                    choice=[
                        (["Old Emails"], 0),
                        (["Alright enough phone usage"], 0),
                        (["Time to Scroll"], 0),
                        (["Lets still try to be productive"], 0)
                    ],
                    next_choices=[
                        "Phone Old Emails",
                        "Nightstand",
                        "Scroll",
                        "Productive"
                    ]
                ),
                    "Phone Old Emails": Choice(
                        box=[["Just spam and newsletters. Why are we looking at this?"], 0],
                        choice=[
                            (["Older"], 0),
                            (["Back to productiveness"], 0),
                            ([""], 0),
                            ([""], 0)
                        ],
                        next_choices=[
                            "Phone Older Emails",
                            "Productive",
                            "",
                            ""
                        ]
                    ),
                        "Phone Older Emails": Choice(
                            box=[["Still just spam and newsletters. You know I have things to do right?"], 0],
                            choice=[
                                (["Even Older"], 0),
                                (["Back to productiveness"], 0),
                                ([""], 0),
                                ([""], 0)
                            ],
                            next_choices=[
                                "Phone Oldest Emails",
                                "Productive",
                                "",
                                ""
                            ]
                        ),
                            "Phone Oldest Emails": Choice(
                                box=[[
                                    "Key kiddo, I don't know if you'll get this, but here is your first email. Testing 1 2 3... Boo! Alright thats enough, love ya kid\nDad",
                                    "Your transcript just came in, I can't beleive what a good job you are doing little man. I know it sucks I can\'t be there to congratulate you in person, but know I am so so so proud of you.\nDad",
                                    "Netflix code: 834668",
                                    "I know we just talked... but I love you son. I\'ll always be there, even when I'm not.\nDad",
                                    "That was the last email... why can't there be another",
                                    "But there was nothing else..."
                                    ], 0],
                                choice=[
                                    (["Another"], 0),
                                    (["Time to be less productive"], 0),
                                    ([""], 0),
                                    ([""], 0)
                                ],
                                next_choices=[
                                    "Phone Oldest Emails",
                                    "Productive",
                                    "",
                                    ""
                                ]
                            ),
            "Texts": Choice(
                box=[["No new messages. They delete after a few months to save storage anyway."], 0],
                choice=[
                    ([""], 0),
                    (["Unfortunate"], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Deleted",
                    "Phone",
                    "",
                    ""
                ]
            ),
                "Deleted": Choice(
                    box=[["Deleted. Like I said, they are deleted after some time. They aren't on this phone anymore because I never knew the feature was on. Is that explination enough for you??"], 0],
                    choice=[
                        (["Yes"], 0),
                        (["No"], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Deleted Yes",
                        "Deleted No",
                        "",
                        ""
                    ]
                ),
                    "Deleted Yes": Choice(
                    
                        box=[["Good. Moving on."], 0],
                        choice=[
                            (["Back to phone"], 0),
                            ([""], 0),
                            ([""], 0),
                            ([""], 0)
                        ],
                        next_choices=[
                            "Phone",
                            "",
                            "",
                            ""
                        ]
                    ),
                    "Deleted No": Choice(
                        box=[["Well tough luck. They are gone. Nothing I can do about it. I don't have any other way of getting those texts anyway."], 0],
                        choice=[
                            (["Back to phone"], 0),
                            ([""], 0),
                            ([""], 0),
                            ([""], 0)
                        ],
                        next_choices=[
                            "Phone",
                            "",
                            "",
                            ""
                        ]
                    ),
            "Discord": Choice(
                box=[["I said something more productive, not something actually productive."], 0],
                choice=[
                    (["Servers"], 0),
                    (["Friends"], 0),
                    (["Enough of Discord"], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Discord Servers",
                    "Discord Friends",
                    "Phone",
                    ""
                ]
            ),
                "Discord Servers": Choice(
                    box=[["Just scrolling through servers, nothing important here, no new messages."], 0],
                    choice=[
                        (["Back to Discord"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Discord",
                        "",
                        "",
                        ""
                    ]
                ),
                "Discord Friends": Choice(
                    box=[["Only one new message. Its from one of my oldest friends on here actually… it reads:\nYo man, I just was looking through that old tech box you sold me, theres some cool stuff in here: an old typewriter, a phone, harddrive (which looks cooked) and some more stuff. Do you really not need any of this?"], 0],
                    choice=[
                        (["Respond"], 0),
                        ([""], 0),
                        ([""], 0),
                        (["Leave it for now"], 0),
                    ],
                    next_choices=[
                        "Discord Respond",
                        "",
                        ""
                        "Discord",
                    ]
                ),
                    "Discord Respond": Choice(
                        box=[["What should I say? Do I want any of this stuff?"], 0],
                        choice=[
                            (["The typewriter"], 0),
                            (["The phone"], 0),
                            (["The Harddrive"], 0),
                            (["Don't respond, forget it"], 0),
                        ],
                        next_choices=[
                            "Want Typewriter",
                            "Want Phone",
                            "Want Harddrive",
                            "Discord",
                        ]
                    ),
                        "Want Typewriter": Choice(
                            box=[["Yeah sure, I could use an old typewriter. Send it over."], 0],
                            choice=[
                                (["Back to Discord"], 0),
                                ([""], 0),
                                ([""], 0),
                                ([""], 0)
                            ],
                            next_choices=[
                                "Discord",
                                "",
                                "",
                                ""
                            ]
                        ),
                        "Want Phone": Choice(
                            box=[["Yeah sure, I could use an old phone. Send it over."], 0],
                            choice=[
                                (["Back to Discord"], 0),
                                ([""], 0),
                                ([""], 0),
                                ([""], 0)
                            ],
                            next_choices=[
                                "Discord",
                                "",
                                "",
                                ""
                            ]
                        ),
                        "Want Harddrive": Choice(
                            box=[["Yeah sure, I could use the old harddrive. Send it over."], 0],
                            choice=[
                                (["Back to Discord"], 0),
                                ([""], 0),
                                ([""], 0),
                                ([""], 0)
                            ],
                            next_choices=[
                                "Discord",
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
                (["Laptop Mail"], 0),
                (["Close Assignments","Close Mail","Close Messages","Close Notes","Close the Rest","My Desktop"], 0),
                (["Power Down"], 0)
            ],
            next_choices=[
                "Assignments",
                "Laptop Mail",
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
                "Music": Choice( 
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
                    "Listen": Choice( #TODO: add music
                        box=[["*Jam out*"], 0],
                        choice=[
                            (["Back to assignments"], 0),
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
        "Laptop Mail": Choice(
            box=[["No new emails."], 0],
            choice=[
                (["Old Emails"], 0),
                ([""], 0),
                ([""], 0),
                (["Lets still try to be productive"], 0)
            ],
            next_choices=[
                "Laptop Old Emails",
                "",
                "",
                "Productive"
            ]
        ),
            "Laptop Old Emails": Choice(
                box=[["Just spam and newsletters. Why are we looking at this?"], 0],
                choice=[
                    (["Older"], 0),
                    (["Back to productiveness"], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Laptop Older Emails",
                    "Laptop",
                    "",
                    ""
                ]
            ),
                "Laptop Older Emails": Choice(
                    box=[["Still just spam and newsletters. You know I have things to do right?"], 0],
                    choice=[
                        (["Even Older"], 0),
                        (["Back to productiveness"], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Laptop Oldest Emails",
                        "Laptop",
                        "",
                        ""
                    ]
                ),
                    "Laptop Oldest Emails": Choice(
                        box=[[
                            "Key kiddo, I don't know if you'll get this, but here is your first email. Testing 1 2 3... Boo! Alright thats enough, love ya kid\nDad",
                            "Your transcript just came in, I can't beleive what a good job you are doing little man. I know it sucks I can\'t be there to congratulate you in person, but know I am so so so proud of you.\nDad",
                            "Netflix code: 834668",
                            "I know we just talked... but I love you son. I\'ll always be there, even when I'm not.\nDad",
                            "That was the last email... why can't there be another",
                            "But there was nothing else..."
                            ], 0],
                        choice=[
                            (["Another"], 0),
                            (["Time to be less productive"], 0),
                            ([""], 0),
                            ([""], 0)
                        ],
                        next_choices=[
                            "Laptop Oldest Emails",
                            "Laptop",
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





    ## Endings
    "Lazy": Choice(
        box=[["Really? I understand that sleep is important... but this is a game, for your enjoyment, that you chose to play. It was well thought out, had interesting characters, and was meant to show the juxtaposition of player choice in games. How it drives the story, but inherently takes out the meaning of the work. Making the story less of a vessel for the author to convey a message, and more of a reflection of the player themself. If you didn\'t want to engage with that, you didn\'t have to play the game."], 0],
        choice=[
            (["Skip"], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Lazy Skip",
            "",
            "",
            ""
        ]
    ),
    "Lazy Skip": Choice(
        box=[["Woah Woah Woah, you can\'t just leave. You didn\'t want to hear the story, I can get that. But now you don\'t want to even hear this? Sure story games can be dull, but what are you doing if you don\'t want to play, *and* you don\'t want to not play. What are you looking for? A quick fix of dopamine is not what you signed up for... I mean look at the title of the *game* you are (not) playing."], 0],
        choice=[
            (["Sorry I guess"], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Not Lazy Skip",
            "",
            "",
            ""
        ]
    ),
    "Not Lazy Skip": Choice(
        box=[["So if you didn\'t want to engage in the story, what was missing?"], 0],
        choice=[
            (["A Good Story"], 0),
            (["Action"], 0),
            (["Intrigue"], 0),
            (["Something else"], 0)
        ],
        next_choices=[
            "Really!?",
            "Really!?",
            "Really!?",
            "Really!?"
        ]
    ),
    "Really!?": Choice(
        box=[["Well that\’s unfortunate. Maybe next time you can try actually playing the game before snoozing it away. Did you even read the paragraph I wrote? The analysis I... you know what? Fine. You don't like the game thats okay, good luck finding enjoyment somewhere else."], 0],
        choice=[
            (["Goodbye"], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Goodbye",
            "",
            "",
            ""
        ]
    ),



    "Goodbye": Choice(
        box=[["."], 0],
        choice=[
            ([""], 0),
            ([""], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "t",
            "",
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