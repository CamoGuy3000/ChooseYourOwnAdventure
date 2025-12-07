import customtkinter
from gameStats import SPECIAL_CHOICES
# from story import STORY_CHOICES as S_C
from story import TEST_STORY_CHOICES as S_C
from story import Choice
# import specialFunctions

DEBUG = False # TODO

TYPING_SPEED = 30  # Lower is faster

class TextChoice(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Choose")
        # self.geometry("1920x1080")
        self.geometry("810x540")

        # Frame for choices at the bottom
        self.choice_frame = customtkinter.CTkFrame(
            self,
            height=200,
            fg_color="transparent"
        )
        self.choice_frame.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=(10,20)
        )
        self.choice_frame.pack_propagate(False)

        # Story label at the top
        self.story_label = customtkinter.CTkLabel(
            self,
            text="",
            wraplength=550,
            font=("Arial", 18),
            anchor="center",
        )
        self.story_label.pack(
            side="top",     
            fill="both",    
            expand=True,    
            pady=20, 
            padx=20
        )

        # Create dummy buttons
        self.choice_buttons = []
        for _ in range(4):
            button = customtkinter.CTkButton(self.choice_frame, text="")
            self.choice_buttons.append(button)

        self.typing_job = None

        global TYPING_SPEED
        # TYPING_SPEED = 100
        self.update_scene("Start")
        self.after(27 * 1000, self._make_snooze)
        # TYPING_SPEED = 30

    
    def update_scene(self, choice: str):
        if self.typing_job:
            self.after_cancel(self.typing_job)
            self.typing_job = None

        for button in self.choice_buttons:
            button.pack_forget()

        # 1. Store the current scene object so we can access it in the button callback
        self.current_scene = S_C[choice]
        scene = self.current_scene

        # 2. Get the current text based on the saved index
        text_options, text_index = scene.box_text
        current_text = text_options[text_index]

        self._start_typing(''.join(current_text), scene)


    def _perform_backspace(self, full_text, scene, index):
        self.story_label.configure(text=full_text[:index])
        
        self.typing_job = self.after(
            350 - (175 if full_text[index+1]=='^' else 0), # Time to reset
            lambda: self._start_typing(full_text, scene, index, True)
        )

    def _start_typing(self, full_text, scene: Choice, index=0, back=False):

        if index < len(full_text):
            current_display_text = full_text[:index+1]
            self.story_label.configure(text=current_display_text)

            speed = TYPING_SPEED

            char = full_text[index]
            if char == '^':
                if index + 1 < len(full_text):
                    full_text = full_text[:index-1] + full_text[index+1:]
                    index -= 1              # Time mistake is shown
                    self.typing_job = self.after(200 - (150 if back else 50), self._perform_backspace(full_text, scene, index))
                else:
                    self.typing_job = self.after(1, lambda: self._start_typing(full_text, scene, index+1))
                return

            speed += 30 if back else 0

            self.typing_job = self.after(
                speed,
                lambda: self._start_typing(full_text, scene, index + 1)
            )
        else:
            # --- Typing is finished ---
            self.typing_job = None
            # Now, show the buttons for this scene
            next_choices_names = scene.choices
            next_choice_links = scene.next_choices
            self._configure_buttons(next_choices_names, next_choice_links)

    def _configure_buttons(self, next_choices_names, next_choice_links):
        for i in range(4):
            button = self.choice_buttons[i]

            if i < len(next_choices_names):
                options_list = next_choices_names[i][0]
                current_index = next_choices_names[i][1]
                choice_text = options_list[current_index]

                if choice_text == "":
                    button.pack_forget()
                    continue
                
                # Update the callback to cycle the BOX text as well
                def on_click(idx=i, next_node=next_choice_links[i]):
                    # 1. Cycle the BUTTON text for the next time we see this specific button
                    btn_opts, btn_idx = next_choices_names[idx]
                
                    next_choices_names[idx] = (btn_opts, min(btn_idx + 1, len(btn_opts) - 1))
                    
                    # 2. Cycle the BOX text for the next time we visit this scene
                    # We access the scene object we saved in update_scene
                    box_opts, box_idx = self.current_scene.box_text
                    self.current_scene.box_text = (box_opts, min(box_idx + 1, len(box_opts) - 1))

                    # 3. Move to the next scene
                    self.update_scene(next_node)

                button.configure(text=choice_text, command=on_click)
                button.pack(pady=8, padx=10, fill="x")
            else:
                button.pack_forget()
    
    def _make_snooze(self):
        S_C["Start"].choices[3] = (["Snooze"], 0)
        self._configure_buttons(S_C["Start"].choices, S_C["Start"].next_choices)



# ex_choice: Choice = Choice("ex thing", ["choice 1", "choice 2", "choice 3", "choice 4"])

app = TextChoice()
# app.update_scene(ex_choice)
app.mainloop()

## 
## Text
## 
## 
## Choice1
## Choice2
## Choice3
## Choice4

