import random
import time
import tkinter as tk
from tkinter import messagebox

class Sorter():
    def __init__(self, length, display):
        self.length = length
        self.display = display
        self.start = 0
        self.end = 0

    def get_function_mappings(self):
        return self.function_mappings

    def init_data(self, length):
        randomlist = random.sample(range(1, length + 1), length)
        self.data = randomlist

    def switch(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.display.show_data(self.data)

    def startSorting(self):
        self.init_data(self.length)
        msg = f'{__class__.__name__} is sorting {len(self.data)} items'
        if len(self.data) <= 100:
            msg += str(self.data)
        self.display.show_info(msg)
        print(msg)
        self.display.show_data(self.data)
        self.start = time.time()

    def endSorting(self):
        self.end = time.time()
        msg = f'{self.algorithm} took {round(self.end - self.start, 3)} seconds to sort {len(self.data)} items'
        if len(self.data) <= 100:
            msg += str(self.data)
        self.display.show_info(msg)

    def sort():
        # this method must be implemented by the child class
        pass

class BubbleSort(Sorter):
    def __init__(self, length, display):
        super().__init__(length, display)
        self.algorithm = 'Bubble Sort'

    def sort(self):
        self.startSorting()
        for i in range(len(self.data)):
            for j in range(i+1, len(self.data)):
                if self.data[i] > self.data[j]:
                    self.switch(i, j)
            self.display.show_data(self.data)
        self.endSorting()
        return self.data
    
class SelectionSort(Sorter):
    def __init__(self, length, display):
        super().__init__(length, display)
        self.algorithm = 'Selection Sort'

    def sort(self):
        self.startSorting()
        for i in range(len(self.data)):
            min = i
            for j in range(i+1, len(self.data)):
                if self.data[min] > self.data[j]:
                    min = j
            self.data[i], self.data[min] = self.data[min], self.data[i]
            self.display.show_data(self.data)
        self.endSorting()
        return self.data
    
class InsertionSort(Sorter):
    def __init__(self, length, display):
        super().__init__(length, display)
        self.algorithm = 'Insertion Sort'

    def sort(self):
        self.startSorting()
        for i in range(1, len(self.data)):
            j = i
            while j > 0 and self.data[j-1] > self.data[j]:
                self.data[j], self.data[j-1] = self.data[j-1], self.data[j]
                j -= 1
            self.display.show_data(self.data)
        self.endSorting()
        return self.data
    
class QuickSort(Sorter):
    def __init__(self, length, display):
        super().__init__(length, display)
        self.algorithm = 'Quick Sort'

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
                self.switch(left, right)
                # slow down quicksort for better visiblity
                time.sleep(0.01)
                left += 1
                right -= 1
        return left
    
    def sort(self):
        self.startSorting()
        self._quickSort(0, len(self.data) - 1)
        end = time.time()
        self.endSorting()
        return self.data
    
class MergeSort(Sorter):
    def __init__(self, length, display):
        super().__init__(length, display)
        self.algorithm = 'Merge Sort'

    def sort(self):
        self.startSorting()
        self.data = self._mergeSort(self.data)
        self.endSorting()
        return self.data

    def _mergeSort(self, datalist):
        if len(datalist) <= 1:
            return datalist
        mid = len(datalist) // 2
        left = self._mergeSort(datalist[:mid])
        right = self._mergeSort(datalist[mid:])
        self.display.show_data(self.data)
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
    