from airport import Airport
from chromosome import Chromosome, generate_chromosome

def main():
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
    
if __name__ == '__main__':
    main()