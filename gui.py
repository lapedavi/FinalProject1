from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        # Main Menu
        self.main_frame = Frame(self.window)

        self.vote_menu_label = Label(self.main_frame, text="VOTING APPLICATION", font=("Helvetica", 10))

        self.vote_menu_label.pack(pady=10)

        self.id_frame = Frame(self.main_frame)
        self.id_label = Label(self.id_frame, text="ID", font=("Helvetica", 10))
        self.id_entry = Entry(self.id_frame)

        self.id_label.pack(side=LEFT)
        self.id_entry.pack(side=LEFT, padx=5)
        self.id_frame.pack()

        self.candidate_menu_label = Label(self.main_frame, text="CANDIDATE MENU", font=("Helvetica", 10))

        self.candidate_menu_label.pack(pady=10)

        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.john_ratio = Radiobutton(self.main_frame, text="John", variable=self.radio_answer, value=1)
        self.jane_ratio = Radiobutton(self.main_frame, text="Jane", variable=self.radio_answer, value=2)

        self.john_ratio.pack()
        self.jane_ratio.pack()

        self.vote_button = Button(self.main_frame, text='SUBMIT VOTE')
        self.view_button = Button(self.main_frame, text='VIEW VOTES')

        self.vote_button.pack(pady=10)
        self.view_button.pack()

        self.error_label = Label(self.main_frame, font=("Helvetica", 10))

        self.error_label.pack(pady=10)

        self.main_frame.pack()

        # Final Frame
        self.result_frame = Frame(self.window)

        self.result_label = Label(self.result_frame, font=("Helvetica", 10))
        self.result_label.pack(pady=10)





