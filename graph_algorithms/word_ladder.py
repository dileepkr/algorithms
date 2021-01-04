import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_graphs"))
sys.path.append(os.path.abspath(r"C:\Users\getdi\Desktop\Github repositories\datastructures\ds_queues"))
from graph_adt import Graph, Vertex
from myqueue import Queue
from bfs import bfs, traverse

def build_graph(word_file):
    word_bucket_dict = {}
    g = Graph()
    with open(word_file, 'r') as wfile:
        for line in wfile:
            word = line.strip()[:]
            for i in range(len(word)):
                bucket = word[:i] + '_' +word[i+1:]
                if bucket in word_bucket_dict:
                    word_bucket_dict[bucket].append(word)
                else:
                    word_bucket_dict[bucket] = [word]
    
    for bucket in word_bucket_dict.keys():
        for word1 in word_bucket_dict[bucket]:
            for word2 in word_bucket_dict[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

if __name__ == "__main__":
    graph = build_graph(r'C:\Users\getdi\Desktop\Github repositories\algorithms\graph_algorithms\vocabulary.txt')
    bfs(graph, graph.get_vertex('FOOL'))
    traverse(graph.get_vertex('SAGE'))