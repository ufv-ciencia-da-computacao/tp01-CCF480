import random
import math
from tabnanny import check
from matplotlib.pyplot import step
import numpy as np

from typing import Dict, List


class HillClimbing:
    def __init__(self, func, lower_bound, upper_bound) -> None:
        self.func = func
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.start_value =  {"x": random.uniform(lower_bound[0], upper_bound[0]), 
                                "y": random.uniform(lower_bound[1], upper_bound[1])}

    def check_upper_bound(self, x, y):
        if x > self.upper_bound[0]:
            x = self.upper_bound[0]
        if y > self.upper_bound[1]:
            y = self.upper_bound[1]

        return x, y
    
    def check_lower_bound(self, x, y):
        if x < self.lower_bound[0]:
            x = self.lower_bound[0]
        if y < self.lower_bound[1]:
            y = self.lower_bound[1]

        return x, y


    def neighbors(self, curr_value: Dict, step, vis_pts: List[Dict], vis_func_values: List[float]) -> Dict:
        X = curr_value['x']
        Y = curr_value['y']

        x, y = self.check_upper_bound(X + step, Y + step)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_lower_bound(X - step, Y - step)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_upper_bound(X + step, Y)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_upper_bound(X, Y + step)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_lower_bound(X - step, Y)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_lower_bound(X, Y - step)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_upper_bound(X + step, Y - step)
        x, y = self.check_lower_bound(x, y)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

        x, y = self.check_upper_bound(X - step, Y + step)
        x, y = self.check_lower_bound(x, y)
        c = {"x": x, "y": y}
        vis_pts.append(c)
        vis_func_values.append(self.func(c))

    def solve(self, step: float):

        curr_pt = self.start_value
        curr_value = self.func(curr_pt)

        min_arr = [curr_value]
        
        while(True):
            vis_pts = []
            vis_func_values = []
            self.neighbors(curr_pt, step, vis_pts, vis_func_values)

            min_value_idx = np.argmin(vis_func_values)
            min_value = vis_func_values[min_value_idx]
            
            if min_value >= curr_value:
                return min_value, curr_pt
            else:
                curr_pt = vis_pts[min_value_idx]
                curr_value = min_value
                        
            min_arr.append(curr_value)

            
            
        
