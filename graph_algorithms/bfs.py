import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_graphs"))
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_queues"))
from graph_adt import Graph
from myqueue import Queue

class Color:
    WHITE = "white"
    GRAY = 'gray'
    BLACK = 'black'

def bfs(g, start):
    '''
    After running through BFS, all vertices of the graph will have their color, distance and predecessor from the start.
    '''
    start.set_predecessor(None)
    start.set_distance(0)
    vert_queue = Queue()
    vert_queue.enqueue(start)

    while vert_queue.size() != 0:
        cur_vertex = vert_queue.dequeue()

        for nbr in cur_vertex.get_connections():
            if nbr.color == Color.WHITE:
                nbr.set_color(Color.GRAY)
                nbr.set_distance(cur_vertex.get_distance() + 1)
                nbr.set_predecessor(cur_vertex)
                vert_queue.enqueue(nbr)
        
        cur_vertex.set_color(Color.BLACK)

def traverse(vertex):
    temp = vertex
    while temp.get_predecessor():
        print(temp.get_key())
        temp = temp.get_predecessor()
    print(temp.get_key())

