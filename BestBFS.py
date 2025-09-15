import networkx as nx
from collections import deque
from collections import defaultdict

def neighbors_in_depth(G, anchor, influence_range,data=True):
    queue = deque([anchor])
    depths = {anchor:0}
    while queue:
        node = queue.popleft()
        if depths[node] == influence_range:            
            break        
        for neighbour in G.neighbors(node):
            if neighbour in depths:
                continue
            queue.append(neighbour)
            depths[neighbour] = depths[node] + 1
    adjacent = []
    for i in depths:
        adjacent.append(i)
    #adjacent.pop(0)
    
    return adjacent

def weight_calculation(G,V, I_N,reward, influence_range, data=True):
    for u,v,d in G.edges(data=True):
      d['weight'] = 1 
    for u,v,d in V.edges(data=True):
     for y in range(0,influence_range):          
      if u in I_N[y] and v in I_N[y]:            
       G[u][v]['weight'] = reward
       
       break
    return
