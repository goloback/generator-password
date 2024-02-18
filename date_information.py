from tkinter import *
class Date_information():
    def __init__(self, canvas):
        self.amount_numbers = 0
        self.amount_letters = 0
        self.amount_LETTERS = 0
        self.amount_sympols = 0
        self.error_text = None
        self.canvas = canvas
    def print_information(self):
        print(self.amount_numbers, self.amount_letters, self.amount_LETTERS, self.amount_sympols)
    def get_sum(self):
        return self.amount_numbers + self.amount_letters + self.amount_LETTERS + self.amount_sympols

    def delete_error(self):
        if self.error_text is not None:
            self.error_text.destroy()
            self.error_text = None

    def create_error(self):
        if self.error_text is None:
            self.error_text = Label(self.canvas, text='write correct password length', bg='#9f6fde', fg='red',
                              font=('Comic Sans MS', 15))
            self.error_text.place(x=400, y=300)
