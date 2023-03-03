from tkinter import *
import tkinter.messagebox as messagebox

class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("300x150")

        self.label_username = Label(self.master, text="Username:")
        self.label_username.pack()

        self.entry_username = Entry(self.master)
        self.entry_username.pack()

        self.label_password = Label(self.master, text="Password:")
        self.label_password.pack()

        self.entry_password = Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_login = Button(self.master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()
        if self.username == "hari" and self.password == "password1234":
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(self.username))
            self.master.destroy()
            root = Tk()
            feedback_system = FeedbackSystem(root)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password. Please try again.")
            self.entry_password.delete(0, END)

class FeedbackSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Feedback System")
        self.master.geometry("500x600")

        self.label_name = Label(self.master, text="Name:")
        self.label_name.pack()

        self.entry_name = Entry(self.master)
        self.entry_name.pack()

        self.label_feedback = Label(self.master, text="Feedback Ratings:")
        self.label_feedback.pack()

        self.feedback_ratings = {}
        for subject in ["RL", "DEV", "WT", "NOSQL", "CS", "LSS"]:
            subject_label = Label(self.master, text=subject)
            subject_label.pack()
            subject_rating = Scale(self.master, from_=1, to=10, orient=HORIZONTAL, length=200)
            subject_rating.pack()
            subject_rating.set(1)  # Set initial value to 1
            self.feedback_ratings[subject] = subject_rating

        self.label_comment = Label(self.master, text="Comments:")
        self.label_comment.pack()

        self.text_comment = Text(self.master, height=5)
        self.text_comment.pack()

        self.button_submit = Button(self.master, text="Submit", command=self.submit_feedback)
        self.button_submit.pack()

    def submit_feedback(self):
        self.name = self.entry_name.get()
        self.ratings = self.feedback_ratings
        self.comment = self.text_comment.get("1.0", "end-1c")
        self.entry_name.delete(0, END)
        self.text_comment.delete("1.0", "end")
        feedback_text = ""
        for subject, rating in self.ratings.items():
            feedback_text += "{}: {}\n".format(subject, rating.get())
            rating.set(1)  # Set value back to 1 after submission
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback, {}! Your feedback ratings were:\n{}\nYour comment was: {}".format(self.name, feedback_text, self.comment))

root = Tk()
login_system = LoginSystem(root)
root.mainloop()