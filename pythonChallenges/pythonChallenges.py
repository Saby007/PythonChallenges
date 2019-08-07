import unittest
import ArraySequences.twoNumberSum as  tn

def TestArrays():
    #twonumbersum test
    tn.func(4,6)
    #assertEqual(twoNumberSum([4, 6], 10), [4, 6])

if __name__ == "__main__":
    while(True):
        print("-----------------------------------------------")
        print("1. Array Sequences")
        print("2. Stacks Queues & Dequeues")
        print("3. Linked Lists")
        print("4. Recursion")
        print("5. Trees")
        print("6. Searching and Sorting")
        print("7. Riddles")
        print("------------------------------------------------")
        res = input("Please enter your response: ")
        if(res == "1"):
            TestArrays()
        res = input("Do you want to continue : ")
        if(res != "y"):
            break

