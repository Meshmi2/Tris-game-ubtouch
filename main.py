import sys
import os
import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class TrisGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tris Game")
        self.setFixedSize(300, 300)
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.init_ui()

    def init_ui(self):
        self.grid = QGridLayout()
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.setFixedSize(80, 80)
                btn.setStyleSheet("font-size: 32px;")
                btn.clicked.connect(lambda _, x=i, y=j: self.handle_click(x, y))
                self.grid.addWidget(btn, i, j)
        self.setLayout(self.grid)

    def handle_click(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            self.buttons[x][y].setText(self.current_player)
            if self.check_win(self.current_player):
                QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                QMessageBox.information(self, "Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
        # Check rows, columns, diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
        self.current_player = "X"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TrisGame()
    game.show()
    sys.exit(app.exec_())
