import tkinter as tk
from tkinter import messagebox


class TrisGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tris Game")
        self.root.geometry("340x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#222")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#222")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=("Arial", 28, "bold"), width=4, height=2,
                                bg="#333", fg="#eee", activebackground="#444", activeforeground="#fff",
                                borderwidth=0, highlightthickness=0,
                                command=lambda x=i, y=j: self.handle_click(x, y))
                btn.grid(row=i, column=j, padx=6, pady=6)
                self.buttons[i][j] = btn

    def handle_click(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            self.buttons[x][y]["text"] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
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
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TrisGame(root)
    root.mainloop()
