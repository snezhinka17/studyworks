# -*- coding: utf-8 -*-
"""travelling salesman problem and roc auc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KeO6OEU9dgfxFglUq5UjYIB0x4MLPPsL
"""

graph_main = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
        [4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
        [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
        [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
        [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
        [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ]

# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 12
results= []
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    iter_cnt=0

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    next_permutation=permutations(vertex)
    for i in next_permutation:
          iter_cnt += 1
        # store current Path weight(cost)
          current_pathweight = 0

        # compute current path weight
          k = s
          for j in i:
            current_pathweight += graph[k][j]
            k = j
          current_pathweight += graph[k][s]
        # update minimum
          min_path = current_pathweight
          if min_path >= 72:
            results.append(min_path)
          #output = print(min_path, iter_cnt, i) if min_path >=72 else ''
    return len(results)
# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = graph_main

    s = 0
    print(travellingSalesmanProblem(graph, s))

from sklearn.metrics import roc_auc_score

# Истинные значения и предсказанные вероятности
true_labels = [1, 0, 0, 1, 1, 1, 0, 0, 0, 1]
predicted_probabilities = [1,1,1,1,1,1,0,0,0,0]

# Вычисление ROC AUC
roc_auc = roc_auc_score(true_labels, predicted_probabilities)

print(f"ROC AUC: {roc_auc}")

"""# https://pythonhelp.ru/python/kak-poschitat-roc-auc-python/?ysclid=lpmosv8i7n918037022"""