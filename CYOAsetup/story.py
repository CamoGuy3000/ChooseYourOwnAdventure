
class Choice:
    def __init__(self,
                 box: str,
                 choice: list[str],
                 next_choices: list[Choice],
                 ):
        self.box_text: str = box
        self.choices: list[(list[str], int)] = choice
        # List of list of choice strings and the current selected index

        self.next_choices: list[str] = next_choices


TEST_STORY_CHOICES: dict[str, Choice] = {
    "WIP": Choice(
        box="This is a work in progress",
        choice=[
            (["Dock"], 0),
            (["WIP"], 0),
            ([""], 0),
            ([""], 0)
        ],
        next_choices=[
            "Dock",
            "WIP",
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
        box="You board the boat",
        choice=[
            (["Sail the boat"], 0),
            (["Sleep on the boat"], 0),
            (["Board 1", "Board 2", "Board 3"], 0),
            (["Wait for someone"], 0),
        ],
        next_choices=[
            "WIP",
            "WIP",
            "Board",
            "WIP"
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
            "WIP",
        ]
    ),
    "Water": Choice(
        box="You jump in the water",
        choice=[
            (["Swim"], 0),
        ],
        next_choices=[
            "WIP",
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