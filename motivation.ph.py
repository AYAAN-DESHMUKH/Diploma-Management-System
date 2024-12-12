import tkinter as tk
from tkinter import Label

import requests
from bs4 import BeautifulSoup 
r = requests.get('https://www.inspiringquotes.com/')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='IQDailyInspiration__quoteContainer')
lines = s.find_all('h1')
for line in lines:
	quote=line.text
cont=soup.find('div',class_='IQDailyInspiration__author')
for line in cont:
    author=line.text
theory=soup.find('div',class_='IQDailyInspiration__explanation')
details=theory.find('div')
explain=details.text




# Function to add entry animation
def entry_animation(label, text, delay):
    for i in range(len(text)):
        label.config(text=text[:i+1])
        label.update()
        label.after(delay)

# Function to exit the program on pressing Escape key
def exit_on_escape(event):
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Motivational Quotes")

# Configure the window to full screen
root.attributes('-fullscreen', True)

# Set the background color to black
root.configure(bg="black")

# Create a label for the motivational quote
quote_text = "Inspire Quest"
quote_label = Label(root, text=quote_text, font=("Helvetica", 30, "bold"), fg="yellow", bg="black")
quote_label.pack(side="top",pady=70)

# Create a label for the animated motivational text
animated_text_label = Label(root, text="", font=("garamond", 20, "bold"), fg="white", bg="black",wraplength=800)
animated_text_label.pack()

# Call the entry_animation function with the label and text for the motivational text
entry_animation(animated_text_label, quote, 100)

# Create a label for the animated writer's name
writer_name = author
writer_label = Label(root, text="", font=("Helvetica", 15, "italic"), fg="gray", bg="black")
writer_label.pack(pady=20)

# Different entry animation for the writer's name
for char in writer_name:
    writer_label.config(text=writer_label.cget("text") + char)
    writer_label.update()
    root.after(100)
    
paragraph_text = "Your additional information about the author goes here."
paragraph_label = Label(root, text="", font=("garamond", 14), fg="white", bg="black", justify="center",wraplength=800)
paragraph_label.pack(pady=80)
def fade_in_animation(label, text, delay):
    label.config(text=text)
    current_color = label.cget("bg")
    for i in range(1, 11):
        alpha = i / 10.0
        new_color = label.winfo_rgb(current_color) + (alpha,)
        new_color = "#%04x%04x%04x" % new_color[:-1]
        label.config(bg=new_color)
        label.update()
        label.after(delay)
# Fade-in animation for the paragraph
fade_in_animation(paragraph_label, explain, 100)

# Bind the Escape key to the exit function
root.bind("<Escape>", exit_on_escape)

# Run the Tkinter event loop
root.mainloop()
