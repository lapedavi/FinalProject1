import os.path

from gui import *

class Logic(Gui):
    FILE_NAME = 'data.csv'

    def __init__(self, window) -> None:
        super().__init__(window)

        self.__john_votes = 0
        self.__jane_votes = 0

        self.exit_button.config(command=self.select_exit)
        self.vote_button.config(command=self.open_candidate_menu)
        self.cast_button.config(command=self.cast_vote)
        self.load_button.config(command=self.load_votes)
        self.save_button.config(command=self.save_votes)


    def select_exit(self) -> None:
        """Closes both vote and main screens and displays votes per candidate and total votes"""
        self.vote_frame.pack_forget()
        self.main_frame.pack_forget()
        self.result_label.config(text=f'John - {self.__john_votes}, Jane - {self.__jane_votes}, Total - {self.__john_votes + self.__jane_votes}')
        self.result_frame.pack()

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

    def load_votes(self) -> None:
        """Read data file to load the previously saved votes. If data file does not exist show an error"""
        if os.path.isfile(Logic.FILE_NAME):
            data_file = open(Logic.FILE_NAME,'r')
        else:
            self.vote_result_label.config(text='File does not exist')
            return

        line_data = data_file.readline()
        data_file.close()

        split_data = line_data.split(',')
        self.__john_votes = int(split_data[0])
        self.__jane_votes = int(split_data[1])
        self.vote_result_label.config(text='Read data successfully')

    def save_votes(self) -> None:
        """Write current vote counts to data file"""
        data_file = open(Logic.FILE_NAME,'w')
        data_file.write(f'{self.__john_votes},{self.__jane_votes}')
        data_file.close()
        self.save_button.pack_forget()
        self.result_label.config(text=f'Votes saved successfully')