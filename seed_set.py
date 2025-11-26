import pandas as pd
import networkx as nx
from Seed_set_expansion import Dynamic_anchor_community
import time
from anchor_seed1 import find_anchor_community
 
start = time.time()
graph_df = pd.read_csv('interactions.txt',sep='\t',header=None)
graph_df.columns = ['Iter', 'Time', 'Type', 'node1', 'node2']
res = graph_df.loc[graph_df['Iter'] < 0]
#Remove rows that belong to iteration 0 from the dataframe to get it ready for step 2
graph_df.drop(graph_df[graph_df['Iter'] < 0].index, inplace = True)
#Because of the drop the index κof the dataframe is not correct. We reset it.
graph_df.reset_index(drop=True, inplace=True)
G = nx.Graph()
nx.set_edge_attributes(G, values = 1, name = 'weight')
G = nx.from_pandas_edgelist(res,'node1', 'node2')
nx.write_edgelist(G, "graph0-edgelist.txt", data=False)
nx.write_gexf(G, "Gephi.gexf")
# USE THE SEED (ANCHOR) YOU WANT. NOW I USE ANCHOR = 0
anchor=0
edg=[0]
edges_n=[0]

a=1
G.add_node(anchor)
C=[[anchor],[0],[0],[0]]
Dynamic_anchor_community(G,edg,edges_n,C, graph_df,anchor,a,data=True)
C=find_anchor_community(G,C,a,data=True)

print(G)

