import unittest

class Number():
    def __init__(self,value):
        self.value = value
        
    def read_value(self, filename):
        with open(filename, "r") as file:
            self.value = int(file.read().strip())
                
    def write_value(self, filename):
        with open(filename, "w") as file:
            file.write(str(self.value))
        
    def to_octal(self):
        return oct(self.value).replace("0o", "")

    def to_hexadecimal(self):
        return hex(self.value).replace("0x", "")
        
    def to_binary(self):
        return bin(self.value).replace("0b", "")



class Tester(unittest.TestCase):
    def setUp(self):
        self.number = Number(12) 
        self.filename = "temp.txt"
    
    def test_write_and_read_file(self):
        self.number.write_value(self.filename)
        self.number.value = None 
        self.number.read_value(self.filename)
        self.assertEqual(self.number.value, 10)
    
    def test_to_octal(self):
        self.assertEqual(self.number.to_octal(), "12") 

    def test_to_hexadecimal(self):
        self.assertEqual(self.number.to_hexadecimal(), "a") 

    def test_to_binary(self):
        self.assertEqual(self.number.to_binary(), "1010") 