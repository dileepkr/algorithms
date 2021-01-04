import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_graphs"))
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_queues"))
from graph_adt import Graph

def knight_graph(board_size):
    #for a 8x8 board, board_size is 8
    kt_graph = Graph()
    for row in range(len(board_size)):
        for col in range(len(board_size)):
            curr_node_id = pos_to_node_id(row, col, board_size)
            legal_moves = gen_legal_knight_moves(row, col, board_size)
            for legal_move in legal_moves:
                legal_move_node_id = pos_to_node_id(legal_move[0], legal_move[1], board_size)
                kt_graph.add_edge(curr_node_id, legal_move_node_id)
    return kt_graph

def pos_to_node_id(row, col, board_size):
    '''
    Given row, col, board_size, return linear position of the square
    '''
    return (row * board_size) + col

def gen_legal_knight_moves(row, col, board_size):
    
    def is_valid(move, board_size):
        return 0 <= move[0] < board_size and 0 <= move[1] < board_size

    legal_moves = [] # list of tuples
    knight_locations = [
            (1,2), (2,1),
            (-1,2), (-2,1),
            (-1,-2), (-2,-1),
            (1,-2), (2,-1),
        ]
    for location in knight_locations:
        new_legal_move = ()
        new_legal_move[0] = row + location[0]
        new_legal_move[1] = col + location[1]

        if is_valid(new_legal_move, board_size):
            legal_moves.append(new_legal_move)
    return legal_moves

def knight_tour(cur_depth, path, cur_vertex, limit):
    '''
    n = current depth in the search tree
    path = list of verties visited up to this point 
    u = vertex in the graph we wish to explore
    limit = number of nodes in the path
    '''
    cur_vertex.set_color('gray')
    path.append(cur_vertex)
    if cur_depth < limit:
        nbr_list = list(cur_vertex.get_connections())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(cur_depth+1, path, nbr_list[i], limit)
            i = i+1
        if not done:
            path.pop()
            cur_vertex.set_color('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for vertex in n.getConnections():
        if vertex.getColor() == 'white':
            c = 0
            for nbr in vertex.getConnections():
                if nbr.getColor() == 'white':
                    c = c + 1
            resList.append((c,vertex))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]