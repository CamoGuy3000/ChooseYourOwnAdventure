import story


def goodbye_special(engine):
    if engine.HAVE_GUN:
        engine.after(100, engine.update_scene, "Gun Special")
        engine.after(3000, engine.destroy)
    else:
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
        if engine.HAVE_KEY:
            current_scene.box_text = [["The key I have would fit perfectly, I swore I would never use it though..."], 0]
            current_scene.choices[0] = (["Use the key to open the drawer"], 0)
            current_scene.choices[1] = (["Leave it alone"], 0)
            current_scene.next_choices[0] = "Drawer Opened"
            current_scene.next_choices[1] = "Desk"
        else:
            current_scene.box_text = [["The drawer is locked. I don\'t have a key. I locked it for a reason."], 0]
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

def brush_teeth_special(engine):
    if not engine.TEETH_BRUSHED:
        engine.TEETH_BRUSHED = True

def wash_face_special(engine):
    if not engine.FACE_WASHED:
        engine.FACE_WASHED = True

def leak_special(engine):
    if not engine.TOOK_LEAK:
        engine.TOOK_LEAK = True


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

ENTERED_ALREADY = False
def living_room_special(engine):
    global ENTERED_ALREADY
    if ENTERED_ALREADY:
        current_scene = story.STORY_CHOICES.get("Living Room")
        if current_scene is not None:
            current_scene.box_text = [["My living room, empty, but full of me"], 0]
        return
    ENTERED_ALREADY = True

    if not engine.TEETH_BRUSHED:
        engine.deviance += 5
    if not engine.FACE_WASHED:
        engine.deviance += 5
    if not engine.TOOK_LEAK:
        engine.deviance += 5
    
    box = ""
    if not engine.TEETH_BRUSHED and not engine.FACE_WASHED and not engine.TOOK_LEAK:
        box += "As I step into the living room, the light from outside casts long shadows across the floor. The unwashed feeling of my face and the lingering taste of unbrushed teeth make me uneasy. My bladder feels full, a reminder of my neglect to take care of myself this morning. The weight of these oversights presses down on you, making each movement of mine feel heavier than the last."
    
    if engine.deviance > 50:
        box = "You know what you did."
    elif engine.deviance > 20:
        box += "\nOkay I get it. I don\'t matter much to you, but can you at least treat me like a person?"
    elif engine.deviance > 15:
        box += "\nLook I know this may be a game to you, but it would be nice to have you take some care on how you treat this day."
    elif engine.deviance < 50:
        box += "\nI walk into my living room, the emptiness is as prevalent as the lack of space. There isn\'t much to do here, but I try to find a way."

    current_scene = story.STORY_CHOICES.get("Living Room")
    if current_scene is not None:
        current_scene.box_text = [[box], 0]

def eggs_special(engine):
    if engine.EGGS is False:
        engine.EGGS = True

def stove_special(engine):
    if engine.EGGS is False:
        return
    current_scene = story.STORY_CHOICES.get("Stove")
    if current_scene is not None:
        current_scene.choices[0] = (["Cook the eggs"], 0)
        current_scene.next_choices[0] = "Cook Eggs"

def the_story_special(engine):
    current_scene = story.STORY_CHOICES.get("The Story")
    box = ""
    if engine.deviance > 25:
        box += "I\'m sure you tried your best, but you didn\'t seem to mind to spend your time watching me waste away or not do what I needed or… or… or… it can go on and on."
        current_scene.choices[0] = (["I\'m sorry I guess?"], 0)
        current_scene.next_choices[0] = "End"
    else:
        box += "Well that's nice to hear. I hope the mundane wasn\'t too mundane"
        current_scene.choices[0] = (["It wasn't that bad"], 0)
        current_scene.choices[1] = (["It was pretty bad"], 0)
        current_scene.next_choices[0] = "End"
        current_scene.next_choices[1] = "End"
    current_scene.box_text = [[box], 0]

def end_special(engine):
    current_scene = story.STORY_CHOICES.get("End")
    
    if engine.wants_typewriter:
        current_scene.box_text = [["Oh yeah... I guess I did ask for this typewriter. I don\'t know what I am supposed to do with it though..."], 0]
        current_scene.choices[0] = (["I don't know either"], 0)
        current_scene.next_choices[0] = "END"
    elif engine.wants_phone:
        current_scene.box_text = [["This is the phone I asked for. This is actually my old phone. I wonder if it still works"], 0]
        current_scene.choices[0] = (["Turn On"], 0)
        current_scene.choices[1] = (["Don\'t Bother"], 0)
        current_scene.next_choices[0] = "Turn on"
        current_scene.next_choices[1] = "Dont Turn on"
    elif engine.wants_harddrive:
        current_scene.box_text = [["Here is the harddrive I asked for… it does look a bit broken I don\'t think there is anything I can do with it unfortunately"], 0]
        current_scene.choices[0] = (["That is unfortunate..."], 0)
        current_scene.next_choices[0] = "END"
    else:
        current_scene.box_text = [["Theres my door"], 0]
        current_scene.choices[0] = (["Enter"], 0)
        current_scene.next_choices[0] = "END"

def dad_texts(engine):
    if not engine.dad1_found:
        scene = story.STORY_CHOICES.get("Old Phone Texts")
        scene.box_text = [["Nothing I can see here", "Still nothing"], 0]
        scene.choices[0] = (["anticlimactic"], 0)
        scene.next_choices[0] = "Turn On"
        return
    current_scene = story.STORY_CHOICES.get("Turn on")
    current_scene.choices[2] = (["Treasure it"], 0)
    
    scene = story.STORY_CHOICES.get("Old Phone Texts")
    scene.box_text = [["These... are my old texts with my dad before the car crash. I can't beleive they are still here. I would never have found them. I... I... thank you.\nHey kiddo, you and..."], 0]
    scene.choices[0] = (["Give space to read texts"], 0)
    scene.next_choices[0] = "SOLO_END"
