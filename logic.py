from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''The initial setup for the GUI

        There are 2 groups of 2 buttons layered on top of each other.
        Even though VOTE and EXIT are layered on them, I felt it was
        necessary to hide vote_jake and vote_jane.
        '''
        super().__init__()
        self.setupUi(self)
        self.button_vote_jake.hide()
        self.button_vote_jake.clicked.connect(lambda: self.vote_jake())
        self.button_vote_jane.hide()
        self.button_vote_jane.clicked.connect(lambda: self.vote_jane())
        self.button_vote.clicked.connect(lambda: self.vote())
        self.button_exit.clicked.connect(lambda: self.exit())

    def vote(self):
        '''The vote button moves on to the Candidate Menu

        Clicking the vote button hides VOTE and EXIT,
        revealing the option to vote for Jake or Jane.
        It also changes the output and header text.
        '''
        self.button_vote.hide()
        self.button_exit.hide()
        self.button_vote_jake.show()
        self.button_vote_jane.show()
        self.label_header.setText(f'CANDIDATE MENU')
        self.label_output.setText(f'Please select a candidate')
    def vote_jake(self):
        '''Clicking Jake adds 1 to his count and 1 to the total vote count.

        vote_jake looks for his name and adds 1 vote to his row
        and the total vote row in the csv file.
        The menu will revert back to the Vote Menu, hiding the option
        to vote for a candidate until VOTE is selected again.
        '''
        with open('votes.csv') as readvotes:
            reader = csv.reader(readvotes.readlines())
            with open('votes.csv', 'w', newline='') as writevotes:
                writer = csv.writer(writevotes)
                for row in reader:
                    if row[0] == 'Jake' or row[0] == 'Total':
                        writer.writerow([row[0],str(int(row[1])+1)])
                        self.label_output.setText(f'Voted for Jake!')
                        self.button_vote.show()
                        self.button_exit.show()
                        self.button_vote_jake.hide()
                        self.button_vote_jane.hide()
                        self.label_header.setText(f'VOTE MENU')
                    else:
                        writer.writerow(row)
    def vote_jane(self):
        '''This will achieve the same effect as vote_jake, except the vote is added to Jane.'''
        with open('votes.csv') as readvotes:
            reader = csv.reader(readvotes.readlines())
            with open('votes.csv', 'w', newline='') as writevotes:
                writer = csv.writer(writevotes)
                for row in reader:
                    if row[0] == 'Jane' or row[0] == 'Total':
                        writer.writerow([row[0], str(int(row[1]) + 1)])
                        self.label_output.setText(f'Voted for Jane!')
                        self.button_vote.show()
                        self.button_exit.show()
                        self.button_vote_jake.hide()
                        self.button_vote_jane.hide()
                        self.label_header.setText(f'VOTE MENU')
                    else:
                        writer.writerow(row)
    def exit(self):
        '''This will end function of the program until you open the app again.

        All lines are read and saved in a list in a formatted order,
        the output text is changed to this and the header text is also changed.
        '''
        with open('votes.csv', newline='') as readvotes:
            reader = csv.reader(readvotes)
            data: list = [f'{name} - {votes}' for name,votes in reader]
            self.label_output.setText(', '.join(data))
            self.label_header.setText(f'Thanks for voting!')