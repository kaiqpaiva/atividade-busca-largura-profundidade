# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""
# Grafo como uma lista de adjacência
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m-=1
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )

    def dfs(self, v, visitados=None, profundidade=0):
        if visitados is None:
            visitados = []
        print("  " * profundidade + f"visitando {v}")
        visitados.append(v)
        for w in self.listaAdj[v]: # passa pelos vizinho w do vertice atual
            if w not in visitados: # verifica se já não foi visitado
                self.dfs(w, visitados, profundidade + 1) # chama a recursão para descer mais
        return visitados

    def bfs(self, v):
        visitados = [v]
        fila = [(v, 0)]
        ordem = []
        while fila:
            atual, nivel = fila.pop(0)
            print(" " * nivel + f"visitando {atual}")
            ordem.append(atual)
            for w in self.listaAdj[atual]: # passa pelos vizinho w do vertice atual
                if w not in visitados: # verifica se já não foi visitado
                    visitados.append(w)  # coloca o w na lista de visitados
                    fila.append((w, nivel + 1)) # coloca ele na fila
        return ordem