import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget, QMessageBox


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tic Tac Toe")

        # create a central widget and a grid layout
        central_widget = QWidget()
        grid_layout = QGridLayout()

        # create buttons for each square on the board and add them to the grid layout
        self.buttons = {}
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.clicked.connect(lambda _, row=i, col=j: self.handle_button_click(row, col))
                self.buttons[(i, j)] = button
                grid_layout.addWidget(button, i, j)

        # create a status label and add it to the grid layout
        self.status_label = QLabel()
        grid_layout.addWidget(self.status_label, 3, 0, 1, 3)

        # set the central widget and the grid layout
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

        # show the main window
        self.show()

    def handle_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[(row, col)].setText(self.current_player)
            winner = self.check_winner()
            if winner:
                self.show_game_over_message(f"{winner} wins!")
            elif self.check_tie():
                self.show_game_over_message("It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f"{self.current_player}'s turn")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def check_tie(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def show_game_over_message(self, message):
        QMessageBox.about(self, "Game Over", message)
        self.reset_board()

    def reset_board(self):
        self.board = [[' ']*3 for _ in range(3)]
        for button in self.buttons.values():
            button.setText('')
        self.current_player = 'X'
        self.status_label.setText(f"{self.current_player}'s turn")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tictactoe = TicTacToe()
    sys.exit(app.exec_())



