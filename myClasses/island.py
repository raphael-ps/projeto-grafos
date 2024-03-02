from .region import *
from .path import *
from .dangers import *
from .creatures import *
from .heal import *
from math import ceil


class Island: #Mesmo que grafo
    def __init__(self):
        self.regions = []

    def add_region(self, value : int) -> Region:
        new_region = Region(value)
        self.regions.append(new_region)
        return new_region

    def add_path(self, region1 : Region, region2 : Region):
        region1.paths.append(Path(region2))
        region2.paths.append(Path(region1))

    def toString(self):
        for region in self.regions:
            region.toString()
            print("")
    
    def prepare_island(self, num_regions : int):
        self.number_of_regions = num_regions
        
        #Cria quantidade de regiões passadas por parâmetro
        for index in range(0, num_regions):
            new_region = self.add_region(index)
            
            #Cria aresta entre a nova região criada e todas criadas anteriormente
            for region in self.regions[:-1]:
                self.add_path(new_region, region)
        
        num_events = int(ceil(num_regions * 0.3))
        
        print("events:", num_events)
        
        avaible_regions = self.regions[1:]
        
        for cont in range(0, num_events):
            region_index = random.randint(0, len(avaible_regions)-1)
            self.regions[region_index].add_random_region_event()
            print("Regiao sorteada:", self.regions[region_index].value)
            avaible_regions.pop(region_index)