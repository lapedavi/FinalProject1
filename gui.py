from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        self.main_frame = Frame(self.window)

        self.vote_menu_label = Label(self.main_frame, text="VOTE MENU", font=("Helvetica", 10))
        self.vote_button = Button(self.main_frame, text='Vote')
        self.exit_button = Button(self.main_frame, text='Exit')
        self.vote_menu_label.pack(pady=5)
        self.vote_button.pack(pady=10)
        self.exit_button.pack()

        self.vote_result_label  = Label(self.main_frame, font=("Helvetica", 10))
        self.vote_result_label.pack(pady=10)

        self.main_frame.pack()

        self.vote_frame = Frame(self.window)
        self.candidate_menu_label = Label(self.vote_frame, text="CANDIDATE MENU", font=("Helvetica", 10))
        self.candidate_menu_label.pack(pady=10)

        self.candidate_frame = Frame(self.vote_frame)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.john_ratio = Radiobutton(self.candidate_frame, text="John", variable=self.radio_answer, value=1)
        self.jane_ratio = Radiobutton(self.candidate_frame, text="Jane", variable=self.radio_answer, value=2)

        self.john_ratio.pack(side='left')
        self.jane_ratio.pack(side='left')
        self.candidate_frame.pack()

        self.cast_button = Button(self.vote_frame, text='Cast Vote')
        self.cast_button.pack(pady=15)

        self.error_label = Label(self.vote_frame, font=("Helvetica", 10))
        self.error_label.pack(pady=20)

        self.final_label = Label(self.window, font=("Helvetica", 10))





