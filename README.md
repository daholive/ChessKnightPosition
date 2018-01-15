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
```
import numpy as np
```

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

