import random
import time
import tkinter as tk
from tkinter import messagebox

class Sorter():
    def __init__(self, length):
        self.length = length
        self.function_mappings = {
            'bubbleSort': self.bubbleSort,
            'insertionSort': self.insertionSort,
            'mergeSort': self.mergeSort,
            'quickSort': self.quickSort,
            'selectionSort': self.selectionSort,
        }
        self.start = 0
        self.end = 0
        self.algorithm = ''
        self.visualize = Visualize(self.function_mappings, self.length, self.run)
        self.visualize.start_gui()

    def get_function_mappings(self):
        return self.function_mappings

    def run(self):
        self.algorithm = self.visualize.get_algorithm()
        self.function_mappings[self.algorithm]()
        self.visualize.stop()

    def set_algorithm(self, algorithm):
        self.algorithm = self.visualize.select_algorithm()

    def get_algorithm(self):
        return self.algorithm

    def select_algorithm_by_buttons(self):
        self.algorithm = self.var.get()

    def init_data(self, length):
        randomlist = random.sample(range(1, length + 1), length)
        self.data = randomlist

    def startSorting(self):
        self.init_data(self.length)
        msg = f'{self.algorithm} is sorting {len(self.data)} items'
        # if len(self.data) <= 100:
        #     msg += str(self.data)
        # messagebox.showinfo(title=None, message=msg)
        print(msg)
        self.visualize.set_data(self.data)
        self.visualize.set_olddata(self.data)
        self.visualize.show_data(self.data)
        self.start = time.time()

    def endSorting(self):
        self.end = time.time()
        msg = f'{self.algorithm} took {round(self.end - self.start, 3)} seconds to sort {len(self.data)} items'
        if len(self.data) <= 100:
            msg += str(self.data)
        messagebox.showinfo(title=None, message=msg)

    def bubbleSort(self):
        self.startSorting()
        for i in range(len(self.data)):
            for j in range(i+1, len(self.data)):
                if self.data[i] > self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
            self.visualize.show_data(self.data)
        self.endSorting()
        return self.data
    
    def selectionSort(self):
        self.startSorting()
        for i in range(len(self.data)):
            min = i
            for j in range(i+1, len(self.data)):
                if self.data[min] > self.data[j]:
                    min = j
            self.data[i], self.data[min] = self.data[min], self.data[i]
            self.visualize.show_data(self.data)
        self.endSorting()
        return self.data
    
    def insertionSort(self):
        self.startSorting()
        for i in range(1, len(self.data)):
            j = i
            while j > 0 and self.data[j-1] > self.data[j]:
                self.data[j], self.data[j-1] = self.data[j-1], self.data[j]
                j -= 1
            self.visualize.show_data(self.data)
        self.endSorting()
        return self.data
    
    def _quickSort(self, left, right):
        if left >= right:
            return
        pivot = self.data[(left + right) // 2]
        index = self._partition(left, right, pivot)
        self._quickSort(left, index - 1)
        self._quickSort(index, right)
        return self.data
    
    def _partition(self, left, right, pivot):
        while left <= right:
            while self.data[left] < pivot:
                left += 1
            while self.data[right] > pivot:
                right -= 1
            if left <= right:
                self.data[left], self.data[right] = self.data[right], self.data[left]
                left += 1
                right -= 1
        return left
    
    def quickSort(self):
        self.startSorting()
        self._quickSort(0, len(self.data) - 1)
        end = time.time()
        self.endSorting()
        return self.data
    
    def mergeSort(self):
        self.startSorting()
        self.data = self._mergeSort(self.data)
        self.endSorting()
        return self.data

    def _mergeSort(self, datalist):
        if len(datalist) <= 1:
            return datalist
        mid = len(datalist) // 2
        left = self._mergeSort(datalist[:mid])
        self.visualize.show_data(self.data)
        right = self._mergeSort(datalist[mid:])
        self.visualize.show_data(self.data)
        return self._merge(left, right)
    
    def _merge(self, left, right):
        merged = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1  
        merged += left[left_index:]
        merged += right[right_index:]
        return merged
    
class Visualize():
    def __init__(self, function_mappings, size = 500, callback = None):
        self.root = tk.Tk()
        self.root.title('Sorting Algorithms')
        self.function_mappings = function_mappings
        self.algorithm = list(self.function_mappings.keys())[0]
        self.size = size
        self.is_running = False
        self.callback = callback
        self.data = []
        self.olddata = []
        
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

        for key in self.function_mappings.keys():
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

    def get_algorithm(self):
        return self.algorithm

    def set_data(self, data):
        self.data = data

    def set_olddata(self, data):
        self.olddata = data

    def draw_dot(self, x, y, color):
        self.canvas.create_line(x, y, x+1, y+1, fill=color)

    def show_data(self, data):
        self.set_data(data)
        # self.canvas.delete('all')
        for i in range(len(self.olddata)):
            self.draw_dot(i, self.olddata[i], self.canvas['bg'])
        for i in range(len(self.data)):
            self.draw_dot(i, self.data[i], 'red')
        self.set_olddata(self.data.copy())
        self.canvas.update_idletasks()
    
    def run(self):
        self.canvas.delete('all')
        self.callback()

    def stop(self):
        self.is_running = False

    def running(self):
        return self.is_running
        

if __name__ == '__main__':
    sorter = Sorter(200)