import story


def goodbye_special(engine):
    engine.destroy()

# Add 'engine' argument to accept the passed 'self'
def board_special(engine):
    story.TEST_STORY_CHOICES["Board"].box_text += "\n\nYou feel a bit dizzy as you step onto the boat."

def snooze_special(engine):
    engine.typing_speed = engine.normal_typing_speed
    engine.snooze_time += 1

    if engine.snooze_time >= 10:
        current_scene = story.STORY_CHOICES.get("Snooze")
        if current_scene is not None:
            current_scene.next_choices[0] = "Lazy"

# Add 'engine' argument and update engine.typing_speed
def wake_up_special(engine):
    engine.typing_speed = engine.normal_typing_speed

def laptop_check(engine):
    current_scene = engine.current_scene
    if current_scene is not None:
        match current_scene.choices[2][0][current_scene.choices[2][1]]:
            case "Close Assignments":
                current_scene.box_text = [["Opening my laptop, the screen whines on. Typing in my password opens the screen to my incomplete assignments and unread emails.","I don't feel like that anyway.","My laptop..."], 0]
            case "Close Mail":
                current_scene.box_text = [["Opening my laptop, the screen whines on. Typing in my password opens the screen to my incomplete assignments and unread emails.","Don't need to read those either","My laptop..."], 0]
            case "Close Messages":
                current_scene.box_text = [["Opening my laptop, the screen whines on. Typing in my password opens the screen to my incomplete assignments and unread emails.","No one\'s up to text anyway","My laptop..."], 0]
            case "Close Notes":
                current_scene.box_text = [["Opening my laptop, the screen whines on. Typing in my password opens the screen to my incomplete assignments and unread emails.","Not important until I'm in class anyway","My laptop..."], 0]
            case "Close the Rest":
                current_scene.next_choices[2] = "Laptop Desktop"
                current_scene.box_text = [["Opening my laptop, the screen whines on. Typing in my password opens the screen to my laptop desktop.","Finally done with those distractions","My laptop..."], 0]

def drawer_check(engine):
    current_scene = story.STORY_CHOICES.get("Drawer")
    if current_scene is not None:
        if engine.HAVE_KEY and engine.HAVE_CODE:
            current_scene.box_text = [["The key I have would fit perfectly"], 0]
            current_scene.choices[0] = (["Use the key to open the drawer"], 0)
            current_scene.choices[1] = (["Leave it alone"], 0)
            current_scene.next_choices[0] = "Drawer Opened"
            current_scene.next_choices[1] = "Desk"
        else:
            current_scene.box_text = [["The drawer is locked. I don\'t have a key. I locked it for a reason. The code changes everyday too, no need for me to try to guess it."], 0]
            current_scene.choices[0] = (["Leave it alone"], 0)
            current_scene.next_choices[0] = "Desk"


def gun_stuff_special(engine):
    current_scene = engine.current_scene
    if current_scene is not None:
        print(current_scene.choices[0][1])
        match current_scene.choices[0][1]:
            case 0:
                pass
            case 1:
                story.STORY_CHOICES["Gun Stuff"].choices[2] = (["Leave it alone!"], 0)
                story.STORY_CHOICES["Leave it alone"].box_text = [["You leave the gun alone. About time."], 0]
            case 2:
                story.STORY_CHOICES["Gun Stuff"].choices[2] = (["Leave it alone!! What are you doing?"], 0)
                story.STORY_CHOICES["Leave it alone"].box_text = [["You leave the gun alone. Why would you even think to do that?"], 0]
            case 3:
                story.STORY_CHOICES["Gun Stuff"].choices[1] = (["Hold onto it"], 0)
                story.STORY_CHOICES["Gun Stuff"].choices[2] = (["Put it back. Please just put it back"], 0)
                story.STORY_CHOICES["Leave it alone"].box_text = [["You put back the gun. Thank you for finally listening to any amount of reason."], 0]
            case 4:
                story.STORY_CHOICES["Gun Stuff"].next_choices[0] = "Point It"
                story.STORY_CHOICES["Gun Stuff"].choices[1] = ([""], 0)
                story.STORY_CHOICES["Gun Stuff"].choices[2] = (["Put it back! You don't need this!!"], 0)
                story.STORY_CHOICES["Leave it alone"].box_text = [["At the last possible moment, you realize you have some humanity. Good job."], 0]


def hold_gun_special(engine):
    engine.HAVE_GUN = True

def living_room_check(engine):
    current_scene = story.STORY_CHOICES.get("To The Living Room")
    if current_scene is not None:
        if engine.BAG_PACKED:
            if engine.WATCH_ON:
                current_scene.box_text = [["I get dressed and sling the packed bag around my arm and shoulder; the weight of the bag balances well with the watch, keeping my center of gravity from not being too far off. The weight may not be a fraction of the bag, but it once again grounds me, allowing for my feet to stay grounded too. As I vacate my bedroom, so does the light behind me, instead choosing to illuminate the living room in front of me."], 0]
            else:
                current_scene.box_text = [["I get dressed and sling the packed bag around my arm and shoulder; the weight of the bag pulls my chest, fixing my posture for a split second before dragging it beyond its equilibrium. Finding existence on the floor less appealing than having to exert effort to stand, I do the latter. I fix my posture, though my wrist feels lighter than it should. As I vacate my bedroom, so does the light behind me, instead choosing to illuminate the living room in front of me."], 0]
        elif engine.WATCH_ON:
            current_scene.box_text = [["I get dressed, sling my bag around my arm and shoulder; it's lighter than it should be. As I expect to feel the weight that isn't there my wrist pulls me forward, the watch, while not heavy, acts enough to pull me off balance. Beleiving that the floor is a worse option than exerted effort, I do the latter. As I vacate my bedroom, so does the light behind me, instead choosing to illuminate the living room in front of me."], 0]
        else:
            current_scene.box_text = [["I get dressed, sling my bag around my arm and shoulder; it's lighter than it should be, my wrist is too. Something is off. As I vacate my bedroom, so does the light behind me, instead choosing to illuminate the living room in front of me."], 0]
            
def don_watch(engine):
    if not engine.WATCH_ON:
        engine.WATCH_ON = True

def pack_bag(engine):
    if not engine.BAG_PACKED:
        engine.BAG_PACKED = True


def lazy_special(engine):
    current_scene = story.STORY_CHOICES.get("Lazy")
    if current_scene is not None:
        engine.after(3000, _l1, engine)
        
        engine.after(15000, _l2, engine)

def _l1(engine):
    if engine.current_scene == story.STORY_CHOICES["Lazy"]:
        engine._configure_buttons(story.STORY_CHOICES["Lazy"].choices, story.STORY_CHOICES["Lazy"].next_choices)
        
def _l2(engine):
    if engine.current_scene == story.STORY_CHOICES["Lazy"]:
        story.STORY_CHOICES["Lazy"].next_choices[0] = "Not Lazy Skip"
        engine._configure_buttons(story.STORY_CHOICES["Lazy"].choices, story.STORY_CHOICES["Lazy"].next_choices)


def dad_found(engine):
    engine.dad1_found = True

def texts_question(engine):
    if engine.dad1_found:
        current_scene = story.STORY_CHOICES.get("Texts")
        if current_scene is not None:
            current_scene.choices[0] = (["Where are his texts?"], 0)


def wants_typewriter_special(engine):
    engine.wants_typewriter = True

def wants_phone_special(engine):
    engine.wants_phone = True

def wants_harddrive_special(engine):
    engine.wants_harddrive = True

