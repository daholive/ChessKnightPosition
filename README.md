Chess Board - Finding out knight moves - Solução para o Algoritmo
=============
O Problema
-----------
Some context on chess
A chessboard is the type of checkerboard used in the board game chess, consisting of 64
squares (eight rows and eight columns). The squares are arranged in two alternating colors
(light and dark). https://en.wikipedia.org/wiki/Chessboard

A chessboard generally use Algebraic notation , basically rows are marked 1 to 8 from
bottom to top and columns a to h from left to right. With that players can make a move using
coordinates.
The knight (♘ ♞ /ˈnaɪt/) is a piece in the game of chess, representing a knight (armored
cavalry). It is normally represented by a horse's head and neck. It moves to a square that is
two squares away horizontally and one square vertically, or two squares vertically and one
square horizontally. The complete move therefore looks like the letter L.

Challenge
Given a knight located on a coordinate chosen by the user find out all possible locations
where the knight can move in 2 turns.
You are expected to build a web application and an API.


Importando a biblioteca numpy para manipulação de matrizes
----------------------------------------------------------
```
import numpy as np
```

Função para determinar a posição do cavalo no tabuleiro
-------------------------------------------------------
```
def IndiceCavalo(pos):
    valInd = []
    for i in range(8):
        for j in range(8):
            if mtx[i,j]==pos:
                valInd.append((i,j))
                break
    return valInd
```

Função para determinar as possíveis jogadas com o cavalo
--------------------------------------------------------
```
def FindPosKnight(matrix, coordTupla):
    x = coordTupla[0][0]
    y = coordTupla[0][1]
    valInd = []

    for dXY in [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]:
        ResX = x - dXY[0]
        RexY = y - dXY[1]
        NewTpl = (x, y)

        for i in range(8):
            for j in range(8):
                if i == ResX and j == RexY:
                    valInd.append(matrix[i, j])
                    break

    return valInd
```
