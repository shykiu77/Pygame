import sys
import copy
BLACK = 0
WHITE = 1
NONE = -1
MAXDEPTH = 3

class Node:
    def __init__(self,pattern,parent,children,turn):
        self.pattern = pattern
        self.parent = parent
        self.children = children
        self.turn = turn
        self.score = None
    

def printBoard(board):
    for i in range(0,8):
        for j in range(0,8):
            print("board[" + str(i) + "]["+ str(j) + "] = ",end = '')
            if board[i][j] == BLACK:
                print("BLACK")
            elif board[i][j] == WHITE:
                print("WHITE")
            else: 
                print("None")

def GenerateMoves(board,turn,parent):
    moves = []
    for i in range(0,3):
        moves.append(Node(copy.deepcopy(board),parent,[],turn))
    return moves

def GenerateTree(node,depth):
    if depth > MAXDEPTH:
        return
    node.children = GenerateMoves(node.pattern,BLACK if depth%2 == 0 else WHITE,node)
    for element in node.children:
        GenerateTree(element,depth+1)

def heuristica(board):
    whites = 0
    blacks = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == BLACK:
                blacks += 1
            if board[i][j] == WHITE:
                whites += 1
    return whites - blacks

def DFS(node):
    if node.children == []:
        node.score = heuristica(node.pattern)
        return node.score
    


def main():
    board = []
    for i in range(0,8):
        column = []
        for j in range(0,8):
            if j <= 2 and (i+j)%2 != 0:
                column.append(WHITE)
            elif j >= 5 and (i+j)%2 != 0:
                column.append(BLACK)
            else:
                column.append(None)
        board.append(column)
    root = Node(board,None,[],WHITE)
    GenerateTree(root,0)
    DFS(root)
if __name__ == '__main__':
    main()
