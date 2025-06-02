import tkinter as tk
from triviagame import TriviaGameFrame

def main():
    # builds main frame
    # sets title, size
    root = tk.Tk()
    root.title("The Office Trivia Game")
    root.geometry("450x200")

    main_frame = tk.Frame(root, width=450, height=200)
    main_frame.pack_propagate(False)        # dimensions won't change with widgets
    main_frame.pack(fill='both', expand=True)

    # calls triviagame.py
    game = TriviaGameFrame(main_frame)
    game.file_handing()
    root.mainloop()         # displays frame

if __name__ == "__main__":
    main()