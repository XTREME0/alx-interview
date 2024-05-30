#!/usr/bin/python3
""" Pascal Triangle gen """


class pascal_triangle:
    """ pascall class """

    def __init__(self, n=0):
        self.n = n
        self.tri = []

    def trigen(self):
        nxt = []
        if self.n <= 0:
            return [[]]

        for i in range(self.n):
            if i == 0:
                self.tri.append([1])
            elif i == 1:
                self.tri.append([1, 1])
                nxt = [1, 2, 1]
            else:
                self.tri.append(nxt)
                nxt = [1]
                for j in range(1, len(self.tri[i])):
                    nxt.append(self.tri[i][j] + self.tri[i][j-1])
                nxt.append(1)
        return self.tri
    
    def __iter__(self):
        return iter(self.trigen())

