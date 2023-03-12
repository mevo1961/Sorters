import pytest
from Sorter import Sorter as S

class Display():
    def __init__(self):
        pass

    def show_data(self, data):
        pass

    def show_info(self, info):
        pass

@pytest.fixture
def reference_list():
    length = 10
    return [x for x in range(1, length + 1)] 

def test_sorters(reference_list):
    print('testing bubblesort' )
    display = Display()
    for algorithm in [S.BubbleSort, S.SelectionSort, S.InsertionSort, S.QuickSort, S.MergeSort]:
        sorter = algorithm(len(reference_list), display)
        resultList = sorter.sort()
        assert resultList == reference_list, f'{algorithm} failed'