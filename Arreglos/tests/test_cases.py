from src.bubble_sort import bubble_sort
from src.selection_sort import selection_sort
from src.find_element import find_max, find_min

def run_tests():
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Test Bubble Sort
    print("Bubble Sort:", bubble_sort(arr.copy()))
    
    # Test Selection Sort
    print("Selection Sort:", selection_sort(arr.copy()))
    
    # Test Find Max
    print("Max Element:", find_max(arr))
    
    # Test Find Min
    print("Min Element:", find_min(arr))

if __name__ == "__main__":
    run_tests()
