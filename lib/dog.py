#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init__(self,name="Buddy", breed = "Corgi"):
        self._name = None
        self._breed = None

        self.name = name
        self.breed = breed

    def get_breed(self):
        return self._breed
    
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")


    def get_name(self):
        return self._name
    
    def set_name(self,name):
        is_valid =isinstance(name,str) and 1 <= len(name) <= 25

        if is_valid:
            self._name = name
        
        else:
             print( "Name must be string between 1 and 25 characters.")

    name = property(get_name,set_name)
    breed = property(get_breed,set_breed) 

    
