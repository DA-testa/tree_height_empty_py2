import sys
import threading
import numpy

def compute_height(n, parents):
    max_height = 0
    return max_height

def main():

    n = int(input("Enter the number of elements: "))
    parents = list(map(int, input("Enter the values of the parents array separated by space: ").strip().split()))
    print("Maximum height of the tree:", compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
