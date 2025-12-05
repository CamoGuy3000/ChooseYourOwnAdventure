import customtkinter
from gameStats import SPECIAL_CHOICES
from story import TEST_STORY_CHOICES as S_C
from story import Choice

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

        self.update_scene("WIP")
    
    def update_scene(self, choice: str):

        if self.typing_job:
            self.after_cancel(self.typing_job)
            self.typing_job = None

        for button in self.choice_buttons:
            button.pack_forget()

        scene: Choice = S_C[choice]
        self._start_typing(''.join(scene.box_text), scene)
    


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
                # Extract the list of options and the current index for this button slot
                options_list = next_choices_names[i][0]
                current_index = next_choices_names[i][1]
                
                # Get the text based on the current index
                choice_text = options_list[current_index]

                # Check if the choice text is empty (hidden choice)
                if choice_text == "":
                    button.pack_forget()
                    continue
                
                # Define what happens when the button is clicked
                def on_click(idx=i, next_node=next_choice_links[i]):
                    if next_node in SPECIAL_CHOICES:
                        SPECIAL_CHOICES[next_node]()  # Call the special function
                    # 1. Update the choice index for the NEXT time we come here
                    opts, c_idx = next_choices_names[idx]
                    # Cycle to the next text option (wrap around to 0 if at the end)
                    new_idx = min((c_idx + 1), len(opts) - 1)
                    next_choices_names[idx] = (opts, new_idx)
                    
                    # 2. Move to the next scene
                    self.update_scene(next_node)

                button.configure(
                    text=choice_text,
                    command=on_click
                )

                button.pack(pady=8, padx=10, fill="x")
            else:
                button.pack_forget()



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

