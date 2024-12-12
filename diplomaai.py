import tkinter as tk
from PIL import Image, ImageTk
from chatbot_module import ChatUI 
from motivation import MotivationalQuotesApp
from tkinter import scrolledtext
from projectmakerui import ProjectInfoUI
from qm import QB


class Diploma:
    def __init__(self, root):
        self.root = root
        self.root.title("Diploma Management System")
        self.root.configure(bg="black")

        # Displaying the title text
        self.title_label = tk.Label(self.root, text="Diploma Management System", font=("ALGERIAN", 50), fg="white", bg="black")
        self.title_label.pack(pady=10)
        self.title_label.place(x=230, y=50)

        # Image paths for the icons
        self.chatbot_icon_path = "C:/Users/Ayaan Deshmukh/Downloads/chat.png"
        self.project_maker_path = "C:/Users/Ayaan Deshmukh/Downloads/project.png"
        self.motivation_path = "C:/Users/Ayaan Deshmukh/Downloads/motivation.png"
        self.sylabus_path = "C:/Users/Ayaan Deshmukh/Downloads/sylabus.png"
        self.timetable_path = "C:/Users/Ayaan Deshmukh/Downloads/exam.png"

        # Load and resize the icons
        self.chatbot_icon = Image.open(self.chatbot_icon_path).resize((200, 200))
        self.project_icon = Image.open(self.project_maker_path).resize((200, 200))
        self.motivation_icon = Image.open(self.motivation_path).resize((200, 200))
        self.sylabus_icon = Image.open(self.sylabus_path).resize((200, 200))
        self.timetable_icon = Image.open(self.timetable_path).resize((200, 200))
        self.project_icon_photo = ImageTk.PhotoImage(self.project_icon)
        self.photo_chatbot_icon = ImageTk.PhotoImage(self.chatbot_icon)
        self.motivation_icon_photo = ImageTk.PhotoImage(self.motivation_icon)
        self.sylabus_icon_photo = ImageTk.PhotoImage(self.sylabus_icon)
        self.timetable_photo_icon = ImageTk.PhotoImage(self.timetable_icon)

        # Create buttons with the icons
        self.btn_chatbot = tk.Button(self.root, image=self.photo_chatbot_icon, text="Search", compound="top",
                                     command=self.open_chatbot_window, fg="white", bg="black", bd=0, highlightthickness=0)
        self.btn_project = tk.Button(self.root, image=self.project_icon_photo, text="Project Maker", compound="top",
                                     command=self.project_maker, fg="white", bg="black", bd=0, highlightthickness=0)
        self.btn_motivation = tk.Button(self.root, image=self.motivation_icon_photo, text="Motivational Speeches",
                                        command=self.show_motivational_quotes, compound="top", fg="white", bg="black", bd=0, highlightthickness=0)
        self.btn_sylabus = tk.Button(self.root, image=self.sylabus_icon_photo, text="Sylabus", compound="top",
                                     fg="white", bg="black", bd=0, highlightthickness=0)
        self.btn_timetable = tk.Button(self.root, image=self.timetable_photo_icon, text="Question Maker", compound="top",
                                       fg="white", bg="black", bd=0, highlightthickness=0,command=self.questionmaker)

        # Pack buttons
        self.btn_chatbot.pack(side="left", padx=30)
        self.btn_project.pack(side="left", padx=30)
        self.btn_motivation.pack(side="left", padx=30)
        self.btn_sylabus.pack(side="left", padx=30)
        self.btn_timetable.pack(side="left", padx=40)

        # Hover effects for chatbot
        self.btn_chatbot.bind("<Enter>", self.on_enter_chatbot)
        self.btn_chatbot.bind("<Leave>", self.on_leave_chatbot)

        # Hover effects for project maker
        self.btn_project.bind("<Enter>", self.on_enter_project)
        self.btn_project.bind("<Leave>", self.on_leave_project)

        # Hover effects for motivation
        self.btn_motivation.bind("<Enter>", self.on_enter_motivation)
        self.btn_motivation.bind("<Leave>", self.on_leave_motivation)

        # Hover effects for sylabus
        self.btn_sylabus.bind("<Enter>", self.on_enter_sylabus)
        self.btn_sylabus.bind("<Leave>", self.on_leave_sylabus)

        # Hover effects for timetable
        self.btn_timetable.bind("<Enter>", self.on_enter_timetable)
        self.btn_timetable.bind("<Leave>", self.on_leave_timetable)

        # Full screen
        self.root.attributes("-fullscreen", True)

        # Custom button
        self.custom_button = tk.Button(self.root, text="EXIT", font=("Arial", 25), command=self.exit_application,
                                       fg="white", bg="black", bd=0, highlightthickness=0)
        self.custom_button.place(x=1150,y=650)

        # Hover effects for custom button
        self.custom_button.bind("<Enter>", self.on_enter_custom_button)
        self.custom_button.bind("<Leave>", self.on_leave_custom_button)

        # Exiting full screen on pressing Escape key
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))

    def open_chatbot_window(self):
        chatbot_root = tk.Toplevel()
        chat_ui = ChatUI(chatbot_root)

    def show_motivational_quotes(self):
        motivational_root = tk.Toplevel()
        app = MotivationalQuotesApp(motivational_root)

    def questionmaker(self):
        q = tk.Toplevel()
        qs = QB(q)
        
    def project_maker(self):
        project_root = tk.Toplevel()
        project_info_ui = ProjectInfoUI(project_root)

    def exit_application(self):
        self.root.destroy()

    def on_enter_chatbot(self, event):
        self.btn_chatbot.config(bg="lightblue", fg="lightblue")

    def on_leave_chatbot(self, event):
        self.btn_chatbot.config(bg="black", fg="white")

    def on_enter_project(self, event):
        self.btn_project.config(bg="yellow", fg="black")

    def on_leave_project(self, event):
        self.btn_project.config(bg="black", fg="white")

    def on_enter_motivation(self, event):
        self.btn_motivation.config(bg="orange", fg="black")

    def on_leave_motivation(self, event):
        self.btn_motivation.config(bg="black", fg="white")

    def on_enter_sylabus(self, event):
        self.btn_sylabus.config(bg="pink", fg="black")

    def on_leave_sylabus(self, event):
        self.btn_sylabus.config(bg="black", fg="white")

    def on_enter_timetable(self, event):
        self.btn_timetable.config(bg="#FFE5B4", fg="black")

    def on_leave_timetable(self, event):
        self.btn_timetable.config(bg="black", fg="white")

    def on_enter_custom_button(self, event):
        self.custom_button.config(bg="white", fg="black")

    def on_leave_custom_button(self, event):
        self.custom_button.config(bg="black", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    diploma_system = Diploma(root)
    root.mainloop()
