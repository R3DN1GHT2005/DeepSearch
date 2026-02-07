import customtkinter as ctk
import webbrowser
from search import QueryArchitect
from ui import SearchInputField, ActionButton


class GoogleOperatorsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Google Advanced Search")
        self.geometry("400x800")
        self.resizable(False, False)
        
        self.architect = QueryArchitect()
        self.inputs = {}
        
        self._setup_ui()
    
    def _setup_ui(self):
        ctk.CTkLabel(self, text="ADVANCED SEARCH", font=("Segoe UI", 22, "bold")).pack(pady=20)
        
        self.container = ctk.CTkScrollableFrame(self, width=360, height=520)
        self.container.pack(padx=10, pady=10)

        fields = [
            ("keyword", "Primary Keyword / Phrase"),
            ("exclude", "Exclude Words (comma-separated)"),
            ("or_terms", "OR Terms (comma-separated)"),
            ("site", "Target Domain (e.g., github.com)"),
            ("filetype", "File Extension (e.g., pdf, xlsx)"),
            ("intitle", "Text in Page Title"),
            ("inurl", "Text in URL Path"),
            ("before", "Before Date (YYYY-MM-DD)"),
            ("after", "After Date (YYYY-MM-DD)"),
            ("define", "Word to Define"),
            ("cache", "Cached Page URL"),
            ("link", "Pages Linking to URL")
        ]

        for key, label in fields:
            ctk.CTkLabel(self.container, text=label).pack(anchor="w", padx=20)
            entry = SearchInputField(self.container, f"Enter {key}...")
            entry.pack(pady=(0, 10))
            self.inputs[key] = entry

            if key == "keyword":
                self.exact_match_var = ctk.BooleanVar(value=False)
                self.chk_exact = ctk.CTkCheckBox(
                    self.container, 
                    text="Use Exact Match (Quotes)", 
                    variable=self.exact_match_var,
                    font=("Segoe UI", 12),
                    checkbox_width=20, checkbox_height=20
                )
                self.chk_exact.pack(anchor="w", padx=20, pady=(0, 15))

        self.preview_frame = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.preview_frame.pack(pady=10, fill="x", padx=40)
        
        ctk.CTkLabel(self.preview_frame, text="Query Preview:", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(5, 0))
        
        self.preview_label = ctk.CTkLabel(self.preview_frame, text="(empty query)", font=("Segoe UI", 10), wraplength=320, justify="left")
        self.preview_label.pack(anchor="w", padx=10, pady=(0, 5))
        
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10, fill="x", padx=40)
        
        self.clear_btn = ctk.CTkButton(button_frame, text="CLEAR ALL", command=self.clear_all, 
        font=("Segoe UI", 12, "bold"), height=40, fg_color="#d32f2f", hover_color="#b71c1c")
        self.clear_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        self.submit_btn = ActionButton(button_frame, "RUN SEARCH", self.execute_logic)
        self.submit_btn.pack(side="right", expand=True, fill="x", padx=(5, 0))
        
        for entry in self.inputs.values():
            entry.bind("<KeyRelease>", lambda e: self.update_preview())
        self.exact_match_var.trace("w", lambda *args: self.update_preview())

    def update_preview(self):
        """Update the query preview"""
        raw_values = {key: entry.get() for key, entry in self.inputs.items()}
        raw_values["exact_match"] = self.exact_match_var.get()
        preview_text = self.architect.build_preview_query(raw_values)
        self.preview_label.configure(text=preview_text)
    
    def clear_all(self):
        """Clear all input fields"""
        for entry in self.inputs.values():
            entry.delete(0, "end")
        self.exact_match_var.set(False)
        self.update_preview()
    
    def execute_logic(self):
        raw_values = {key: entry.get() for key, entry in self.inputs.items()}
        raw_values["exact_match"] = self.exact_match_var.get()
        final_url = self.architect.build_google_url(raw_values)
        
        if final_url.startswith("ERROR:"):
            self.preview_label.configure(text=final_url, text_color="#ff5252")
        elif final_url:
            webbrowser.open(final_url)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = GoogleOperatorsApp()
    app.mainloop()