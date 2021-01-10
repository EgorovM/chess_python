import tkinter as tk 

from chess import ChessDesk


class DeskFrame(tk.Frame):
    BOARD = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [+1, +1, +1, +1, +1, +1, +1, +1],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, master):
        super().__init__()
        self.init_ui(master)

    def init_ui(self, master):
        self.master = master
        self._draw_desk()
        self.pack()

    def _draw_desk(self):
        for i in range(len(self.BOARD)):
            for j in range(len(self.BOARD[i])):
                l = tk.Label(self, text=self.BOARD[i][j])
                l.grid(row=i, column=j)


class GUI:
    def __init__(self, window_size=('480', '480')):
        self._chessdesk = ChessDesk()
        self._screen = tk.Tk()
        self._screen.geometry('x'.join(window_size))
        self._desk_frame = DeskFrame(self._screen)

    def run(self):
        self._screen.mainloop()

if __name__ == "__main__":
     gui = GUI()
     gui.run()