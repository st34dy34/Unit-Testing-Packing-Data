from unit_testing import Number,Tester
import unittest

filename = "temp.txt"
running = True
options = """
Do you wish to:
1) Unit test
2) Pack Data
3) Exit Program

"""
if __name__ == '__main__':
    while running:
        print(options)
        choice = input()
        
        if choice == "1":
            unittest.main()
        elif choice == "3":
            running = False
        
    
        