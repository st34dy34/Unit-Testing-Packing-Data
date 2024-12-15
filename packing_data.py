import json
import pickle

class Car:
    def __init__(self, brand, year,owners,used):
        self.brand = brand
        self.year = year
        self.owners = owners
        self.used = used
    def to_dict(self):
        return {
            'brand': self.brand,
            'year': self.year,
            'owners': self.owners,
            'used': self.used
        }

class Packing:
    @staticmethod
    def json_pack(car, filepath):
        data = car.to_dict()
        with open(filepath, "w") as f:
            json.dump(data, f)
        print(f"    Done packing data into JSON! Data: {data}")
    
    @staticmethod
    def json_unpack(filepath):
        with open(filepath, "r") as f:
            file_data = json.load(f)
        print("    Here is the data I read from the JSON file:")
        print(file_data)
        return file_data

    @staticmethod
    def pickle_pack(car, filepath):
        data = car.to_dict()
        with open(filepath, "wb") as f:
            pickle.dump(data, f)
        print(f"    Done packing data into Pickle! Data: {data}")
    
    @staticmethod
    def pickle_unpack(filepath):
        with open(filepath, "rb") as f:
            file_data = pickle.load(f)
        print("    Here is the data I read from the Pickle file:")
        print(file_data)
        return file_data