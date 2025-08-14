import random

class Mutation:
    def insert(route):
        """
        Perform insert mutation on a permutation route.
        
        Args:
            route (list): A list representing the permutation (e.g., city order).
        
        Returns:
            list: A new route with one element inserted elsewhere.
        """
        route = route[:]
        n = len(route)

        # pick 2 random alleles
        i, j = sorted(random.sample(range(n), 2))

        # inserting
        element = route.pop(j)
        route.insert(i + 1, element)

        return route

    def swap(route):
        """
        Perform swap mutation on a permutation route.
        
        Args:
            route (list): A list representing the permutation (e.g., city order).
        
        Returns:
            list: A new route with 2 alleles swapping their positions elsewhere.
        """
        route = route[:]
        n = len(route)
        
        # pick 2 random alleles
        i, j = random.sample(range(n), 2)
        
        # swap
        temp = route[i]
        route[i] = route[j]
        route[j] = temp

        return route
    
    def inversion(route):
        """
        Perform swap mutation on a permutation route.
        
        Args:
            route (list): A list representing the permutation (e.g., city order).
        
        Returns:
            list: A new route with an inverse segment elsewhere.
        """
        route = route[:]
        n = len(route)

        # pick 2 random alleles
        i, j = sorted(random.sample(range(n), 2))

        # inverse the segment between 2 alleles
        route[i:j+1] = reversed(route[i:j+1])

        return route