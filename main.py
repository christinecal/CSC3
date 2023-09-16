import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import urllib.request as request
import urllib.parse
import json

class RegistrationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Registration")
        self.geometry("400x400+400+200")  # Adjusted window size

        self.label_1 = tk.Label(self, text="Create Your Account", width=30, font=("bold", 15))
        self.label_1.pack(pady=10)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()

        # Error message label for the Name input
        self.name_error_label = tk.Label(self, text="", fg="red")
        self.name_error_label.pack()

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.pack()
        self.age_entry = ttk.Entry(self)
        self.age_entry.pack()

        # Error message label for the Age input
        self.age_error_label = tk.Label(self, text="", fg="red")
        self.age_error_label.pack()

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        # Error message label for the Username input
        self.username_error_label = tk.Label(self, text="", fg="red")
        self.username_error_label.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        # Error message label for the Password input
        self.password_error_label = tk.Label(self, text="", fg="red")
        self.password_error_label.pack()

        # Add padding below the entry fields
        self.entry_padding = tk.Label(self, text="", height=1)
        self.entry_padding.pack()

        self.register_btn = ttk.Button(self, text="Register", command=self.register)
        self.register_btn.pack()

    def display_name_error_message(self, message):
        self.name_error_label.config(text=message, fg="red")

    def display_age_error_message(self, message):
        self.age_error_label.config(text=message, fg="red")

    def display_username_error_message(self, message):
        self.username_error_label.config(text=message, fg="red")

    def display_password_error_message(self, message):
        self.password_error_label.config(text=message, fg="red")

    def validate_name(self):
        name = self.name_entry.get()

        if not name.strip():
            self.display_name_error_message("Please enter a name.")
            return False

        if not all(char.isalpha() or char.isspace() for char in name):
            self.display_name_error_message("Name must contain only letters and spaces.")
            return False

        if len(name) < 3:
            self.display_name_error_message("Name is too short. Please enter a valid name.")
            return False

    # Clear any previous error message
        self.display_name_error_message("")
        return True


    def validate_age(self):
        age = self.age_entry.get()

        if not age.strip():
            self.display_age_error_message("Please enter an age.")
            return False

        if not age.isdigit():
            self.display_age_error_message("Age must be a number.")
            return False

        age = int(age)
        if age < 6:
            self.display_age_error_message("Age is below minimum (6 years old).")
            return False

        if age > 99:
            self.display_age_error_message("Age is above maximum (99 years old).")
            return False

        # Clear any previous error message
        self.display_age_error_message("")
        return True

    def validate_username(self):
        username = self.username_entry.get()

        if not username.strip():
            self.display_username_error_message("Please enter a username.")
            return False

        if not username.isalnum():
            self.display_username_error_message("Invalid characters in username.")
            return False

        if len(username) < 4:
            self.display_username_error_message("Username is too short.")
            return False

        # Clear any previous error message
        self.display_username_error_message("")
        return True

    def validate_password(self):
        password = self.password_entry.get()

        if not password.strip():
            self.display_password_error_message("Please enter a password.")
            return False

        if not any(char.isalnum() for char in password):
            self.display_password_error_message("Password must contain at least one letter or digit.")
            return False

        if not any(char in "!@#$%^&*()_-+={}[]|\:;'<>,.?/~" for char in password):
            self.display_password_error_message("Password must contain at least one special character.")
            return False

        if len(password) < 6:
            self.display_password_error_message("Password is too short. It must be at least 6 characters.")
            return False

        # Clear any previous error message
        self.display_password_error_message("")
        return True

    def register(self):
        if (
            self.validate_name()
            and self.validate_age()
            and self.validate_username()
            and self.validate_password()
        ):
            name = self.name_entry.get()
            age = self.age_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()

            if name and age and username and password:
                # Store the account data (you can replace this with a database)
                self.parent.account_data[username] = {'name': name, 'age': age, 'password': password}
                self.parent.registered = True
                self.parent.btn_register.config(state="disabled")  # Disable the Register button
                self.parent.btn_register.pack_forget()  # Hide the Register button
                self.destroy()
                self.parent.display_info_message("Registration Successful!")
            else:
                self.display_name_error_message("Please enter all required information.")

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.s = ttk.Style()
        self.title("Quiz Time")
        self.geometry("900x300+200+200")

        self.account_data = {}
        self.registered = False

        self.label_1 = tk.Label(self, text="Welcome to the Quiz!", width=30, font=("bold", 15))
        self.label_1.pack(padx=10, pady=30)

        self.btn_1 = ttk.Button(self, text="Start Quiz", command=self.check_registration)
        self.btn_1.pack()

        self.btn_register = ttk.Button(self, text="Register", command=self.create_account_window)
        self.btn_register.pack()

        self.current_user = None  # Store the current user's data

    def display_info_message(self, message):
        messagebox.showinfo("Info", message)

    def create_account_window(self):
        if not self.registered:
            registration_window = RegistrationWindow(self)
        else:
            messagebox.showinfo("Info", "You are already registered!")

    def check_registration(self):
        if self.registered:
            self.label_1.destroy()
            self.btn_1.destroy()
            self.choices()
        else:
            messagebox.showinfo("Info", "Please register before starting the quiz!")

    def choices(self):
        # user's category and difficulty level preference are taken here

        # initializing the score array to store the user's score.
        self.score = [0] * 10
        # play again gets redirected to this window

        # label for category preference
        self.label_1 = tk.Label(
            self, text="Choose a Category", width=20, font=("bold", 10)
        )
        # widget is placed in fixed coordinates using 'place'
        self.label_1.place(x=250, y=50)

        # combobox/drop down menu for category preference
        self.category_choice = ttk.Combobox(
            self,
            values=[
                "Random Category",
                "General Knowledge",
                "Books",
                "Movies",
                "Music",
                "Television",
                "Video Games",
                "Science and Nature",
                "Computers",
                "Mathematics",
                "Mythology",
                "Sports",
                "Geography",
                "History",
                "Animals",
                "Celebrities",
                "Anime and Manga",
                "Cartoons and Animations",
                "Comics",
            ],
        )

        # widget is placed in fixed coordinates
        self.category_choice.place(x=480, y=50)

        # sets the default choice that's initially displayed
        self.category_choice.current(0)

        # label for difficulty preference
        self.label_2 = tk.Label(
            self, text="Choose a Difficulty Level", width=20, font=("bold", 10)
        )
        # widget is placed in fixed coordinates
        self.label_2.place(x=265, y=100)

        # combobox/drop down menu for difficulty preference
        self.difficulty_choice = ttk.Combobox(self, values=["Easy", "Medium", "Hard"])
        # widget is placed in fixed coordinates
        self.difficulty_choice.place(x=480, y=100)

        # sets the default choice that's initially displayed
        self.difficulty_choice.current(1)

        # button to go to next window
        self.btn_1 = ttk.Button(
            self,
            text="Go",
            width=10,
            command=lambda: destroy_widgets() or self.getQuestions(),
        )
        # widget is placed in fixed coordinates
        self.btn_1.place(x=450, y=160, anchor="center")

        def destroy_widgets():
            # user's category choice and difficulty choice are saved
            self.category = self.category_choice.get()
            self.difficulty = self.difficulty_choice.get()

            # all widgets from this window are destroyed
            self.btn_1.destroy()
            self.category_choice.destroy()
            self.difficulty_choice.destroy()
            self.label_1.destroy()
            self.label_2.destroy()

    def getQuestions(self):
        # Chosen Category and Difficulty level are displayed here for confirmation
        # The user is also allowed to go back and change their preference

        # function call to the questions api to retrieve questions
        self.questionsapi(self.category, self.difficulty)

        # displays the category chosen by the user
        self.label_1 = tk.Label(
            self, text="Category: " + self.category, font=("italics", 13)
        )
        # widget is placed in fixed coordinates and centered
        self.label_1.place(x=450, y=50, anchor="center")

        # displays the difficulty level chosen by the user
        self.label_2 = tk.Label(
            self, text="Difficulty: " + self.difficulty, font=("italics", 12)
        )
        # widget is placed in fixed coordinates and centered
        self.label_2.place(x=450, y=100, anchor="center")

        # button redirects the user back to previous window to change their preference
        self.btn_1 = ttk.Button(
            self,
            text="Change Choice",
            command=lambda: destroy_widgets() or self.choices(),
            width=20,
        )
        # widget is placed in fixed coordinates
        self.btn_1.place(x=400, y=150, anchor="e")

        # button to go to next window, to start playing
        self.btn_2 = ttk.Button(
            self,
            text="Next",
            command=lambda: destroy_widgets() or self.printQuestion(0),
            width=20,
        )
        self.btn_2.place(x=500, y=150, anchor="w")

        def destroy_widgets():
            # destroy all widgets from this window
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.label_1.destroy()
            self.label_2.destroy()

    def printQuestion(self, index):
        # function is recursively called to print each question
        # there are a total of 10 questions

        if index < 10:
            # label to display question number
            self.label_1 = ttk.Label(
                self, text="Question " + str(index + 1), font=("bold", 11)
            )
            self.label_1.place(x=450, y=30, anchor="center")

            # a label to display the question text
            # wraplength used to make sure the text doesn't flow out of the screen
            self.label_2 = tk.Label(
                self,
                text=self.questions[index],
                font=("bold", 11),
                wraplength=700,
                justify=tk.CENTER,
            )
            self.label_2.place(x=450, y=70, anchor="center")

            # button to display option 1
            self.option1 = tk.Button(
                self,
                text=self.options[index][0],
                wraplength=200,
                justify=tk.CENTER,
                borderwidth=0.5,
                relief=tk.SOLID,
                activebackground="#ddd",
                command=lambda: destroy_widgets()
                or self.printQuestion(index + 1)
                or self.scoreUpdater(index, 0),
                width=30,
            )
            self.option1.place(x=250, y=130, anchor="center")

            # button to display option 2
            self.option2 = tk.Button(
                self,
                text=self.options[index][1],
                wraplength=200,
                justify=tk.CENTER,
                borderwidth=0.5,
                relief=tk.SOLID,
                activebackground="#ddd",
                command=lambda: destroy_widgets()
                or self.printQuestion(index + 1)
                or self.scoreUpdater(index, 1),
                width=30,
            )
            self.option2.place(x=650, y=130, anchor="center")

            # button to display option 3
            self.option3 = tk.Button(
                self,
                text=self.options[index][2],
                wraplength=200,
                justify=tk.CENTER,
                borderwidth=0.5,
                relief=tk.SOLID,
                activebackground="#ddd",
                command=lambda: destroy_widgets()
                or self.printQuestion(index + 1)
                or self.scoreUpdater(index, 2),
                width=30,
            )
            self.option3.place(x=250, y=180, anchor="center")

            # button to display option 4
            self.option4 = tk.Button(
                self,
                text=self.options[index][3],
                wraplength=200,
                justify=tk.CENTER,
                borderwidth=0.5,
                relief=tk.SOLID,
                activebackground="#ddd",
                command=lambda: destroy_widgets()
                or self.printQuestion(index + 1)
                or self.scoreUpdater(index, 3),
                width=30,
            )
            self.option4.place(x=650, y=180, anchor="center")

            if index > 0:
                # button to navigate to previous question
                # appears from the second question onwards
                self.btn_2 = ttk.Button(
                    self,
                    text="Go to Previous Question",
                    command=lambda: destroy_widgets() or self.printQuestion(index - 1),
                )
                self.btn_2.place(x=70, y=220)

        else:
            # once 10 questions have been printed we move onto here
            # a buffer window before we print the score

            # a label to notify the user that the quiz is done
            self.label_1 = tk.Label(
                self, text="Great Work. Hope you had fun!", font=("bold", 12)
            )
            # widget is placed in fixed coordinates
            self.label_1.place(x=450, y=70, anchor="center")

            # button to navigate to the next page to view score
            self.btn_1 = ttk.Button(
                self,
                text="Get Score",
                command=lambda: self.label_1.destroy()
                or self.btn_1.destroy()
                or self.getScore(),
                width=15,
            )
            # widget is placed in fixed coordinates
            self.btn_1.place(x=450, y=130, anchor="center")

        def destroy_widgets():
            # destroy all widgets from this window
            self.label_1.destroy()
            self.label_2.destroy()
            self.option1.destroy()
            self.option2.destroy()
            self.option3.destroy()
            self.option4.destroy()
            if index > 0:
                self.btn_2.destroy()

    def scoreUpdater(self, question, option):
        # function is called every time the user answers a question

        # the users answer is compared to the right answer to the question
        # the score array is updated accordingly
        if self.options[question][option] == self.correct_answers[question]:
            self.score[question] = 1
        else:
            self.score[question] = 0

    def getScore(self):
        # window to display score

        # save the user's score as an integer - previously an array
        # count() is used to count the number of correctly answered questions
        self.score = self.score.count(1)

        # following if conditions are targeted for a certain score range
        if self.score <= 4:
            self.label_1 = tk.Label(
                self, text="Better Luck Next Time!", font=("bold", 12)
            )
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12)
            )

        elif self.score == 5:
            self.label_1 = tk.Label(self, text="Not Bad!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12)
            )

        elif self.score < 10 and self.score > 5:
            self.label_1 = tk.Label(self, text="Good Job!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12)
            )

        elif self.score == 10:
            self.label_1 = tk.Label(self, text="Awesome!", font=("bold", 12))
            self.label_2 = tk.Label(
                self, text="Your Score is: " + str(self.score), font=("bold", 12)
            )

        # labels are assigned definite coordinates on the window
        self.label_1.place(x=450, y=70, anchor="center")
        self.label_2.place(x=450, y=120, anchor="center")

        # Button to navigate the user to the quiz preferences window to play again
        self.btn_1 = ttk.Button(
            self, text="Play Again", command=lambda: destroy_widgets() or self.choices()
        )
        self.btn_1.place(x=400, y=170, anchor="e")

        # button to quit
        self.btn_2 = ttk.Button(
            self, text="Quit", command=lambda: destroy_widgets() or self.destroy()
        )
        self.btn_2.place(x=500, y=170, anchor="w")

        def destroy_widgets():
            # destroys all widgets from this window
            self.label_1.destroy()
            self.label_2.destroy()
            self.btn_1.destroy()
            self.btn_2.destroy()

    def questionsapi(self, category, difficulty):
        # questions for the quiz are retrieved using an api
        # api link https://opentdb.com/api_config.php

        # category to ID mapping is made here
        # the full list of category to id mapping can be retrieved here -> https://opentdb.com/api_category.php
        categoryMappings = {
            "General Knowledge": 9,
            "Books": 10,
            "Movies": 11,
            "Music": 12,
            "Television": 14,
            "Video Games": 15,
            "Science and Nature": 17,
            "Computers": 18,
            "Mathematics": 19,
            "Mythology": 20,
            "Sports": 21,
            "Geography": 22,
            "History": 23,
            "Animals": 27,
            "Celebrities": 26,
            "Anime and Manga": 31,
            "Cartoons and Animations": 32,
            "Comics": 29,
        }

        # random category is generated in the below if condition
        if category == "Random Category":
            self.category = random.choice(list(categoryMappings.keys()))
        # category is obtained through the category mappings
        category_id = categoryMappings[self.category]

        # url to make api call from category and difficulty preferences is generated
        url = (
            "https://opentdb.com/api.php?amount=10&category="
            + str(category_id)
            + "&difficulty="
            + self.difficulty.lower()
            + "&type=multiple&encode=url3986"
        )

        # json response is saved using the request module of Python
        with request.urlopen(url) as response:
            source = response.read()
            data = json.loads(source)

        # questions, incorrect answers and the correct answers are extracted fromt he response data
        # urllib.parse is used to decode the response data (%20..etc)
        self.questions = [
            urllib.parse.unquote(q["question"], encoding="utf-8", errors="replace")
            for q in data["results"]
        ]
        self.correct_answers = [
            urllib.parse.unquote(
                q["correct_answer"], encoding="utf-8", errors="replace"
            )
            for q in data["results"]
        ]

        incorrect_options = [q["incorrect_answers"] for q in data["results"]]

        # loops through each question's incorrect answers and appends the correct answer to it
        # all 4 options are shuffled usind 'random' module's shuffle
        for i in range(len(incorrect_options)):
            for j in range(len(incorrect_options[i])):
                incorrect_options[i][j] = urllib.parse.unquote(
                    incorrect_options[i][j], encoding="utf-8", errors="replace"
                )
            incorrect_options[i].append(self.correct_answers[i])
            random.shuffle(incorrect_options[i])

        self.options = []
        # the
        for i in range(len(incorrect_options)):
            self.options.append(incorrect_options[i])

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
