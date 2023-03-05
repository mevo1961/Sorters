import Sorter
import tkinter as tk
from tkinter import messagebox

class SorterGUI():
    def __init__(self, size = 500):
        self.root = tk.Tk()
        self.root.title('Sorting Algorithms')
        self.mapping = {
            'Bubble Sort': Sorter.BubbleSort,
            'Insertion Sort': Sorter.InsertionSort,
            'Merge Sort': Sorter.MergeSort,
            'Quick Sort': Sorter.QuickSort,
            'Selection Sort': Sorter.SelectionSort,
        }
        self.size = size
        self.algorithm = list(self.mapping.keys())[0]
        self.sorter = self.mapping[self.algorithm](self.size, self)
        self.is_running = False
        self.start_gui()
        
    def start_gui(self):
        self.set_canvas()
        self.select_algorithm()
        self.root.mainloop()

    def set_callback(self, callback):
        self.callback = callback

    def set_canvas(self):
        self.frm_canvas = tk.Frame(self.root, relief=tk.GROOVE, borderwidth=5)
        self.frm_canvas.pack(side=tk.LEFT)
        self.canvas = tk.Canvas(self.frm_canvas, width=self.size, height=self.size)
        self.canvas.pack()

    def select_algorithm(self):
        self.var = tk.StringVar(value = self.algorithm)
        self.frm_buttons = tk.Frame(self.root)
        self.frm_buttons.pack(side=tk.RIGHT)

        for key in self.mapping.keys():
            R = tk.Radiobutton(self.frm_buttons, text=key, variable=self.var, value=key,
                  command=self.select_algorithm_by_buttons)
            R.pack( anchor = 'w')
        
        btn_start = tk.Button(
            self.frm_buttons,
            text="Start",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command=self.run
        )
        btn_start.pack(anchor = 's' )

    def select_algorithm_by_buttons(self):
        self.algorithm = self.var.get()
        self.sorter = self.mapping[self.algorithm](self.size, self)

    def get_algorithm(self):
        return self.algorithm

    def draw_dot(self, x, y, color):
        self.canvas.create_line(x, y, x+1, y+1, fill=color)

    def show_data(self, data):
        self.canvas.delete('all')
        for i in range(len(data)):
            self.draw_dot(i, data[i], 'red')
        self.canvas.update_idletasks()
    
    def run(self):
        self.canvas.delete('all')
        self.sorter.sort()

    def stop(self):
        self.is_running = False

    def running(self):
        return self.is_running
        

if __name__ == '__main__':
    display = SorterGUI(200)