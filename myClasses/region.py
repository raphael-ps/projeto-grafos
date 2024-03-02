import random
from .dangers import *
from .heal import *
from .weapons import *
from .creatures import *

class Region(): #Mesmo que vértice
    def __init__(self, value : int):
        region_options = ["Praia", "Montanha", "Floresta", "Lago"]
        region_type = 0 if value == 0 else random.randint(1, len(region_options)-1 )
        
        self.region_type = region_options[region_type]
        self.value = value
        self.paths = []
        self.event = None
    
    def add_random_region_event(self):
        rand = 0
        events = [self.add_random_creature]
        events[rand]()
    
    def add_random_creature(self):
        rand = random.randint(0, len(avaible_creatures)-1)
        self.event = avaible_creatures[rand]()
        
    def toString(self):     
        neighbors_str = ", ".join( (str(path.destination.value) for path in self.paths) ) #+ " Ao Longo De "+path.path_type)
       
        print(f"Vértice: {self.value}\n\tTipo: {self.region_type}\n\tVizinhos: {neighbors_str}")
           
        if self.event != None:
            print("\t", end="")
            self.event.use_attack()
        else: 
            print("\tSem evento nessa região")
        
        
 