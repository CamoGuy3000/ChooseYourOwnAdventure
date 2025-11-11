
class Choice:
    def __init__(self,
                 box: str,
                 choice: list[str],
                 next_choices: list[Choice],
                 ):
        self.box_text: str = box
        self.choices: list[str] = choice

        self.next_choices: list[str] = next_choices


TEST_STORY_CHOICES: dict[str, Choice] = {
    "WIP": Choice(
        box="This is a work in progress",
        choice=[
            "Dock",
            "",
            "",
            ""
        ],
        next_choices=[
            "Dock",
            "",
            "",
            ""
        ]
    ),
    
    "Dock": Choice(
        box="You are on a dock looking at a boat",
        choice=[
            "Go on the boat",
            "Turn aroud to the harbor",
            "Jump in the water",
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
            "Sail the boat",
            "Sleep on the boat",
            "Get a drink",
            "Wait for someone",
        ],
        next_choices=[
            "WIP",
            "WIP",
            "WIP",
            "WIP"
        ]
    ),
    "Harbor": Choice(
        box="You are on the harbor",
        choice=[
            "Back to the boat",
            "Look around",
        ],
        next_choices=[
            "Dock",
            "WIP",
        ]
    ),
    "Water": Choice(
        box="You jump in the water",
        choice=[
            "Swim",
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