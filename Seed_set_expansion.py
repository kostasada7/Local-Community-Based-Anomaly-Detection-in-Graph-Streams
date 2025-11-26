from anchor_seed1 import find_anchor_community
from weights_with_anchors import positive_weight, negative_weight
from BestBFS import neighbors_in_depth
import os
import re


def Dynamic_anchor_community(G,edg,edges_n,C, graph_df,anchor,a,data=True):
    y=0
    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        return [ atoi(c) for c in re.split(r'(\d+)', text) ]

    for root, dirs, files in os.walk('communities', topdown=True, onerror=None, followlinks=False):
     files.sort(key=natural_keys)
    #files.pop(0)
    res = list(map(lambda sub:int(''.join(
          [ele for ele in sub if ele.isnumeric()])), files))
    #print(res)
    depth=[anchor]
    L=0
    for i in range(len(graph_df)): 
     #print(i)   
     if graph_df.loc[i,"Iter"]-1 in res:
          res.remove(graph_df.loc[i,"Iter"]-1)
          for x in range(1,len(C[3])):
              if C[3][x-1] >= C[3][x]:
              #if C[3][x-1] <= C[3][x]:   
               del C[3][x:]
               del C[2][x:]
               del C[1][x:]
               del C[0][x:]
               #print(i)
               #print("community after scan =",C[0])
               break
          f=open('communities_set_1.txt','a')
            #f.write(str(graph_df.loc[i,"Iter"]))
            #f.write(' ')
          f.write(str(C[0])[1 : -1]) 
          f.write('\n')   
     if graph_df.loc[i,"node1"] not in G:
              G.add_node(graph_df.loc[i,"node1"])
     if graph_df.loc[i,"node2"] not in G:
              G.add_node(graph_df.loc[i,"node2"])              
     #print(i)
     if graph_df.loc[i,"Type"]== "-":
        negative_weight(G,edg,edges_n,C,graph_df,i,anchor,a,data=True)
     elif graph_df.loc[i,"Type"]== "+":   
        positive_weight(G,edg,edges_n,C,graph_df,i,anchor,a,data=True)
     if graph_df.loc[i,"node1"] in depth or graph_df.loc[i,"node2"] in depth:
         depth=neighbors_in_depth(G, anchor, 1 ,data=True)           
         NEW1=G.subgraph(depth)
         L=len(NEW1.edges())
         edg[0] +=1
     Comm1=G.subgraph(C[0])
     L1=len(Comm1.edges())
     if  edges_n[0] > 0.3*L1 or edg[0] > 0.3*L: 
          for x in range(1,len(C[3])):
              if C[3][x-1] >= C[3][x]:
              #if C[3][x-1] <= C[3][x]:   
               del C[3][x:]
               del C[2][x:]
               del C[1][x:]
               del C[0][x:]
               #print(i)
               #print("community after scan =",C[0])
               break
          edges_n[0] += -edges_n[0]          
          edg[0] += -edg[0]
          C=find_anchor_community(G,C,a,data=True)          
          y +=1
    

