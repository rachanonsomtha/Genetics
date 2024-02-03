import random
from airport import Airport
from typing import List

class Chromosome:
  def __init__(self, genes: list[list[Airport]]):
    self.genes = genes

  def print_genes(self):
    print("Chromosome infomations")
    for airport_list in self.genes:
        print([airport.name for airport in airport_list])
        
  def repair_module(self):
    # Find overflow cluster in given solution
    overflow_nodes = []
    
    # Detacing minimun-flow nodes from the cluster until the overall cluster flow is with-in the limit of hub capacity
    # Save the nodes detached in an overflow nodes list.
    for cluster in self.genes:
        cluster_flow = sum(airport.flow for airport in cluster[1:])
        cluster_cap = cluster[0].capacity
        
        while cluster_flow > cluster_cap:
            min_flow_node = min(cluster[1:], key= lambda airport: airport.flow)
            cluster.remove(min_flow_node)
            overflow_nodes.append(min_flow_node)
            cluster_flow = sum(airport.flow for airport in cluster[1:])

    
    print(f"Over flow nodes: {[node.name for node in overflow_nodes]}")
    
    # Repeat this step untill all of the nodes have been assigned or furthur assignment is not possible without violating the capacities of the hubs.
    assigned_node = set()
    for node in overflow_nodes:
        for cluster in self.genes:
            if sum(airport.flow for airport in cluster[1:]) + node.flow <= cluster[0].capacity:
                cluster.append(node)
                assigned_node.add(node)
    
    print(f"assined nodes : {[airport.name for airport in assigned_node]}")
    
    overflow_nodes = [node for node in overflow_nodes if node not in assigned_node]
    print(f"Over flow nodes: {[node.name for node in overflow_nodes]}")
    
    # If there are still some un-assigned nodes in the overflow node list, create a new hub (from one of the spokes) with suffients capacity and assign it
    # the remaining nodes.
    while overflow_nodes:
        hub = overflow_nodes.pop(0)
        cluster = [hub]
        
        hub_capacity = hub.capacity
        hub_flow = hub.flow
        
        while overflow_nodes and (sum(airport.flow for airport in cluster[1:]) + overflow_nodes[0].flow) <= hub_capacity:
            spoke = overflow_nodes.pop(0)
            cluster.append(spoke)
            
        self.genes.append(cluster)

    

def generate_chromosome(num_hub, airports: List[Airport]) -> Chromosome:
    if (num_hub / 2 > len(airports)):
        raise ValueError("Number of hub shouldn't exceeds available locations")
    locations = airports
        
    random.shuffle(locations)
    
    hubs = random.sample(locations, num_hub)
    [print(hub.name, end=' ') for hub in hubs]
    print('\n')
    
    chromosome = [[] for _ in range(num_hub)]
    
     # Assign spokes to hubs
    for location in locations:
        hub_index = hubs.index(location) if location in hubs else random.randint(0, num_hub - 1)
        chromosome[hub_index].append(location)
        
    for i in range(num_hub):
        chromosome[i].remove(hubs[i])
        chromosome[i] = [hubs[i]] +  chromosome[i]
        
    return Chromosome(chromosome)

#testing--------

#list of airports location
airports = [Airport(name= "1", flow = 100, capacity= 500),Airport(name= "2", flow = 100, capacity= 200),Airport(name= "3", flow = 100, capacity= 200),
            Airport(name= "4", flow = 100, capacity= 200),Airport(name= "5", flow = 100, capacity= 200),Airport(name= "6", flow = 100, capacity= 200),
            Airport(name= "7", flow = 100, capacity= 200),Airport(name= "8", flow = 100, capacity= 200),Airport(name= "9", flow = 100, capacity= 200),
            Airport(name= "10", flow = 100, capacity= 200),Airport(name= "11", flow = 100, capacity= 200),Airport(name= "12", flow = 100, capacity= 200),
            Airport(name= "13", flow = 100, capacity= 200),Airport(name= "14", flow = 100, capacity= 200),Airport(name= "15", flow = 100, capacity= 200),]

# airports = [
#     Airport(name=f"A {i}", flow=10, capacity=20) for i  in range(1, 16)
# ]

chromosome = generate_chromosome(3, airports)
print("Before repair")
chromosome.print_genes()
chromosome.repair_module()

print("After repair")
chromosome.print_genes()
