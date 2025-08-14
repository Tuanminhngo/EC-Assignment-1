import tsplib95
from collections import defaultdict
from mutation import Mutation
from crossover import Crossover

# Load from local file
problem = tsplib95.load_problem('./Data/eil51.tsp')
print(problem.name)          # 'eil51'
print(problem.dimension)     # 51
print(problem.edge_weight_type)  # EUC_2D

# Get all nodes and coordinates
coords = problem.node_coords
print(coords[1])  # (37.0, 52.0)
print(type(coords[1]))

# Distance between 1 and 2
print(problem.get_weight(1, 3))

# Mutation examples
route = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Mutation')
insert_mutation = Mutation.insert(route)
print(f'insert mutation: {insert_mutation}')

swap_mutation = Mutation.swap(route)
print(f'swap mutation: {swap_mutation}')

inversion_mutation = Mutation.inversion(route)
print(f'inversion mutation: {inversion_mutation}')
print()

# Crossover examples
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

print('Order Crossover')
children1, children2 = Crossover.order(parent1, parent2)
print(f'children1: {children1}')
print(f'children2: {children2}')
print()

print('PMX Crossover')
children1, children2 = Crossover.pmx(parent1, parent2)
print(f'children1: {children1}')
print(f'children2: {children2}')

print('Cycle Crossover')
children1, children2 = Crossover.cycle(parent1, parent2)
print(f'children1: {children1}')
print(f'children2: {children2}')

print('Edge Recombination Crossover')
children1 = Crossover.edge_recombination(parent1, parent2)
children2 = Crossover.edge_recombination(parent1, parent2)
print(f'children1: {children1}')
print(f'children2: {children2}')
