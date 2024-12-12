import webbrowser

def redirect_to_website():
    # Get the website link from the user
    website_link = input("Please enter the website link: ")

    # Open the provided website link in the default web browser
    webbrowser.open(website_link)

if __name__ == "__main__":
    redirect_to_website()
