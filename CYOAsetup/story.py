
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
        box="BEEP ^ ^ ^ ^ BEEP ^ ^ ^ ^ BEEP\n\n ^ ^ ^ ^BEEP ^ ^ ^ ^ BEEP ^ ^ ^ ^ BEEP\n\n ^ ^ ^ ^The Mundane ^ ^ ^ ^     ",
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
                    "Listen": Choice(
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

    "Living Room": Choice(
        box=[[""], 0],
        choice=[
            (["Kitchenette"], 0),
            (["Couch"], 0),
            (["Window"], 0),
            (["Front Door"], 0)
        ],
        next_choices=[
            "Kitchen",
            "Couch",
            "Window",
            "Front Door"
        ]
    ),
        "Kitchen": Choice(
            box=[["Heading to my kitchen, if you can call it that. I ponder breakfast", "My kitchen"], 0],
            choice=[
                (["Fridge"], 0),
                (["Freezer"], 0),
                (["Stove"], 0),
                (["Back to Living Room"], 0)
            ],
            next_choices=[
                "Fridge",
                "Freezer",
                "Stove",
                "Living Room"
            ]
        ),
            "Fridge": Choice(
                box=[["What I\'ve got is what I\'ve got. Even if it isn\'t much", "Back to staring at my eerly empty fridge"], 0],
                choice=[
                    (["Grab leftovers"], 0),
                    (["Grab eggs"], 0),
                    ([""], 0),
                    (["Back to Kitchenette"], 0)
                ],
                next_choices=[
                    "Leftovers",
                    "Eggs",
                    "",
                    "Living Room"
                ]
            ),
                "Leftovers": Choice(
                    box=[["You heat up the leftovers from last night. Not the most appetizing, but it will do.", "Leftovers are gone now."], 0],
                    choice=[
                        (["Sounds... tasty"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Fridge",
                        "",
                        "",
                        ""
                    ]
                ),
                "Eggs": Choice(
                    box=[["You grab some eggs from the fridge. Maybe you can cook them later.", "Eggs are taken. Note to get some from the store", "No more eggs..."], 0],
                    choice=[
                        (["Back to Fridge"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Fridge",
                        "",
                        "",
                        ""
                    ]
                ),
            "Freezer": Choice(
                box=[["Just some frozen dinners"], 0],
                choice=[
                    (["Take frozen dinner"], 0),
                    (["Keep looking"], 0),
                    ([""], 0),
                    (["Back to Kitchenette"], 0)
                ],
                next_choices=[
                    "Frozen Dinner",
                    "Keep Looking",
                    "",
                    "Living Room"
                ]
            ),
                "Frozen Dinner": Choice(
                    box=[["You decide to take out a pizza. Not really what I want to be eating for breakfast", "Not really breakfast food."], 0],
                    choice=[
                        (["Back to Freezer"], 0),
                        ([""], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Freezer",
                        "",
                        "",
                        ""
                    ]
                ),
                "Keep Looking": Choice(
                    box=[["Just letting the cold out...", "My toes feel the cool air pooling around them", "Now my ankles feel it too", "Any reason you are doing this?", "I think it is time to close the freezer"], 0],
                    choice=[
                        (["Keep looking", "Keep looking", "Keep looking", "Keep looking", "Keep looking", "Keep looking", "Maybe something is here", "Keep looking"], 0),
                        (["Close the freezer"], 0),
                        ([""], 0),
                        ([""], 0)
                    ],
                    next_choices=[
                        "Keep Looking",
                        "Freezer",
                        "",
                        ""
                    ]
                ),
            "Stove": Choice(
                box=[["My stove... not much to relish.", "My stove... not much to note.", "My stove... not much to do here.", "My stove... not very interesting.", "Looking at my stove, the grease marks jump out at me, the burns show the neglect I have showed when cooking late at night. Turning to the sink, a pile of casualties of my laziness lie.", "My stove"], 0],
                choice=[
                    ([""], 0),
                    (["Turn on burner", "Turn off the burner","Turn on burner", "Turn off the burner","Turn on burner", "Turn off the burner","Turn on burner", "Turn off the burner","Turn on burner", "Turn off the burner","Doesn't this get old?", "Flip the burner"], 0),
                    ([""], 0),
                    (["Back to the kitchen"], 0),
                ],
                next_choices=[
                    "",
                    "Stove",
                    "",
                    "Kitchen"
                ]
            ),
                "Cook Eggs": Choice(
                box=[["You cook the eggs you took from the fridge. They turn out decent enough. Not as good as he made them, but good enough."], 0],
                choice=[
                    (["Back to Kitchenette"], 0),
                    ([""], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Living Room",
                    "",
                    "",
                    ""
                ]
            ),


        "Couch": Choice(
            box=[["Sitting on my couch fills me with lethargic energy. The cushions begin to swallow my being as my mind begins to wander to what I want to do here.", "What a comfy couch"], 0],
            choice=[
                (["Scroll on Phone"], 0),
                (["Watch TV"], 0),
                (["No Nothing"], 0),
                (["Back to Living Room"], 0)
            ],
            next_choices=[
                "Couch Scroll",
                "Couch Watch",
                "Couch Nothing",
                "Living Room"
            ]
        ),
            "Couch Scroll": Choice(
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
                    "Couch Scroll",
                    "",
                    "",
                    "Couch"
                ]
            ),
            "Couch Watch": Choice(
                box=[[
                    "Turning on the TV, I go to Netflix. What to watch? No… No… not yet… waiting for someone else to watch that with. Maybe I\'ll watch something later",
                    "Back to the TV, lets try hulu this time. Too serious, too scary, why is everything so weird on here?",
                    "Disney maybe? Kids show, ruined show, man nothing to watch these days",
                    "Spoiled for choice and here I am not able to choose anything.",
                    "Unable to choose...",
                ], 0],
                choice=[
                    (["Keep watching"], 0),
                    ([""], 0),
                    ([""], 0),
                    (["Turn off the TV"], 0),
                ],
                next_choices=[
                    "Couch Watch",
                    "",
                    "",
                    "Couch",
                ]
            ),
            "Couch Nothing": Choice(
                box=[[
                    "I sit on the couch. It\'s comfy",
                    "Even though I got this at a thrift store, it does a great job.",
                    "I wonder how many lives this couch has lived. How many experiences it has had",
                    "Probably more than me...",
                    "I guess time doesn\'t matter"
                ], 0],
                choice=[
                    (["Keep sitting"], 0),
                    ([""], 0),
                    ([""], 0),
                    (["Snap out of this"], 0),
                ],
                next_choices=[
                    "Couch Nothing",
                    "",
                    "",
                    "Couch",
                ]
            ),
            
        "Window": Choice(
            box=[["My rusty window, cloudy glass, at least the hinges work"], 0],
            choice=[
                (["Open Window", "Close Window","Open Window", "Close Window","Open Window", "Close Window","Open Window", "Close Window","Open Window", "Close Window","Does this ever get old?"], 0),
                (["Look Outside"], 0),
                (["Climb Out"], 0),
                (["Back to Living Room"], 0)
            ],
            next_choices=[
                "Window",
                "Window Look",
                "Window Fall",
                "Living Room"
            ]
        ),
            "Window Look": Choice(
                box=[["Looking outside I see what I am used to. The sidewalk I mindlessly meander down while listening to music I haven't written, the cars that are owned by people I don\'t know, and the world I haven\'t explored", "What a world that is out there", "Will I ever actually see what is around me?", "Its a nice day out"], 0],
                choice=[
                    (["Keep looking"], 0),
                    ([""], 0),
                    ([""], 0),
                    (["Stop looking"], 0)
                ],
                next_choices=[
                    "Window",
                    "",
                    "",
                    "Window Look"
                ]
            ),


        "Front Door": Choice(
            box=[["Am you sure I\'m ready to leave? I've been autopiloting this morning for a while now, but I have to take some agency back", "Are you sure?"], 0],
            choice=[
                (["Yes?"], 0),
                (["No"], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "Leaving",
                "Living Room",
                "",
                ""
            ]
        ),

    "Leaving": Choice(
        box=[["I leave out the front door. I walk down my hallway to the elevator. Ding… Ding… Ding… I listen on as I descend the 5 stories below me. I listen to this everyday really, multiple times a day. How many times have you played this day? Over and over, every one the same, well mostly the same."], 0],
        choice=[
            (["To the school"], 0),
            (["Back into my room"], 0),
            (["Are you talking to me?"], 0),
            ([""], 0)
        ],
        next_choices=[
            "To School",
            "Not the Point",
            "Talking to me?",
            ""
        ]
    ),
        "To School": Choice(
            box=[["I head to school"], 0],
            choice=[
                (["Okay..."], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "School",
                "",
                "",
                ""
            ]
        ),
        "Not the Point": Choice(
            box=[["Not really the point… You\'ve made your choices, I\'ve made mine. Its about time to wrap this up. I don\'t have that many more words for you unfortunately."], 0],
            choice=[
                (["So this choice doesn't matter?"], 0),
                (["Listen to me!"], 0),
                (["What am I in this?"], 0),
                (["More words?"], 0)
            ],
            next_choices=[
                "School",
                "School",
                "School",
                "School",
            ]
        ),
        "Talking to me?": Choice(
            box=[["Who else would I be talking to? I\'ve narrated the best I could, and sure you were the one choosing, but its not like I haven't been clear. Have you not noticed me talking to *you* this entire time?"], 0],
            choice=[
                (["What?"], 0),
                (["Oh..."], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "School",
                "School",
                "",
                ""
            ]
        ),

    "School": Choice(
        box=[["I get to my school and do my classes. I won\'t bore you with details. They don\'t matter all that much anyway. To you what matters is what you chose. Did you scroll on your phone? Did you watch TV? Did you follow the story or just do what you felt like at the time"], 0],
        choice=[
            (["What I felt like"], 0),
            (["The story"], 0),
            (["Tried to break the game"], 0),
            ([""], 0)
        ],
        next_choices=[
            "Felt like",
            "The Story",
            "Break Game",
            ""
        ]
    ),
        "Felt like": Choice(
            box=[["Did you see me as you? Did you see this world as your own? Or did you just make it up as you went..."], 0],
            choice=[
                (["I just wanted to have fun"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "End",
                "",
                "",
                ""
            ]
        ),
        "The Story": Choice(
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
        "Break Game": Choice(
            box=[["At least you tell the truth. That is worth something I\'m sure. But why? Did you not trust that there would be a good ending? That the options you wanted were somehow better than the options that were provided? I\'m going back to my room."], 0],
            choice=[
                (["I'm not sure"], 0),
                (["It was bad..."], 0),
                (["I just wanted more"], 0),
                ([""], 0)
            ],
            next_choices=[
                "End",
                "End",
                "End",
                ""
            ]
        ),

    "End": Choice(
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
        "Turn on": Choice(
            box=[["It lights up. I can\'t believe this is charged. What a trip! Hey, I wonder if flappy bird is still on here!", "My old phone, I can\'t beleive it"], 0],
            choice=[
                (["Look at games"], 0),
                (["Look at texts"], 0),
                (["Leave the junk phone"], 0),
                ([""], 0)
            ],
            next_choices=[
                "Phone Games",
                "Old Phone Texts",
                "END",
                ""
            ]
        ),
            "Phone Games": Choice(
                box=[["Hey yeah, flappy bird is still on here!", "What a good game"], 0],
                choice=[
                    (["Keep playing"], 0),
                    (["Cool!"], 0),
                    ([""], 0),
                    ([""], 0)
                ],
                next_choices=[
                    "Phone Games",
                    "Turn on",
                    "",
                    ""
                ]
            ),
            "Old Phone Texts": Choice(
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
        "Dont Turn on": Choice(
            box=[["I thought we were getting somewhere… but I guess it doesn\'t need to matter."], 0],
            choice=[
                (["I guess not"], 0),
                ([""], 0),
                ([""], 0),
                ([""], 0)
            ],
            next_choices=[
                "END",
                "",
                "",
                ""
            ]
        ),

    "END": Choice(
        box=[["I head into my room, nothing changes for the better or the worse. I guess you were here. Yeah I know you thought you were some omnipotent being or something, but here you are, reading my words, my thoughts. Did you get the message? Is there one? Did you impose your own thoughts and feelings onto me as we went through this life? It\'s an interesting time to be alive, and I\'ll keep on keeping on and so will you. I guess you\'ll see if we meet again."], 0],
        choice=[
            (["Till we meet again"], 0),
            (["What's the message?"], 0),
            (["Were there secrets?"], 0),
            (["I'm gonna try again"], 0)
        ],
        next_choices=[
            "Goodbye",
            "Goodbye",
            "Goodbye",
            "Goodbye",
        ]
    ),
    "SOLO_END": Choice(
        box=[["You leave the game to its own devices. What will happen, who knows. Is it yours to know? Who knows. But you didn\'t get the point. The point was that it isn\'t your life. What you did might be \"beautiful\" or whatever you want to ascribe to it, but in the end, it wasn\'t mundane."], 0],
        choice=[
            (["I thought I won?"], 0),
            (["I got the good ending at least"], 0),
            (["At least he is happy"], 0),
            (["Screw you game"], 0)
        ],
        next_choices=[
            "Goodbye",
            "Goodbye",
            "Goodbye",
            "Goodbye",
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

    "Point It": Choice(
        box=[["Wow. I didn\'t think we would get here. Alright then\nHe grabs the gun and points it, the metallic barrel feeling cold on his skin he isn\'t sure what he is supposed to do. Told by you, the omniscient god of this world, that is how you see yourself right? As the barrel is pointed, he wonders where he went wrong, why he ended up here out of anything else he could. The trigger is pulled. Where was it aimed?"], 0],
        choice=[
            (["I don\'t know"], 0),
            (["I know"], 0),
            (["I don\'t want to think that"], 0),
            (["Why did I do this?"], 0)
        ],
        next_choices=[
            "Goodbye",
            "Goodbye",
            "Goodbye",
            "Goodbye"
        ]
    ),

    "Window Fall": Choice(
        box=[["Without the care to look through or check or care, whichever it is. You decide it would be best to climb through. I look down the 5 stories my apartment sits on top of, the morning just beginning, people waking up, birds doing their thing, and me; me who is now falling the distance that you didn\'t know about or care enough to consider. Me, the thing you didn\'t consider enough of a being to care about. Did you do this knowingly? Time slows as I fall. Descending past what I knew, the trees I looked out at, the birds I fed… I bet you are feeling bad now huh? Give a little personality to the thing you threw out the window and suddenly it means something. What will my neighbors think? To you they don\'t exist. Neither do their thoughts. Neither do I. Well you are right about one thing at least, I definitely won\'t exi-"], 0],
        choice=[
            (["What have I done?"], 0),
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

    "Gun Special": Choice(
        box=[["Why did you think the gun was important?"], 0],
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