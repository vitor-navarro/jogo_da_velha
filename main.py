from tkinter import *
from tkinter import messagebox

jogadas = 0

def callback(r, c):
    b[r][c].config(text=turn, state='disabled')

    global jogadas

    jogadas += 1

    if checa_vencedor(r, c):
        messagebox.showinfo("Vencedor", f"{turn} venceu!")
        reset_game()
    elif jogadas == 9:
        messagebox.showinfo("Velha", f"Ninguém venceu")
        reset_game()
    else:
        muda_x_o()

def checa_vencedor(row, col):
    if all(b[row][i].cget("text") == turn for i in range(3)):
        return True

    if all(b[i][col].cget("text") == turn for i in range(3)):
        return True

    if row == col and all(b[i][i].cget("text") == turn for i in range(3)):
        return True

    if row + col == 2 and all(b[i][2 - i].cget("text") == turn for i in range(3)):
        return True

    return False

def reset_game():
    global turn
    turn = 'X'
    for r in range(3):
        for c in range(3):
            b[r][c].config(text=" ", state='normal')

def muda_x_o():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

turn = 'X'

root = Tk()
root.title("Jogo da Velha")

b = [[0] * 3 for i in range(3)]
for r in range(3):
    for c in range(3):
        b[r][c] = Button(root, text=" ", font=("Helvetica", 32), width=2, height=1,
                           command=lambda row=r, col=c: callback(row, col))
        b[r][c].grid(row=r, column=c)

root.mainloop()