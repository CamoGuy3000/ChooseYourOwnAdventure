
import storyFunctions

SPECIAL_CHOICES: dict[str, function] = {
    "Board": storyFunctions.board_special,
    "Wake Up": storyFunctions.wake_up_special,
    "Laptop": storyFunctions.laptop_check,
    "Drawer": storyFunctions.drawer_check,
    "Gun Stuff": storyFunctions.gun_stuff_special,
    "Hold onto it": storyFunctions.hold_gun_special,
    "To The Living Room": storyFunctions.living_room_check,
    "Watch": storyFunctions.don_watch,
    "Pack Bag": storyFunctions.pack_bag,
}
