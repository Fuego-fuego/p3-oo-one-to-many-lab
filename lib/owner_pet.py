class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_pet_to_all(self)
        
    @property
    def pet_type(self):
        return self._pet_type
    
    
    @pet_type.setter
    def pet_type(self,type):
        if(type in Pet.PET_TYPES):
            self._pet_type = type
        else:
            raise TypeError("Wrong pet type")
        
    @classmethod
    def add_pet_to_all(cls,pet):
        cls.all.append(pet)
class Owner:
    def __init__(self,name):
        self.name = name
    
    def pets(self):
        pets = [pet for pet in Pet.all if pet.owner == self]
        return pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError('This pet does not exist')
    def get_sorted_pets(self):
        pets = self.pets()
        sorted_pets = sorted(pets, key=lambda x: x.name)
        return sorted_pets