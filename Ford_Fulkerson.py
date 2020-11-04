def caminho(n):
    global p,topo
    p[topo]=n
    topo=topo+1
    
def iniciar_vetor():
    global visitado
    for i in range(tam):
        visitado[i]=0

def DFS_Adaptado(s,t):
    global visitado, grafoResidual,caminho,topo
    visitado[s]=1
    for i in range(tam):
        if ((grafoResidual[s][i]>0)and(visitado[i]==0)):
            visitado[i]=1
            caminho(i)
            if i!=t:
                vetorAux=visitado
                a=DFS_Adaptado(i,t)
                if a==True:
                    return True
                else:
                    topo=topo-1
                    visitado=vetorAux
            else:
                return True
    return False

def caminhoAumentante(s,t):
    global topo,p
    topo=1
    p[0]=s
    iniciar_vetor()
    if DFS_Adaptado(s,t)==True:
        return True
    else:
        return False

def minimo():
    global grafoResidual,p, topo
    menor=grafoResidual[p[0]][p[1]]
    for i in range(1,topo-1):
        if grafoResidual[p[i]][p[i+1]]<menor:
            menor=grafoResidual[p[i]][p[i+1]]
    return menor

def Ford_Fulkerson(s,t):
    global grafoFluxo, grafoResidual, Fluxo, grafoCapacidade,p
    while (caminhoAumentante(s,t)):
        mini=minimo()
        Fluxo=Fluxo+mini
        for i in range(topo-1):
            grafoResidual[p[i]][p[i+1]]=grafoResidual[p[i]][p[i+1]]-mini
            grafoResidual[p[i+1]][p[i]]=grafoResidual[p[i+1]][p[i]]+mini
    return Fluxo            

arq = open('arquivo6.txt', 'r')
conteudo = arq.readlines()

Fluxo=0
grafoCapacidade=[]
grafoResidual=[]
tam=conteudo[0]
tam=int(tam)
visitado=[]
vetorAux=[]
p=[]
topo=0

for i in range(1,tam+1):
    grafoCapacidade += [ conteudo[i].split() ]
    grafoResidual+=[[]]
    visitado+=[0]
    p+=[0]

for i in range(tam):
    for x in range(tam):
        grafoCapacidade[i][x]=int(grafoCapacidade[i][x])
        grafoResidual[i]+=[0]
        if grafoCapacidade[i][x]!=-1:
            grafoResidual[i][x]=grafoCapacidade[i][x]
            if grafoCapacidade[x][i]==-1:
              grafoResidual[x][i]=0  

print(Ford_Fulkerson(0,tam-1))











