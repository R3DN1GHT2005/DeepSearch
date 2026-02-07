import customtkinter as ctk

class SearchInputField(ctk.CTkEntry):
    def __init__(self, master, placeholder):
        super().__init__(master, placeholder_text=placeholder, width=280, height=35, corner_radius=10)

class ActionButton(ctk.CTkButton):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command, font=("Segoe UI", 14, "bold"), height=45)