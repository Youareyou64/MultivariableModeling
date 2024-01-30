import math
import cexprtk
import matplotlib
import numpy as np


# set this value to number of discrete points in physical system
global num_points_x, num_points_y 
num_points_x: int = 10
num_points_y: int = 10
st = cexprtk.Symbol_Table({'x':1.0, 'y':1.0}, add_constants=True)

class Graph:
    def __init__(self,funct):
        self.x_step = 1
        self.y_step = 1

        self.array = np.zeros((num_points_x, num_points_y))

        self.parsed_function = cexprtk.Expression(funct, st)
        # establish function as an Expression that can be evaluated

        print("Graph instance instantiated :)")

    def f(self, x, y):
        st.variables['x'] = x # possible source of errors
        st.variables['y'] = y
        return self.parsed_function()

    def fill(self, x_min, x_max, y_min, y_max):
        x_step = (x_max - x_min) / num_points_x
        print(f"x step set to {x_step}")
        y_step = (y_max - y_min) / num_points_y

        for x in range(0, num_points_x, 1):
            for y in range(0, num_points_y, 1):
                self.array[x,y] = self.f(x_min + x * x_step, y_min + y * y_step)
                # print(f"Filled {x}, {y} with f of {x_min + x * x_step}, {y_min + y * y_step} = {self.f(x_min + x * x_step, y_min + y * y_step)}")
                # print(np.matrix(self.array))
        # print(np.matrix(self.array))

    def get_max(self):
        maximum = self.array[0, 0]
        for x in range(0, num_points_x, 1):
            for y in range(0, num_points_y, 1):
                if self.array[x, y] > maximum:
                    maximum = self.array[x, y]
        print(f"Max value: {maximum} ")
        return maximum

    def get_min(self):
        minimum = self.array[0, 0]
        for x in range(0, num_points_x, 1):
            for y in range(0, num_points_y, 1):
                if self.array[x, y] < minimum:
                    minimum = self.array[x, y]
        print(f"Min value: {minimum}")
        return minimum

    def scale(self):
        min = self.get_min()
        max = self.get_max()

        # Finish this to scale data to available Z height and set appropriate z=0 offset






