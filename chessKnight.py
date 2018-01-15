import numpy as np

def IndiceCavalo(pos):
    valInd = []
    for i in range(8):
        for j in range(8):
            if mtx[i,j]==pos:
                valInd.append((i,j))
                break
    return valInd


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

def DefinePosKnight(matrix, coordTupla):
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
                    matrix[i, j] = '@@_'
                    break

    return matrix


y = ['a','b','c','d','e','f','g','h']
x = [8,7,6,5,4,3,2,1]

temp = [(str(i) + j) for i in x for j in y]

mtx = np.asmatrix(temp).reshape(8,8)

print('\n {} \n'.format(mtx))
input_user = str(input('Veja o tabuleiro e escolha qual a coordenada do cavalo? '))
pos = IndiceCavalo(input_user)

result = FindPosKnight(mtx, pos)
new_matrix = DefinePosKnight(mtx, pos)



print('\nEstas são as possíveis jogadas no tabuleiro {} para a posição escolhida {}\n'.format(result,input_user))
print('\n Veja no tabuleiro como ficou as possíveis jogadas identificadas como @@. \n')
print(new_matrix)