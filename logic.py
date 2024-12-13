import os.path

from gui import *

class Logic(Gui):
    FILE_NAME = 'data.csv'

    def __init__(self, window) -> None:
        """Loads votes from data file or creates file if it does not exist and binds button functions"""
        super().__init__(window)

        self.__john_votes = 0
        self.__jane_votes = 0

        if os.path.isfile(Logic.FILE_NAME):
            data_file = open(Logic.FILE_NAME,'r')
            for line in data_file:
                split_data = line.split(',')
                if split_data[1] == '1\n':
                    self.__john_votes += 1
                else:
                    self.__jane_votes += 1
        else:
            data_file = open(Logic.FILE_NAME, 'w')

        data_file.close()

        self.vote_button.config(command=self.cast_vote)
        self.view_button.config(command=self.select_view)

    def select_view(self) -> None:
        """Close main frame and loads results frame"""
        self.main_frame.pack_forget()
        self.result_label.config(text=f'John - {self.__john_votes}, Jane - {self.__jane_votes}, Total - {self.__john_votes + self.__jane_votes}')
        self.result_frame.pack()

    def cast_vote(self) -> None:
        """Check the id is a valid 6-digit number and if they have previously voted,
        if not save their valid vote to data file"""

        entered_id = self.id_entry.get().strip()

        if entered_id.isalpha() or len(entered_id) != 6:
            self.set_error_response('Please enter valid 6 digit numerical Id')
            return

        data_file = open(Logic.FILE_NAME, 'r')

        for line in data_file:
            split_line = line.split(',')
            if split_line[0] == entered_id:
                self.set_error_response('Already Voted')
                return
        data_file.close()

        status = self.radio_answer.get()
        if status == 1:
            self.__john_votes += 1
            self.set_success_response('Voted John')
        elif status == 2:
            self.__jane_votes += 1
            self.set_success_response('Voted Jane')
        else:
            self.set_error_response('Please select the candidate to vote for')
            return

        data_file = open(Logic.FILE_NAME, 'a')
        data_file.write(f'{entered_id},{status}\n')
        data_file.close()

        self.id_entry.delete(0, END)
        self.radio_answer.set(0)

    def set_error_response(self, error:str) -> None:
        """Set error label to red error"""
        self.error_label.config(text=error, fg='red')

    def set_success_response(self, response:str) -> None:
        """Set error label to green response"""
        self.error_label.config(text=response, fg='green')