import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)], buttons[row][0]["text"])
            return buttons[row][0]["text"]
    
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            highlight_winner([(0, col), (1, col), (2, col)], buttons[0][col]["text"])
            return buttons[0][col]["text"]
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)], buttons[0][0]["text"])
        return buttons[0][0]["text"]
    
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)], buttons[0][2]["text"])
        return buttons[0][2]["text"]
    
    return None

def highlight_winner(cells, winner):
    for row, col in cells:
        buttons[row][col].config(bg="green", fg="white", text=f"win🥳")

def is_full():
    return all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col].config(bg="lightblue", fg="darkblue")
        animate_button(buttons[row][col])
        
        winner = check_winner()
        if winner:
            show_winner_window(winner)
            reset_game()
        elif is_full():
            messagebox.showinfo("Game Over", "It's a tie! 😞")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def show_winner_window(winner):
    winner_window = tk.Toplevel(root)
    winner_window.title("Game Over")
    winner_window.geometry("400x400")
    winner_window.configure(bg="black")
    
    svg_label = tk.Label(winner_window, text="🎉🥳", font=("Arial", 30), fg="gold", bg="black")
    svg_label.pack(pady=10)

    winner_label = tk.Label(winner_window, text=f"Player {winner} ", font=("Arial", 20), fg="white", bg="black")
    winner_label.pack(pady=10)
    
    svg_image = tk.PhotoImage(file="path_to_your_svg_image.svg")  
    svg_image_label = tk.Label(winner_window, image=svg_image, bg="black")
    svg_image_label.image = svg_image 
    svg_image_label.pack(pady=20)
    
    close_button = tk.Button(winner_window, text="Close", command=winner_window.destroy, font=("Arial", 14), bg="red", fg="white")
    close_button.pack(pady=20)

def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(bg="white", fg="black")

def animate_button(button):
    button.config(font=("Arial", 28))
    button.after(200, lambda: button.config(font=("Arial", 24)))

def create_ui():
    global root, buttons
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.configure(bg="black")
    
    frame = tk.Frame(root, bg="black")
    frame.pack(pady=20)
    
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2, bg="white", fg="black", 
                               relief="ridge", command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col, padx=5, pady=5)
            button_row.append(button)
        buttons.append(button_row)
    
    reset_button = tk.Button(root, text="Reset Game", font=("Arial", 16), command=reset_game, bg="red", fg="white")
    reset_button.pack(pady=10)
    
    root.mainloop()

current_player = "X"
buttons = []
create_ui()
