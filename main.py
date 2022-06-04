from math import sin, cos, sqrt
import math
from hill_climbing import HillClimbing
from vns import BVNS
import pickle

def func_1(dict):
    x = dict["x"]
    y = dict["y"]
    return abs(math.pow(x, 2)+math.pow(y, 2)+(x*y))+abs(sin(x))+abs(cos(y))

def func_2(dict):
    x = dict["x"]
    y = dict["y"]
    return (100*sqrt(abs(y-0.01*x**2))+0.01*abs(x+10))

if __name__ == "__main__":
    m = 30
    d = {}
    d["hill_climbing_func_1_1"] = [HillClimbing(func_1, (-500, -500), (500, 500)).solve(0.01) for _ in range(m)]
    d["hill_climbing_func_1_2"] = [HillClimbing(func_1, (-10, -20), (10, 20)).solve(0.01) for _ in range(m)]
    d["hill_climbing_func_2_1"] = [HillClimbing(func_2, (-15, -3), (-5, 3)).solve(0.0001) for _ in range(m)]
    d["hill_climbing_func_2_2"] = [HillClimbing(func_2, (-11, 0), (-9, 2)).solve(0.0001) for _ in range(m)]

    d["bvns_func_1_1"] = [BVNS(func = func_1, lower_bound=(-500, -500), upper_bound=(500, 500), step = 0.01).solve(kmax = 3, tmax=3) for _ in range(m)]
    d["bvns_func_1_2"] = [BVNS(func = func_1, lower_bound=(-10, -20), upper_bound=(10, 20), step = 0.01).solve(kmax = 3, tmax=3) for _ in range(m)]
    d["bvns_func_2_1"] = [BVNS(func = func_2, lower_bound=(-15, -3), upper_bound=(-5, 3), step = 0.0001).solve(kmax = 3, tmax=3) for _ in range(m)]
    d["bvns_func_2_2"] = [BVNS(func = func_2, lower_bound=(-11, 0), upper_bound=(-9, 2), step = 0.0001).solve(kmax = 3, tmax=3) for _ in range(m)]

    with open('experimento.pkl', 'wb') as f:
        pickle.dump(d, f, protocol=pickle.HIGHEST_PROTOCOL)

    # print(HillClimbing(func_1, (-500, -500), (500, 500)).solve(0.01))
    # print(HillClimbing(func_1, (-10, -20), (10, 20)).solve(0.01))

    # print(HillClimbing(func_2, (-15, -3), (-5, 3)).solve(0.0001))
    # print(HillClimbing(func_2, (-11, 0), (-9, 2)).solve(0.0001))

    # print(BVNS(func = func_1, lower_bound=(-500, -500), upper_bound=(500, 500), step = 0.01).solve(kmax = 3, tmax=3))
    # print(BVNS(func = func_1, lower_bound=(-10, -20), upper_bound=(10, 20), step = 0.01).solve(kmax = 3, tmax=3))

    # print(BVNS(func = func_2, lower_bound=(-15, -3), upper_bound=(-5, 3), step = 0.0001).solve(kmax = 3, tmax=3))
    # print(BVNS(func = func_2, lower_bound=(-11, 0), upper_bound=(-9, 2), step = 0.0001).solve(kmax = 3, tmax=3))