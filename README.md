
# Technical Overview: ChooseYourOwnAdventure

This project is a choose your own adventure engine built in Python using `customtkinter` for the interface.

## Core Architecture

The entire application runs through `choose.py`, which sets up the main window class `TextChoice`.

### The Game Loop (`choose.py`)
Because of the nature of choice objects, the game is event-driven.
1.  **`update_scene(choice_key)`**: This is the main function. It takes a string key (like "Start" or "Kitchen"), looks up the corresponding `Choice` object in the `STORY_CHOICES` dictionary, and loads it.
2.  **`_start_typing()`**: I wrote a recursive function to handle the text display. It adds characters one by one to a `CTkTextbox`.
    * **Typos & Backspacing**: If the engine encounters the `^` character in the source text, it triggers a "backspace" effect, deleting the previous character and pausing briefly to simulate a human correcting a typo.
3.  **`_configure_buttons()`**: Once the text finishes typing, this function dynamically creates the buttons. It looks at the current scene's `next_choices` list and maps them to the button slots.

### Data Structure (`story.py`)
The story is stored in a Python dictionary called `STORY_CHOICES`.

Each node is an instance of the `Choice` class, which holds:
* `box`: The main story text.
* `choices`: The text that appears on the buttons.
* `next_choices`: The keys (strings) that the buttons link to.

### Dynamic Content & State Persistence
To make sure the player didn't just see the exact same text over and over again if they looped back to a room, I made a system that used tuples with a list with a stored index.

**The Tuple System**
Both the main text (`box`) and the button labels (`choice`) are stored as tuples: `([list_of_strings], index)`.
* Every time you click a button or leave a room, the code increments the `index` for that specific element.
* It uses logic like `min(index + 1, len - 1)` so it eventually "sticks" on the final variation of the text, after cycling through all of the rest.
* This allows the game to have a "standard" description the first time, a "bored" description the second time, and an "annoyed" description the third time.

### Logic & Special Events (`storyFunctions.py`)
While `story.py` handles the graph, `storyFunctions.py` handles the logic that breaks or modifies that graph.

I used a file called `specialChoices.py` to map specific node keys to functions. When the engine transitions to a node (e.g., "Snooze"), it checks if that key exists in `SPECIAL_CHOICES`. If it does, it runs the corresponding function in `storyFunctions.py`.

These functions do things like:
* **Modify Connectivity**: They can hot-swap the `next_choices` of a node. For example, if you hit snooze too many times, the `snooze_special` function physically rewrites the "Snooze" node to point to the "Lazy" ending instead of the "Wake Up" node.
* **Global Flags**: Variables like `HAVE_GUN` or `deviance` are tracked here. The ending you get (`the_story_special`) is just a function that checks these flags and dynamically rewrites the text of the final node before displaying it.