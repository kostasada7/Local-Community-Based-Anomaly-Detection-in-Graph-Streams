from itertools import combinations
import networkx as nx
from networkx import NetworkXError
from networkx.utils import not_implemented_for
from networkx.utils.decorators import argmap
from networkx.algorithms.community.community_utils import is_partition
from itertools import chain



#G = nx.karate_club_graph()
#p=[]
#C=[31,24,3]

def all_neighbors(G, node):
    l=[]    
    values = list(G.neighbors(node))
    return values  


#for node in C: 
 #    kostas=all_neighbors(G,node)
  #   p.extend(kostas)
#print(p)    
