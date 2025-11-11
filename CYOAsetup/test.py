import customtkinter

class App(customtkinter.CTk):
    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("test123")
        self.geometry("400x250")  # Increased height a bit for the new widget
        self.grid_columnconfigure((0, 1), weight=1) # Configure columns 0 and 1

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        # Using the choices from your comments
        option_choices = ["Choice1", "Choice2", "Choice3", "Choice4"]
        optionmenu_var = customtkinter.StringVar(value="Choice2") # Default value
        
        optionmenu = customtkinter.CTkOptionMenu(self, values=option_choices,
                                                 command=optionmenu_callback,
                                                 variable=optionmenu_var)
        
        # --- THIS WAS THE MISSING LINE ---
        optionmenu.grid(row=2, column=0, padx=20, pady=10, sticky="ew", columnspan=2)
            
    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()