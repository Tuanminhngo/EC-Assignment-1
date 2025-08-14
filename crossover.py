import random
from collections import  defaultdict

class Crossover:
    def order(parent1, parent2):
        """
        Perform Order Crossover (OX) between two parents.

        Args:
            parent1 (list): First parent permutation.
            parent2 (list): Second parent permutation.

        Returns:
            tuple: Two children (list, list)
        """
        parent1 = parent1[:]
        parent2 = parent2[:]
        n = len(parent1)
        
        # pick 2 random alleles positions
        i, j = sorted(random.sample(range(n), 2))
        # i, j = 3, 6

        def gen_child_order(parent1, parent2):
            child = [None] * n
            
            child[i:j+1] = parent1[i:j+1]
            start = j + 1
            for idx in range(n):
                k = (j + idx + 1) % n
                if (parent2[k] not in child):
                    next_idx = start % n
                    child[next_idx] = parent2[k]
                    start += 1
            
            return child
                    
        child1 = gen_child_order(parent1, parent2)
        child2 = gen_child_order(parent2, parent1)

        return child1, child2
            
        
    def pmx(parent1, parent2):
        """
        Perform Partially Mapped Crossover (PMX) between two parents.

        Args:
            parent1 (list): First parent permutation.
            parent2 (list): Second parent permutation.

        Returns:
            tuple: Two children (list, list)
        """
        parent1 = parent1[:]
        parent2 = parent2[:]
        n = len(parent1)

        # pick 2 random alleles position
        i, j = sorted(random.sample(range(n), 2))
        # i, j = 3, 6

        def gen_child_pmx(parent1, parent2):
            child = [None] * n

            # copy segment from parent1
            child[i:j+1] = parent1[i:j+1]

            # mapping
            for k in range(i, j+1):
                if parent2[k] not in child:
                    val = parent2[k]
                    pos = k
                    # Resolve conflicts
                    while True:
                        mapped_val = parent1[pos]
                        pos = parent2.index(mapped_val)
                        if child[pos] is None:
                            child[pos] = val
                            break
            
            # fill remaining positions from parent2
            for k in range(n):
                if child[k] is None:
                    child[k] = parent2[k]

            return child

        # Generate two children
        child1 = gen_child_pmx(parent1, parent2)
        child2 = gen_child_pmx(parent2, parent1)

        return child1, child2

    def cycle(parent1, parent2):
        """
        Perform Cycle Crossover (CX) between two parents.

        Args:
            parent1 (list): First parent permutation.
            parent2 (list): Second parent permutation.

        Returns:
            tuple: Two children (list, list).
        """
        parent1 = parent1[:]
        parent2 = parent2[:]
        n = len(parent1)
        child1 = [None] * n
        child2 = [None] * n

        # track visited positions
        visited = [False] * n

        cycle_num = 0
        while not all(visited):
            # find first unvisited position
            start = visited.index(False)
            index = start
            cycle = []

            # follow the cycle
            while not visited[index]:
                visited[index] = True
                cycle.append(index)
                index = parent1.index(parent2[index])

            # assign values based on cycle number
            if cycle_num % 2 == 0: 
                for idx in cycle:
                    child1[idx] = parent1[idx]
                    child2[idx] = parent2[idx]
            else:  
                for idx in cycle:
                    child1[idx] = parent2[idx]
                    child2[idx] = parent1[idx]

            cycle_num += 1

        return child1, child2

    def edge_recombination(parent1, parent2):
        """
        Perform Edge Recombination Crossover between two parents.

        Args:
            parent1 (list): First parent permutation.
            parent2 (list): Second parent permutation.

        Returns:
            list: child permutations.
        """
        parent1 = parent1[:]
        parent2 = parent2[:]
        n = len(parent1)

        # Builds the edge table from two parents.
        edge_table = defaultdict(set)
        for p in (parent1, parent2):
            for i in range(len(p)):
                left = p[i - 1]
                right = p[(i + 1) % len(p)]

                # check common edge
                if (left, False) not in edge_table[p[i]]:
                    edge_table[p[i]].add((left, False))
                else:
                    edge_table[p[i]].remove((left, False))
                    edge_table[p[i]].add((left, True))
                
                if (right, False) not in edge_table[p[i]]:
                    edge_table[p[i]].add((right, False))
                else:
                    edge_table[p[i]].remove((right, False))
                    edge_table[p[i]].add((right, True))

        current = random.choice(parent1)
        child = [current] 
        while len(child) < n:
            for key, value in edge_table.items():
                value.discard((current, False))
                value.discard((current, True))

            candidate_edges = edge_table[current]
            if len(candidate_edges) != 0:
                common_edges = [edge for (edge, is_common) in candidate_edges if is_common == True]
                if common_edges:
                    next_city = random.choice(common_edges)
                else:
                    min_len = min(len(edge_table[edge]) for (edge, _) in candidate_edges)
                    shortest = [edge for (edge, _) in candidate_edges if len(edge_table[edge]) == min_len]
                    next_city = random.choice(shortest)
            else:
                remaining = [city for city in parent1 if city not in child]
                if remaining:
                    next_city = random.choice(remaining)
                else:
                    break

            child.append(next_city)
            current = next_city

        return child

            
        


        
            
                

                