import math
import numpy as np
import matplotlib.pyplot as plt

def load_graph(input_file):

    file = open(input_file, "r")
    n = int(file.readline())

    # setup graph
    graph = [[0]*n for i in range(0, n)]

    coords_list = []
    for i in range(0, n):
        coords = file.readline()
        coords_arr = coords.split()
        coords_list.append([float(coords_arr[1]), float(coords_arr[2])])

    for i in range(0, n):
        for j in range(i+1, n):
            edge = math.sqrt((coords_list[i][0] - coords_list[j][0])
                             ** 2 + (coords_list[i][1] - coords_list[j][1])**2)
            graph[i][j] = edge
            graph[j][i] = edge

    file.close()
    return graph,coords_list

def generate_trucks(route,breaks):
    trucks = []
    for i in range(len(breaks)):
        if i==0:
            end_pos = breaks[i]
            truck = route[:end_pos]
            truck.append(0)
        else:
            start_pos = end_pos
            end_pos = breaks[i]
            truck = route[start_pos:end_pos]
            truck.insert(0,0)
            truck.append(0)
        trucks.append(truck)
    start_pos = end_pos
    truck = route[start_pos:]
    truck.insert(0,0)
    truck.append(0)
    trucks.append(truck)
    return trucks

def compute_angles(node_0, nodes):
    x_0, y_0 = node_0[0],node_0[1]
    angles = []
    for i in range(len(nodes)):
        angle = np.arctan2(nodes[i][1]-y_0,nodes[i][0]-x_0) 
        angles.append([i+1,angle])
    return angles

def plot_result(coords_list,trucks, m):
    colors = ['brown','red','yellow','green','pink']
    for i in range(m):
        plot_x_set = []
        plot_y_set = []
        for j in trucks[i]:
            plot_x_set.append(int(coords_list[j][0]))
            plot_y_set.append(int(coords_list[j][1]))
            plt.plot(plot_x_set,plot_y_set,colors[i])
            plt.scatter(plot_x_set,plot_y_set)
    plt.show()

