############################################
# version 2.0
######################################
import csv
import os
import hashlib
import kivy
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooser

class UniqueNumberGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(UniqueNumberGenerator, self).__init__(**kwargs)

        # Create a label
        self.label = Label(text="Enter your name:")

        # Create a text input
        self.text_input = TextInput()  # Remove 'id' property
        
        # Create a text input for entering numbers
        self.number_input = TextInput(hint_text="Enter number of Children", multiline=False, input_filter='int')

        # Create a button
        self.button = Button(text="Generate Unique Number", on_press=self.generate_unique_number)

        # Add widgets to the layout
        self.add_widget(self.label)
        self.add_widget(self.text_input)
        self.add_widget(self.number_input)
        self.add_widget(self.button)

    def generate_unique_number(self, instance):
        # Get user input from TextInput widget
        name = self.text_input.text.strip()
        number = self.number_input.text.strip()  # Get the entered number
        
        if name:
            # Use hashlib to generate a unique hash based on the input name
            hashed_name = hashlib.sha256(name.encode()).hexdigest()

            # Take the first 6 characters of the hash and set it to the Label widget
            unique_number = hashed_name[:5]

            # Get the current date and time
            current_datetime = datetime.now()

            self.label.text = "Unique Number: " + unique_number

            # Clear the text input
            self.text_input.text = ""
            
            # Clear the text input for number
            self.number_input.text = ""  # This line clears the number input widget after generating the unique number

            # Save data to CSV file in the user's home directory
            csv_file_path = os.path.expanduser('~/OurData.csv')
            with open(csv_file_path, mode='a', newline='') as file:
                fieldnames = ["Name", "Number", "Unique Number", "Date and Time"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Write the header only if the file is empty (optional)
                if os.stat(csv_file_path).st_size == 0:
                    writer.writeheader()
                    print("Header written to CSV file")
                
                # Write the data row
                writer.writerow({
                    "Name": name,
                    "Number": number,
                    "Unique Number": unique_number,
                    "Date and Time": current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                })
                print("Data written to CSV file")

# Get the screen width
screen_width = Window.size[0]

# Set the minimum width of the window to the screen width
Window.minimum_width = screen_width

# Set the minimum height of the window to 200 pixels
Window.minimum_height = 200

# Inside UniqueNumberApp class
class UniqueNumberApp(App):
    def build(self):
        self.title = "Nairobi Chapel GreenPark Sunday School Register"

        # Load the image
        image = Image(source='C:/Users/scott/OneDrive/Documents/Python_Israel/KIVY/header.jpg')
        
        # Set the size hint of the image to None for both width and height
        image.size_hint = (1, 1)

        # Ensure the image maintains its aspect ratio by setting keep_ratio to False
        image.keep_ratio = False

        # Allow the image to fill the available space
        image.allow_stretch = True

        # Set the size of the image
        image.size_hint_y = None
        image.height = 300
        
        # Create a BoxLayout to hold the image
        image_layout = BoxLayout(orientation='vertical')
        image_layout.add_widget(image)

        # Create a footer Label
        footer_label = Label(text="Copyright © 2024 Nairobi Chapel GreenPark.  All rights reserved by Scott[code zena].",
                             size_hint_y=None, height=30)

        # Create a BoxLayout to hold the footer label
        footer_layout = BoxLayout(orientation='horizontal')
        footer_layout.add_widget(footer_label)
        
        # Create a BoxLayout to hold the UniqueNumberGenerator and footer layout
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(UniqueNumberGenerator())
        main_layout.add_widget(footer_layout)
        
        # Create a BoxLayout to hold the image layout and main layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(image_layout)
        layout.add_widget(main_layout)

        return layout

if __name__ == "__main__":
    UniqueNumberApp().run()


