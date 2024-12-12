import tkinter as tk
from tkinter import Label

import requests
from bs4 import BeautifulSoup


class MotivationalQuotesApp:
    
        
     

    def home(self):
        self.root.destroy()
       
    def on_enter_custom_button(self, event):
            self.custom_button.config(bg="yellow", fg="black")

    def on_leave_custom_button(self, event):
            self.custom_button.config(bg="black", fg="white")
            
            
    def __init__(self, root): 
          
         
        
        r = requests.get('https://www.inspiringquotes.com/')
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('div', class_='IQDailyInspiration__quoteContainer')
        lines = s.find_all('h1')
        for line in lines:
            self.quote = line.text
        cont = soup.find('div', class_='IQDailyInspiration__author')
        for line in cont:
            self.author = line.text
        theory = soup.find('div', class_='IQDailyInspiration__explanation')
        details = theory.find('div')
        self.explain = details.text

        # Create the main window
        self.root = root
        self.root.title("Motivational Quotes")

        # Configure the window to full screen
        self.root.attributes('-fullscreen', True)

        # Set the background color to black
        self.root.configure(bg="black")

        # Create a label for the motivational quote
        quote_text = "Inspire Quest"
        self.quote_label = Label(root, text=quote_text, font=("Helvetica", 30, "bold"), fg="yellow", bg="black")
        self.quote_label.pack(side="top", pady=70)

        # Create a label for the animated motivational text
        self.animated_text_label = Label(root, text="", font=("garamond", 20, "bold"), fg="white", bg="black", wraplength=800)
        self.animated_text_label.pack()

        # Call the entry_animation function with the label and text for the motivational text
        self.entry_animation(self.animated_text_label, self.quote, 63)

        # Create a label for the animated writer's name
        self.writer_name = self.author
        self.writer_label = Label(root, text="", font=("Helvetica", 15, "italic"), fg="gray", bg="black")
        self.writer_label.pack(pady=20)

        # Different entry animation for the writer's name
        for char in self.writer_name:
            self.writer_label.config(text=self.writer_label.cget("text") + char)
            self.writer_label.update()
            root.after(100)

        # Create a label for the animated paragraph
        paragraph_text = "Your additional information about the author goes here."
        self.paragraph_label = Label(root, text="", font=("garamond", 14), fg="white", bg="black", justify="center", wraplength=800)
        self.paragraph_label.pack(pady=50)
          # Custom button
        
        # Fade-in animation for the paragraph
        self.fade_in_animation(self.paragraph_label, self.explain, 100)

        # Bind the Escape key to the exit function
        root.bind("<Escape>", self.exit_on_escape)

    def entry_animation(self, label, text, delay):
        for i in range(len(text)):
            label.config(text=text[:i+1])
            label.update()
            label.after(delay)

    def exit_on_escape(self, event):
        self.root.destroy()

    def fade_in_animation(self, label, text, delay):
        label.config(text=text)
        current_color = label.cget("bg")
        for i in range(1, 11):
            alpha = i / 10.0
            new_color = label.winfo_rgb(current_color) + (alpha,)
            new_color = "#%04x%04x%04x" % new_color[:-1]
            label.config(bg=new_color)
            label.update()
            label.after(delay)

        self.custom_button = tk.Button(self.root, text="EXIT", font=("Arial", 30), command=self.home,
                               fg="white", bg="black", bd=0, highlightthickness=0)
        self.custom_button.place(x=627,y=650)
        
      
            # Hover effects for custom button
        self.custom_button.bind("<Enter>", self.on_enter_custom_button)
        self.custom_button.bind("<Leave>", self.on_leave_custom_button)
if __name__ == "__main__":
    root = tk.Tk()
    app = MotivationalQuotesApp(root)
    root.mainloop()
