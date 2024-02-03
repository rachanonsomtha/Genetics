def is_pareto_dominated(p1, p2):
    # Check if p1 is Pareto-dominated by p2
    return all(x <= y for x, y in zip(p1, p2)) and any(x < y for x, y in zip(p1, p2))

def pareto_sort(population):
    pareto_front = []  # Pareto front solutions
    dominated = set()  # Individuals dominated by others

    for i, ind1 in enumerate(population):
        is_dominated = False
        for j, ind2 in enumerate(population):
            if i != j:
                if is_pareto_dominated(ind1, ind2):
                    is_dominated = True
                    dominated.add(i)
                    break
        if not is_dominated:
            pareto_front.append(ind1)

    # Sort Pareto front by the first objective (or another objective of your choice)
    pareto_front.sort(key=lambda x: x[0])  # Change the index (0) to the objective you want to use

    return pareto_front

# Example usage
population = [(5, 10), (4, 12), (6, 8), (3, 13), (5, 9)]
pareto_sorted_population = pareto_sort(population)

# Print the Pareto-optimal solutions
for ind in pareto_sorted_population:
    print(ind)
