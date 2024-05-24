import random as rand
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Buscaminas")

def create_grid(n):
    return [[1 if rand.random() < 0.2 else 0 for _ in range(n)] for _ in range(n)]

grid = create_grid(10)
root.geometry(f"{len(grid)*50}x{len(grid)*40}")

tk.Label(root, text="El Buscaminas\n", font=("Arial", 16)).pack()

frame = tk.Frame(root)
frame.pack()

def print_grid(grid):
    buttons = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            button = tk.Button(frame, text=" ", bg="white", width=2, height=1)
            button.grid(row=i, column=j)
            buttons.append(button)
    
    def reveal_cell(i, j):
        if grid[i][j] == 0:
            count = sum(grid[x][y] for x in range(max(0, i-1), min(i+2, len(grid))) for y in range(max(0, j-1), min(j+2, len(grid))))
            buttons[i * len(grid) + j].config(text=str(count), bg="lightgray")
        else:
            buttons[i * len(grid) + j].config(text="*", bg="red")
            messagebox.showinfo("Game Over", "Perdiste")
            root.destroy()
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            buttons[i * len(grid) + j].config(command=lambda i=i, j=j: reveal_cell(i, j))

print_grid(grid)

root.mainloop()
