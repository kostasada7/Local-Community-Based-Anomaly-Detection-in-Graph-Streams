import decimal
decimal.getcontext().prec = 16

def positive_weight(G,edg,edges_n,C,graph_df,i,anchor,a,data=True):
   queue=[]
   if graph_df.loc[i,"node1"] not in G.neighbors(graph_df.loc[i,"node2"]):
    G.add_edge(graph_df.loc[i,"node1"],graph_df.loc[i,"node2"])
    G[graph_df.loc[i,"node1"]][graph_df.loc[i,"node2"]]['weight']=1
    Dw=1
    l=[]
    if graph_df.loc[i,"node1"] in C[0]:
           l.append(C[0].index(graph_df.loc[i,"node1"]))
    if graph_df.loc[i,"node2"] in C[0]:
           l.append(C[0].index(graph_df.loc[i,"node2"]))
     
    l.sort()
    if len(l) !=0:
        edges_n[0] += 1
        if graph_df.loc[i,"node1"] in C[0] and graph_df.loc[i,"node2"] in C[0]:
         for j in range(l[0],l[1]): 
          C[2][j]=C[2][j]+Dw
          C[3][j] = (2*C[1][j] + 1)/(2*C[1][j]+C[2][j])**a
          #C[3][j] = C[1][j]/(C[2][j] + 1)
          #C[3][j] = 1 - C[2][j]/(2*C[1][j] + C[2][j])               
         for p in range(l[1],len(C[0])): 
          C[1][p]=C[1][p]+Dw
          C[3][p] = (2*C[1][p] + 1)/(2*C[1][p]+C[2][p])**a
          #C[3][p] = C[1][p]/(C[2][p] + 1)
          #C[3][p] = 1 - C[2][p]/(2*C[1][p] + C[2][p])
         #print("update =",C)
        elif graph_df.loc[i,"node1"] in C[0] or graph_df.loc[i,"node2"] in C[0]:   
        
         for q in range(l[0],len(C[0])):
          C[2][q]=C[2][q]+Dw
          C[3][q] = (2*C[1][q] + 1)/(2*C[1][q]+C[2][q])**a
          #C[3][q] = C[1][q]/(C[2][q] + 1)
          #C[3][q] = 1 - C[2][q]/(2*C[1][q] + C[2][q])
          
             
        if graph_df.loc[i,"node1"] in C[0] and graph_df.loc[i,"node2"] in C[0]: 
           if C[0][l[0]] != anchor:
             queue.append(C[0][l[0]])
        elif graph_df.loc[i,"node1"] in C[0] or graph_df.loc[i,"node2"] in C[0]:
           if C[0][l[0]] != anchor:
             queue.append(C[0][l[0]]) 
        #print(C)
        
        while len(queue) > 0: 
           #print("candidate nodes for deletion =",queue) 
           z=queue.pop(0)
                     
            
             
           if z in C[0] and C[3][C[0].index(z)-1] >= C[3][C[0].index(z)]:
           #if z in C[0] and C[3][C[0].index(z)-1] <= C[3][C[0].index(z)]:    
               for g in G.neighbors(z):
                  
                 if g in C[0] and C[0].index(g) > C[0].index(z):
                   queue.append(g)
                   queue = list(dict.fromkeys(queue))
                   for d in range(C[0].index(g),len(C[0])):                    
                          C[1][d] = C[1][d] - G[g][z]['weight']
                          C[2][d] = C[2][d] + G[g][z]['weight']
                            
                 elif g in C[0] and C[0].index(g) < C[0].index(z):
                       
                     for a in range(C[0].index(z)+1,len(C[0])):
                         C[1][a] = C[1][a] - G[g][z]['weight']
                         C[2][a] = C[2][a] + G[g][z]['weight']    
                 elif g not in C[0]:
                       
                     for v in range(C[0].index(z)+1,len(C[0])):
                         C[2][v] = C[2][v] - G[g][z]['weight']                                        
                      
               for s in range(0,len(C[0])):                   
                   C[3][s] = (decimal.Decimal(2)*decimal.Decimal(C[1][s]) + decimal.Decimal(1))/(decimal.Decimal(2)*decimal.Decimal(C[1][s])+decimal.Decimal(C[2][s]))**decimal.Decimal(a)
                   #C[3][s] = C[1][s]/(C[2][s] + 1)
                   #C[3][s] = 1 - C[2][s]/(2*C[1][s] + C[2][s])  
               C[1].pop(C[0].index(z))
               C[2].pop(C[0].index(z))
               C[3].pop(C[0].index(z))
               C[0].remove(z)
               #print("after node deletion=",C) 
                                         
   return C

def negative_weight(G,edg,edges_n,C,graph_df,i,anchor,a,data=True): 
    queue=[]
    if G.has_edge(graph_df.loc[i,"node1"],graph_df.loc[i,"node2"]):
      Dw=-G[graph_df.loc[i,"node1"]][graph_df.loc[i,"node2"]]['weight']
      G.remove_edge(graph_df.loc[i, "node1"], graph_df.loc[i, "node2"])
      l=[]
      if graph_df.loc[i,"node1"] in C[0]:
             l.append(C[0].index(graph_df.loc[i,"node1"]))
      if graph_df.loc[i,"node2"] in C[0]:
             l.append(C[0].index(graph_df.loc[i,"node2"]))
       
      l.sort()
      if len(l) != 0:
          edges_n[0] += 1
          if graph_df.loc[i,"node1"] in C[0] and graph_df.loc[i,"node2"] in C[0]:
          #print(C[0].index(graph_df.loc[i,"node1"]))
           for j in range(l[0],l[1]): 
            C[2][j]=C[2][j]+Dw
            C[3][j] = (2*C[1][j] + 1)/(2*C[1][j]+C[2][j])**a
            #C[3][j] = C[1][j]/(C[2][j] + 1)
            #C[3][j] = 1 - C[2][j]/(2*C[1][j] + C[2][j])              
           for p in range(l[1],len(C[0])): 
            C[1][p]=C[1][p]+Dw
            C[3][p] = (2*C[1][p] + 1)/(2*C[1][p]+C[2][p])**a
            #C[3][p] = C[1][p]/(C[2][p] + 1)
            #C[3][p] = 1 - C[2][p]/(2*C[1][p] + C[2][p])
           #print("update =",C)
          elif graph_df.loc[i,"node1"] in C[0] or graph_df.loc[i,"node2"] in C[0]:   
           for q in range(l[0],len(C[0])):
            C[2][q]=C[2][q]+Dw
            if C[2][q]==0 and C[1][q]==0:
               C[3][q] = 0
            else:   
               C[3][q] = (2*C[1][q] + 1)/(2*C[1][q]+C[2][q])**a
              #C[3][q] = C[1][q]/(C[2][q] + 1)
              #C[3][q] = 1 - C[2][q]/(2*C[1][q] + C[2][q])
          if graph_df.loc[i,"node1"] in C[0] and graph_df.loc[i,"node2"] in C[0]: 
               queue.append(C[0][l[1]])
          queue = list(dict.fromkeys(queue))
          while len(queue) > 0:
             z=queue.pop(0)              
             if z in C[0] and C[3][C[0].index(z)-1] >= C[3][C[0].index(z)]:
             #if z in C[0] and C[3][C[0].index(z)-1] <= C[3][C[0].index(z)]:    
                 for g in G.neighbors(z):
                  # print(g)  
                   if g in C[0] and C[0].index(g) > C[0].index(z):
                     queue.append(g)
                     queue = list(dict.fromkeys(queue))
                     for d in range(C[0].index(g),len(C[0])):                    
                            C[1][d] = C[1][d] - G[g][z]['weight']
                            C[2][d] = C[2][d] + G[g][z]['weight']          
                   elif g in C[0] and C[0].index(g) < C[0].index(z):
                         
                       for a in range(C[0].index(z)+1,len(C[0])):
                           C[1][a] = C[1][a] - G[g][z]['weight']
                           C[2][a] = C[2][a] + G[g][z]['weight']    
                   elif g not in C[0]:
                         
                       for v in range(C[0].index(z)+1,len(C[0])):
                           C[2][v] = C[2][v] - G[g][z]['weight']  
                 for s in range(0,len(C[0])):
                     
                     C[3][s] = (decimal.Decimal(2)*decimal.Decimal(C[1][s]) + decimal.Decimal(1))/(decimal.Decimal(2)*decimal.Decimal(C[1][s])+decimal.Decimal(C[2][s]))**decimal.Decimal(a)
                     #C[3][s] = C[1][s]/(C[2][s] + 1)
                     #C[3][s] = C[2][s]/(2*C[1][s] + C[2][s])  
                 C[1].pop(C[0].index(z))
                 C[2].pop(C[0].index(z))
                 C[3].pop(C[0].index(z))
                 C[0].remove(z) 
    return C