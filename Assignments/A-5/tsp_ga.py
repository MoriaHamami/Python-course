import random
import sys
import math

class Point:
    def __init__(self) -> None:
        self.x = random.randint(-100,100)
        self.y = random.randint(-100,100)

def dist(p1,p2):
    return float(math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))

def fitness(points):
    sum=0
    for i in range(1,len(points)):
        sum+=dist(points[i-1],points[i])
    return sum

def randSol(points,size):
    mn=sys.maxsize
    for i in range(size):
        ps = points.copy()
        random.shuffle(ps)
        f = fitness(ps)
        if f<mn:
            mn=f
            best=ps
    return best

def selection(paths):
    # Calculate the length of each path
    paths_len = []
    for path in paths:
        paths_len.append(fitness(path))
    # Select 2 paths, with a probability proportional to their fitness score (shorter path len, better prob)
    # random.choices() considers weighted selection and ensure different paths are selected
    rand_paths = random.choices(paths, k=2, weights=paths_len)
    return rand_paths

def solve(cities):
    cities_amount=50
    gen_alg_reps=100
    paths = []  

    # INITIALIZATION - Loop to create random paths
    for _ in range(cities_amount):  
        # Create a random path by shuffling points
        rand_path = randSol(cities, len(cities)) 
        # Add the random path to the paths list
        paths.append(rand_path)  

    for _ in range(gen_alg_reps):   
        # SELECTION - Select fittest paths to produce new paths     
        rand_paths = selection(paths)
        rand_path1 = rand_paths[0]
        rand_path2 = rand_paths[1]
        # Select a city before the current one
        rand_city_idx = random.randint(0, len(rand_path1)) # len(parents[0] is the amount of cities in path
        # Save the path from start of path1 until the randomly selected city
        sub_path1 = rand_path1[:rand_city_idx]
        
        # CROSSOVER - "mate" between the two selected "fit" paths
        fit_path = rand_path1.copy()
        for city in rand_path2:
            if city not in sub_path1:
                fit_path.append(city)

        # MUTATION - randomly change the fit path to make diversity
        fit_path_idxs = range(len(fit_path))
        rand_idx1, rand_idx2 = random.sample(fit_path_idxs, 2)
        # Swap randomly selected cities
        fit_path[rand_idx1], fit_path[rand_idx2] = fit_path[rand_idx2], fit_path[rand_idx1]
        # Change the longest path with a new random path, with better probability
        longest_path = max(paths, key=fitness)
        longest_path_idx = paths.index(longest_path)
        paths[longest_path_idx] = fit_path

    # Return the shortest path
    return min(paths, key=fitness)

