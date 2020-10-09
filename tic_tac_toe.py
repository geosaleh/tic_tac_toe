# Follow Us On Twitter @PY4ALL

from tkinter import *
from tkinter import ttk
import numpy as np

class MainWindow:

    def __init__(self, master):

        master.title('Tic-Tac-Toe Game')
        master.resizable(False, False)
        master.configure(background = 'white')


        self.turn = 'x'
        self.w = Canvas(master, width=600, height=600, bg='white')
        self.w.pack()

        self.frame_control = ttk.Frame()
        self.frame_control.pack()


        ttk.Button(master, text = 'Clear',
                   command = self.clear).pack()

        self.w.create_line(0, 200, 600, 200, fill="red")
        self.w.create_line(0, 400, 600, 400, fill="red")

        self.w.create_line(200, 0, 200, 600, fill="red")
        self.w.create_line(400, 0, 400, 600, fill="red")

        self.w.bind("<Button 1>",self.get_loc)

        self.draw_loc = [[(35,35),(35,235),(35,435)],
                         [(235,35),(235,235),(235,435)],
                         [(435,35),(435,235),(435,435)]]
        self.game = np.array([[0,0,0],
                              [0,0,0],
                              [0,0,0]])
        self.draw_loc2 = [[(0,0,200,200),(200,0,400,200),(400,0,600,200)],
                    [(0,200,200,400),(200,200,400,400),(400,200,600,400)],
                    [(0,400,200,600),(200,400,400,600),(400,400,600,600)]]

        self.x = PhotoImage(file="x.png")
        #self.x = self.x.subsample(2)
        self.o = PhotoImage(file="o.png")
        #self.o = self.o.subsample(2)

        self.game_end = False


        
    def get_loc(self, event):
        if not self.game[event.x//200][event.y//200] and not self.game_end:
            if self.turn == 'x':
                self.w.create_image(self.draw_loc[event.x//200][event.y//200], anchor=NW, image=self.x, tags=('delete',))
                self.turn = 'o'
                self.game[event.x//200][event.y//200] = 1
            else:
                self.w.create_image(self.draw_loc[event.x//200][event.y//200], anchor=NW, image=self.o, tags=('delete',))
                self.turn = 'x'
                self.game[event.x//200][event.y//200] = -1
        self.game_end = self.check()

    def check(self):
        for count, row in enumerate(self.game.sum(0)):
            if row == 3:
                self.w.create_line(0, 100+(count*200), 600, 100+(count*200), fill="blue", tags=('delete',))
                self.x_won()
                return True
            elif row == -3:
                self.w.create_line(0, 100+(count*200), 600, 100+(count*200), fill="blue", tags=('delete',))
                self.o_won()
                return True
                
        for count, col in enumerate(self.game.sum(1)):
            if col == 3:
                self.w.create_line(100+(count*200), 0, 100+(count*200), 600, fill="blue", tags=('delete',))
                self.x_won()
                return True
            elif col == -3:
                self.w.create_line(100+(count*200), 0, 100+(count*200), 600, fill="blue", tags=('delete',))
                self.o_won()
                return True
        if sum(self.game.diagonal()) == 3:
            self.w.create_line(0, 0, 600, 600, fill="blue", tags=('delete',))
            self.x_won()
            return True
        elif sum(self.game.diagonal()) == -3:
            self.w.create_line(0, 0, 600, 600, fill="blue", tags=('delete',))
            self.o_won()
            return True

        if sum(np.fliplr(self.game).diagonal()) == 3:
            self.w.create_line(0, 600, 600, 0, fill="blue", tags=('delete',))
            self.x_won()
            return True
        elif sum(np.fliplr(self.game).diagonal()) == -3:
            self.w.create_line(0, 600, 600, 0, fill="blue", tags=('delete',))
            self.o_won()
            return True

        
        
        if len(np.where(self.game == 0)[0])==0:
            self.w.create_text(300,300,font='Times 40 bold',text='Tie!', tags=('delete',), fill='blue')
            return True
        return False

    def clear(self):
        self.w.delete('delete')
        self.game = np.array([[0,0,0],
                              [0,0,0],
                              [0,0,0]])
        self.game_end = False

    def x_won(self):
        self.w.create_text(300,300,font='Times 40 bold',text='X won!', tags=('delete',), fill='blue')

    def o_won(self):
        self.w.create_text(300,300,font='Times 40 bold',text='O won!', tags=('delete',), fill='blue')
            
        
            
def main():            
    
    root = Tk()
    mainwindow = MainWindow(root)
    root.mainloop()
    
if __name__ == "__main__": main()
