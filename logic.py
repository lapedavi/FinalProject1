from gui import *

class Logic(Gui):
    def __init__(self, window) -> None:
        super().__init__(window)

        self.__john_votes = 0
        self.__jane_votes = 0

        self.exit_button.config(command=self.select_exit)
        self.vote_button.config(command=self.open_candidate_menu)
        self.cast_button.config(command=self.cast_vote)


    def select_exit(self) -> None:
        """Closes both vote and main screens and displays votes per candidate and total votes"""
        self.vote_frame.pack_forget()
        self.main_frame.pack_forget()
        self.final_label.config(text=f'John - {self.__john_votes}, Jane - {self.__jane_votes}, Total - {self.__john_votes + self.__jane_votes}')
        self.final_label.pack(pady=20)

    def cast_vote(self) -> None:
        """Add vote to selected candidate, if vote was not provided return an error message.
         If vote is successful return to menu"""
        status = self.radio_answer.get()
        if status == 1:
            self.__john_votes += 1
            self.vote_result_label.config(text='Voted John')
        elif status == 2:
            self.__jane_votes += 1
            self.vote_result_label.config(text='Voted Jane')
        else:
            self.error_label.config(text='Please select the candidate to vote for')
            return

        self.radio_answer.set(0)
        self.open_main_menu()

    def open_candidate_menu(self) -> None:
        """Closes main menu and opens vote form"""
        self.main_frame.pack_forget()
        self.vote_frame.pack()

    def open_main_menu(self) -> None:
        """Closes vote form and opens main menu"""
        self.vote_frame.pack_forget()
        self.main_frame.pack()
