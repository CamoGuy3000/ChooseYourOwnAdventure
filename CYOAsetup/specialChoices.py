
import storyFunctions

SPECIAL_CHOICES: dict[str, function] = {
    "Goodbye": storyFunctions.goodbye_special,
    "Board": storyFunctions.board_special,
    "Snooze": storyFunctions.snooze_special,
    "Wake Up": storyFunctions.wake_up_special,
    "Laptop": storyFunctions.laptop_check,
    "Drawer": storyFunctions.drawer_check,
    "Gun Stuff": storyFunctions.gun_stuff_special,
    "Hold onto it": storyFunctions.hold_gun_special,
    "To The Living Room": storyFunctions.living_room_check,
    "Watch": storyFunctions.don_watch,
    "Pack Bag": storyFunctions.pack_bag,
    "Lazy": storyFunctions.lazy_special,
    "Phone Oldest Emails": storyFunctions.dad_found,
    "Laptop Oldest Emails": storyFunctions.dad_found,
    "Texts": storyFunctions.texts_question,
    "Want Typewriter": storyFunctions.wants_typewriter_special,
    "Want Phone": storyFunctions.wants_phone_special,
    "Want Harddrive": storyFunctions.wants_harddrive_special,
}

LOST_TIME_CHOICES: dict[str, int] = {
    "Snooze": 5,
    "Watch": 1,
    "Laptop Desktop": 3,
    "Phone": 7,

}
