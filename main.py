from unit_testing import Number,Tester
from packing_data import Car, Packing
import unittest

filename = "files/temp.txt"
json_path = "files/test.json"
pickle_path = "files/test.pkl"
running = True
options = """
Do you wish to:
1) Unit test
2) Pack Data into JSON
3) Unpack Data from JSON
4) Pack Data into Pickle
5) Unpack Data from Pickle
6) Exit Program
"""

if __name__ == '__main__':
    while running:
        print(options)
        choice = input()
        if choice == "1":
            unittest.main()
        elif choice == "2":
            print(f"Packing json data To {json_path}")
            car = Car("Porsche",2001,["Petr","David"],True)
            Packing.json_pack(car,json_path)
        elif choice == "3":
            print(f"Unpacking data from {json_path}")
            Packing.json_unpack(json_path)
        elif choice == "4":
            print(f"Packing pickle data to {pickle_path}")
            car = Car("Porsche",2001,["Petr","David"],True)
            Packing.pickle_pack(car,pickle_path)
        elif choice == "5":
            print(f"Unpickling data from {pickle_path}")
            Packing.pickle_unpack(pickle_path)
        
        elif choice == "6":
            running = False
        
    
        