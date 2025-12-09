
import storyFunctions

SPECIAL_CHOICES: dict[str, function] = {
    "Goodbye": storyFunctions.goodbye_special,
    "Board": storyFunctions.board_special,
    "Snooze": storyFunctions.snooze_special,
    "Wake Up": storyFunctions.wake_up_special,
    "Brush Teeth": storyFunctions.brush_teeth_special,
    "Wash Face": storyFunctions.wash_face_special,
    "Take a Leak": storyFunctions.leak_special,
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

    "Living Room": storyFunctions.living_room_special,
    "Eggs": storyFunctions.eggs_special,
    "Stove": storyFunctions.stove_special,


    "The Story": storyFunctions.the_story_special,
    "End": storyFunctions.end_special,
    "Old Phone Texts": storyFunctions.dad_texts,
}

LOST_TIME_CHOICES: dict[str, int] = {
    "Snooze": 5,
    "Watch": 1,
    "Laptop Desktop": 3,
    "Phone": 7,
    "Chouch Scroll": 2,
    

}

DEVIANCE_CHOICES: dict[str, int] = {
    "Scroll": 2,
    "Deleted": 3,
    "Deleted No": 8,
    "Phone Old Emails": 3,
    "Phone Older Emails": 4,
    "Phone Oldest Emails": 5,
    "Laptop Old Emails": 3,
    "Laptop Older Emails": 4,
    "Laptop Oldest Emails": 5,
    "Drawer Opened": 5,
    "Gun Stuff": 9,
    "Hold onto it": 15,
    "Point It": 25,
    
    "Keep Looking": 3,
    "Couch Scroll": 2,


}
