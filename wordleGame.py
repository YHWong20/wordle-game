import random
import tkinter as tk
import wordleConfig as wdgame
from tkinter import messagebox


def txt_parser(filename):
    result = []
    f = open(filename, "r")
    for line in f:
        result.append(line[0:5])
    return result

word_list = txt_parser(r"C:\Users\Gamer\Documents\Python Files\wordle\5_letter_words.txt")
new_game = wdgame.Wordle(random.choice(word_list))

root = tk.Tk()

root.title("Wordle Game")
root.configure(background= "#454545")
# root.geometry("300x400")


def player_guess():
    guess = entry_box.get().upper() # Guessed word converted to uppercase
    
    if len(guess) != len(new_game.word): # Entered word is of incorrect length (std length is 5)
        messagebox.showinfo("Try Again!", "Entry is not of the correct length!")
        entry_box.delete(0, tk.END)
        return

    new_game.guess_made()
    show_guessed_word()
    attempts_left_upd()

    if guess == new_game.word:
        msg_box.config(text= "Game Over. You Win!")
        submit_button.config(text= "You Win!", command= game_win)
    elif new_game.attempts_left <= 0:
        msg_box.config(text= f"Game Over. The word was {new_game.word}.")
        submit_button.config(text= "Game Over!", command= game_lose)
        
    entry_box.delete(0, tk.END)


def game_lose():
    messagebox.showinfo("Game Over!", "Game Over!")

def game_win():
    messagebox.showinfo("You Win!", f"Your Score Is {1 + new_game.attempts_left}.")
    

def attempts_left_upd(): # Updates attempts left
    msg_box.config(text= f"You have {new_game.attempts_left} attempts left.")


def show_guessed_word():
    guessed_word = entry_box.get().upper()
    position_dict = new_game.position_check(guessed_word, new_game.word)

    for i, chr in enumerate(guessed_word):
        letter_label = tk.Label(root, text= chr)
        letter_label.grid(row= 5 - new_game.attempts_left, columnspan= 5, column= i, \
            padx= 10, pady= 10, ipadx= 10, ipady= 10)

        if (position_dict[chr] == 2 and chr == new_game.word[i]) or (position_dict[chr] == 1 and chr == new_game.word[i]):
            letter_label.config(bg= "#2e9800", fg= "white")
        elif position_dict[chr] == 1 or (position_dict[chr] == 2 and chr != new_game.word[i]):
            letter_label.config(bg= "#FFC300", fg= "white")
        else:
            letter_label.config(bg= "#b2b2b2", fg= "white")


entry_box = tk.Entry(root, width= "20")
entry_box.grid(row= 99, columnspan= 5, column= 2, padx= 10, pady= 10, ipadx= 20)

submit_button = tk.Button(root, text= "Enter", width= "10", command= player_guess, font= ("Helvetica, 10"))
submit_button.grid(row= 100, columnspan= 5, column= 2, padx= 10)

msg_box = tk.Label(root, text= f"You have {new_game.attempts_left} attempts left.", font= ("Helvetica", 10))
msg_box.grid(row= 0, columnspan= 5, column= 2, ipadx= 35)


root.mainloop()





# -- TO-DO --
# ** figure out way to adjust dimensions properly, make interface nicer and less overlappy **
# redo implementation for position check to make labelling easier
# HARD - retry system