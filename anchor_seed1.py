from neighbors import all_neighbors


def find_anchor_community(G,C,a,data=True):
    edges = G.edges(data=True)
    dic = dict( (x[:-1], x[-1]['weight']) for x in edges if      'weight' in x[-1] )
    G_ins = sum(list(dic.values()))
    #print(C[0])
    low=C[3][-1]
    A=len(C[0])-1 
    while len(C[0]) > A: 
       O=[]
       I=[]
       K=[]
       B=[]
       takis=[]
       stas=[]
       l=[]
       for node in C[0]:
        takis=all_neighbors(G,node)
        l.extend(takis)
       stas = list(dict.fromkeys(l))
       for x in C[0]:
           if x in stas:
               stas.remove(x) 
       for y in stas:
        C[0].append(y)
        
        out=0
        ins=0
        kostas=[]
        #p=[]
        Bou=[]
        for u in C[0]:
          p=[]  
          kostas=all_neighbors(G,u)
          p.extend(kostas)
         #p = list(dict.fromkeys(p))
          
          for v in p:
                
            if v in C[0]:
                if u != v:
                   ins=ins+1/2*G[u][v]['weight']
                else:
                   ins=ins+G[u][v]['weight']
                   
            else:
                   
                    out=out+G[u][v]['weight']
                    if u not in Bou:
                     Bou.append(u)
        S = (2*ins+1)/(2*ins+out)**a
        #S = ins/(out+1)
        #S = (2*ins/len(C[0]))/(out/len(Bou))
        #S = out/(2*ins + out)
        #if S not in K and y not in B:    
        K.append(S)
        B.append(y)
        I.append(ins)
        O.append(out)
        C[0].remove(y)
       
       for o in range(len(K)):
           #print(K[i])
           if K[o] > low:
           #if K[o] < low:
             low = K[o]
             index = o   
       if low > C[3][-1]:
       #if low < C[3][-1]:
            C[3].append(low)
            C[0].append(B[index])
            C[1].append(I[index])
            C[2].append(O[index])
            #print("print index=",Y[index])
            A=A+1
            
       else:
            A=A+1
            
    
    return C
    

