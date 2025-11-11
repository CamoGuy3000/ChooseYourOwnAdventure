import customtkinter
from story import TEST_STORY_CHOICES as S_C
from story import Choice

DEBUG = False # TODO

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

        self.update_scene("WIP")
    
    def update_scene(self, choice: str):

        scene: Choice = S_C[choice]

        self.story_label.configure(text=scene.box_text)        
        next_choices_names = scene.choices
        next_choice_links = scene.next_choices


        for i in range(4):
            button = self.choice_buttons[i]

            if i < len(next_choices_names):
                choice = next_choices_names[i]
                # Check if the choice doesn't exist
                if choice == "":
                    button.pack_forget()
                    continue
                    
                button.configure(
                    text=choice,
                    command=lambda next_node=next_choice_links[i]: self.update_scene(next_node)
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

