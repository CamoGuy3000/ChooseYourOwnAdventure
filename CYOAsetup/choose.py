import customtkinter
from specialChoices import SPECIAL_CHOICES
from story import STORY_CHOICES as S_C
# from story import TEST_STORY_CHOICES as S_C
from story import Choice
# import specialFunctions

DEBUG = True

# REMOVE global TYPING_SPEED here

class TextChoice(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        # Define typing speed here as an instance variable
        self.normal_typing_speed = 0 if DEBUG else 30
        self.typing_speed = 0 if DEBUG else 100
        self.HAVE_KEY = True if DEBUG else False
        self.HAVE_CODE = True if DEBUG else False
        self.HAVE_GUN = False
        self.BAG_PACKED = False
        self.WATCH_ON = False

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
            font=("Georgia", 18),
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
        
        self.update_scene("Start")
        self.after(27 * 1000, self._make_snooze)

    
    def update_scene(self, choice: str):
        if self.typing_job:
            self.after_cancel(self.typing_job)
            self.typing_job = None

        for button in self.choice_buttons:
            button.pack_forget()

        self.current_scene = S_C[choice]
        scene = self.current_scene

        text_options, text_index = scene.box_text
        current_text = text_options[text_index]

        self._start_typing(''.join(current_text), scene)


    def _perform_backspace(self, full_text, scene, index):
        self.story_label.configure(text=full_text[:index])
        
        self.typing_job = self.after(
            350 - (175 if full_text[index+1]=='^' else 0), 
            lambda: self._start_typing(full_text, scene, index, True)
        )

    def _start_typing(self, full_text, scene: Choice, index=0, back=False):
        if index < len(full_text):
            current_display_text = full_text[:index+1]
            self.story_label.configure(text=current_display_text)

            # USE SELF.TYPING_SPEED HERE
            speed = self.typing_speed

            char = full_text[index]
            if char == '^':
                if index + 1 < len(full_text):
                    full_text = full_text[:index-1] + full_text[index+1:]
                    index -= 1              
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
            self.typing_job = None
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
                
                def on_click(idx=i, next_node=next_choice_links[i]):
                    if next_node in SPECIAL_CHOICES:
                        # PASS 'SELF' TO THE FUNCTION
                        SPECIAL_CHOICES[next_node](self)
                    
                    btn_opts, btn_idx = next_choices_names[idx]
                    next_choices_names[idx] = (btn_opts, min(btn_idx + 1, len(btn_opts) - 1))
                    
                    if hasattr(self, 'current_scene'):
                        box_opts, box_idx = self.current_scene.box_text
                        self.current_scene.box_text = (box_opts, min(box_idx + 1, len(box_opts) - 1))

                    self.update_scene(next_node)

                button.configure(text=choice_text, command=on_click)
                button.pack(pady=8, padx=10, fill="x")
            else:
                button.pack_forget()
    
    def _make_snooze(self):
        S_C["Start"].choices[3] = (["Snooze"], 0)
        if self.current_scene == S_C["Start"]:
            self._configure_buttons(S_C["Start"].choices, S_C["Start"].next_choices)

if __name__ == "__main__":
    app = TextChoice()
    app.mainloop()