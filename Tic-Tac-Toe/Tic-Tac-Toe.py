import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        
        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        self.player1_name.set("Jugador 1")
        self.player2_name.set("Jugador 2")
        
        self.current_player = "X"
        self.board = [""] * 9
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Nombre Jugador 1:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.player1_name).grid(row=0, column=1)
        
        tk.Label(self.root, text="Nombre Jugador 2:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.player2_name).grid(row=1, column=1)
        
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2, 
                               command=lambda i=i: self.make_move(i))
            button.grid(row=2 + i // 3, column=i % 3)
            self.buttons.append(button)
        
        self.reset_button = tk.Button(self.root, text="Reiniciar", command=self.reset_game)
        self.reset_button.grid(row=5, column=1, pady=10)
    
    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, 
                                       fg="red" if self.current_player == "X" else "blue")
            if self.check_winner():
                winner = self.player1_name.get() if self.current_player == "X" else self.player2_name.get()
                messagebox.showinfo("Fin del juego", f"¡{winner} ha ganado!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False
    
    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
