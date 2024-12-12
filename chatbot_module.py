import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
import importlib



class ChatUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ChatGPT-like Chatbot")
        self.master.configure(bg="#000000")  # Set background color to black
        self.master.attributes("-fullscreen", True)  # Make the window fullscreen
        self.master.bind("<F11>", lambda event: self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen")))
        self.master.bind("<Escape>", lambda event: self.master.attributes("-fullscreen", False))

        self.create_widgets()
    
    def close_application(self):
        self.master.destroy()

    def home(self):
        # You can add additional logic or actions before closing the chat window
        # For now, let's simply close the chat window
        self.close_application()    
        
    
    
        
        
    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.master, text="CHATBOT", font=("helvetica", 24, "bold"), bg="#000000", fg="#00BDFF")
        title_label.pack(side=tk.TOP, pady=10)

        self.text_widget = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=120, height=25, bg="#000000",fg="white")  # Set text color to green
        self.text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.entry_widget = tk.Entry(self.master, width=90, bg="#000000", fg="white", font=("Arial", 16))  # Set font size to 14
        self.entry_widget.pack(side=tk.LEFT, fill=tk.X, pady=5, padx=10)
        self.entry_widget.bind("<Return>", self.send_message_on_enter)  # Bind Enter key to send_message_on_enter

        self.send_button = tk.Button(self.master, text="SUBMIT", command=self.send_message, bg="#333333", fg="#00BDFF",font=("Arial", 14))  # Set font size to 14
        self.send_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.send_button1 = tk.Button(self.master, text="BACK", command=self.home, bg="#333333", fg="#00BDFF",font=("Arial", 14))  # Set font size to 14
        self.send_button1.pack(side=tk.LEFT, padx=15, pady=5)

    def send_message(self, event=None):
        user_input = self.entry_widget.get()
        self.entry_widget.delete(0, tk.END)

        response = self.get_chatbot_response(user_input)

        self.text_widget.insert(tk.END, f"You: {user_input}\nChatbot: {response}\n\n")
        self.text_widget.yview(tk.END)

    def send_message_on_enter(self, event):
        # Function to be called when Enter key is pressed in the entry widget
        self.send_message()

    def get_chatbot_response(self, user_input):
        # Check if the user input has specific patterns for Wikipedia search
        if any(keyword in user_input for keyword in ["search", "who is", "what is", "how is"]):
            # Extract the query after the search keywords
            query = next((user_input.split(keyword)[1].strip() for keyword in ["search", "who is", "what is", "how is"]
                        if keyword in user_input), None)

            if query:
                return self.wikibot_response(query)
            else:
                return "I'm sorry, I don't understand. Please provide a valid query."
        else:
            # Check for custom responses
            custom_response = self.custom_responses(user_input)
            if custom_response:
                return custom_response
            else:
                # No custom response found, use the entire input as the query for Wikipedia
                return self.wikibot_response(user_input)

    def custom_responses(self, user_input):
        # Add your custom datasets and responses here
        custom_qa_dict = {
            "Who made you?": "I was developed collaboratively by a group of students enrolled at Kalsekar Polytechnic College in Navi Mumbai, Panvel. Our aim was to create a cutting-edge solution to assist fellow students. Notable contributors to this initiative include Anas Khan, Talha Dalvi, Faiz Khan, and Ayaan Deshmukh. Together, we endeavored to design a modern and effective tool that addresses the unique challenges faced by students, offering valuable support and enhancing the overall educational experience",
            "Hello": "Hello sir welcome to chatbot section of Diploma Assistant AI",
            "help": 
""" Welcome to Diploma Assistant AI! 
Diploma Assistant AI is a cutting-edge software designed to elevate the educational journey of diploma students. 🎓 It's your all-in-one solution for a seamless learning experience.
 --Key Features-- 
- Syllabus Management 
- Study Schedule Planning 
- Project Creation 
- Chatbot Tutor 
*User-Friendly Commands 
1. Hello: Greet your AI assistant!
2. Who made you?: Learn about the brilliant minds behind this creation.
3. How does the chatbot work?: Understand the magic behind your virtual tutor.
4. What are the key features of DMS?**: Explore the powerful features at your fingertips.
5. What is the use of DMS?: Discover how DMS enhances your educational journey.
Get ready to experience education like never before with Diploma Assistant AI! 🎉
""",
            "How does the chatbot work?": "The chatbot utilizes predefined datasets to respond to specific questions about Diploma Assistant AI. It matches user input with stored questions and provides corresponding answers.",
            "What are the key features of dms?": "Key features include syllabus management, study schedule planning, project creation, chatbot assistance, language translation, deadline reminders, and motivational speeches.",
            "What is the use of dms?": "Diploma Assistant AI is a multifaceted software designed to support the diverse needs of students, educators, and administrators in diploma programs. By integrating features like syllabus management, question bank creation, project management, study schedule planning, and a chatbot tutor, the software aims to streamline educational processes. Additional functionalities, such as language translation, deadline reminders, voice commands, motivational speeches, and a dedicated website for project reviews, contribute to an enriched learning experience. The software is a comprehensive tool designed to enhance collaboration, efficiency, and engagement within the context of diploma education",
            # Add more question-answer pairs as needed
            # Add more question-answer pairs as needed
        }

        # Check if the user's input matches any custom question
        for question in custom_qa_dict:
            if user_input.lower() in question.lower():
                return custom_qa_dict[question]

        # If no match is found
        return None

    def wikibot_response(self, query):
        url = self.search_wikipedia(query)
        return self.wikibot(url)

    @staticmethod
    def search_wikipedia(query):
        formatted_query = query.replace(' ', '_')
        search_url = f"https://www.wikipedia.org/wiki/{formatted_query}"
        return search_url

    @staticmethod
    def wikibot(url):
        url_open = requests.get(url)
        soup = BeautifulSoup(url_open.content, 'html.parser')

        # Get details from the infobox
        details = soup.find('table', {'class': 'infobox'})
        response = ""

        if details:
            rows = details.find_all('tr')
            for row in rows:
                heading = row.find('th')
                detail = row.find('td')
                if heading and detail:
                    response += f"{heading.text} :: {detail.text}\n"
                    response += "-------------------\n"

        # Get content from paragraphs
        paragraphs = soup.find_all('p')
        for i in range(min(3, len(paragraphs))):  # Display at most the first 3 paragraphs
            response += f"{paragraphs[i].text}\n"

        # Filter out unnecessary information
        response = response.replace("[1]", "").strip()

        return response


if __name__ == "__main__":
    root = tk.Tk()
    chat_ui = ChatUI(root)
    root.mainloop()