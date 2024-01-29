import math
import cexprtk


# set this value to number of discrete points in physical system
global num_points_x, num_points_y 
num_points_x = 10
num_points_y = 10

class graph:
    def __init__(self,funct):
        self.x_step = 1
        self.y_step = 1
        self.parsed_function
        
        n = 5
        self.z_array = [[0]*num_points_x]*num_points_y

        st = cexprtk.Symbol_Table({'x':1.0, 'y':1.0}, add_constants=True)
        parsed_function = cexprtk.Expression(funct, st)
        # establish function as an Expression that can be evaluated

        def f(x,y):
            st.variables['x', 'y'] = [x, y]
            return parsed_function()

    def fill(x_min, x_max, y_min, y_max):
        x_step = (x_max - x_min) / num_points_x
        y_step = (y_max - y_min) / num_points_y

        for x in range(0,num_points_x,x_step):
            for y in range(0,num_points_y,y_step):
                z_array[x][y] = f(x,y)




