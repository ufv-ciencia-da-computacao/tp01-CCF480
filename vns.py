import random
import math
from tabnanny import check
from time import time
from tokenize import Double
from matplotlib.pyplot import step
import numpy as np

from typing import Dict, Iterable, List, Union


class BVNS:
    def __init__(self, func, lower_bound, upper_bound, step=0.001, k=3) -> None:
        self.func = func
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.start_value =  {"x": random.uniform(lower_bound[0], upper_bound[0]), 
                                "y": random.uniform(lower_bound[1], upper_bound[1])}
        self.step = step
        self.k = k

    def check_upper_bound(self, x, y) -> Iterable[Union[int, int]]:
        if x > self.upper_bound[0]:
            x = self.upper_bound[0]
        if y > self.upper_bound[1]:
            y = self.upper_bound[1]

        return x, y
    
    def check_lower_bound(self, x, y) -> Iterable[Union[int, int]]:
        if x < self.lower_bound[0]:
            x = self.lower_bound[0]
        if y < self.lower_bound[1]:
            y = self.lower_bound[1]

        return x, y


    def neighbors(self, curr_value: Dict, k: int=1) -> List[Dict]:
        X = curr_value['x']
        Y = curr_value['y']

        self.step *= k

        vis_pts = []

        x, y = self.check_upper_bound(X + self.step, Y + self.step)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_lower_bound(X - self.step, Y - self.step)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_upper_bound(X + self.step, Y)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_upper_bound(X, Y + self.step)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_lower_bound(X - self.step, Y)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_lower_bound(X, Y - self.step)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_upper_bound(X + self.step, Y - self.step)
        x, y = self.check_lower_bound(x, y)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        x, y = self.check_upper_bound(X - self.step, Y + self.step)
        x, y = self.check_lower_bound(x, y)
        c = {"x": x, "y": y}
        vis_pts.append(c)

        return vis_pts

    def shake(self, point: Dict, k: int) -> Dict:
        neighs = self.neighbors(point, k)
        idx = math.floor(random.uniform(0, len(neighs)))

        return neighs[idx]

    def best_improvement(self, curr_pt: Dict) -> Iterable[Union[int, Dict]]:

        curr_value = self.func(curr_pt)
        min_arr = [curr_value]

        while (True):
            vis_pts = self.neighbors(curr_pt)
            vis_func_values = list(map(lambda x: self.func(x), vis_pts))

            min_value_idx = np.argmin(vis_func_values)
            min_value = vis_func_values[min_value_idx]
            
            if min_value >= curr_value:
                return min_value, curr_pt
            else:
                curr_pt = vis_pts[min_value_idx]
                curr_value = min_value
                        
            min_arr.append(curr_value)

    def neighborhood_change(self, curr_pt, sol_pt, k) -> Iterable[Union[Dict, int]]:
        if self.func(sol_pt) < self.func(curr_pt):
            return sol_pt, 1
        else:
            return curr_pt, k+1

    def solve(self, kmax: int = 3, tmax: int = 20):
        curr_pt = self.start_value

        tmax = time() + tmax

        while(time() < tmax):
            k = 1
            while (k <= kmax):
                candidate_neigh_pt = self.shake(curr_pt, k)
                min_value, candidate_sol_pt = self.best_improvement(candidate_neigh_pt)
                curr_pt, k = self.neighborhood_change(curr_pt, candidate_sol_pt, k)

        return self.func(curr_pt), curr_pt
