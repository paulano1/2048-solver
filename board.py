import random
import copy

random.seed(100)

class GameBoard():
  def __init__(self, size: int, board=None):
    self.__size = size
    self.__score = 0
    self.__won = False
    if board:
      self.__board = board
    else:
      self.__board = [[0 for i in range(self.__size)] for j in range(self.__size)]
  
  def getGen(self):
    return self.__gen
  
  def getSize(self):
    return self.__size

  def getBoard(self):
    return self.__board
  
  def setBoard(self, board):
      self.__board = board
  def __eq__(self, other) -> bool:
    board = self.getBoard()
    other = self.getBoard()
    
    for i in range(board):
        for j in range(other):
            if board[i][j] != other[i][j]:
                return False
    return True
  
  def clone(self):
    return GameBoard(self.__size, copy.deepcopy(self.__board))

  def print(self):
    for i in range(self.__size):
      print(self.__board[i])
  
  def getRandomBlockNumber(self):
    chance = random.random()
    return 2 if chance<=0.9 else 4
    
  def generateRandomBlock(self):
    possibleOptions = []
    for i in range(self.__size):
      for j in range(self.__size):
        if self.__board[i][j] == 0:
          possibleOptions.append((i,j))
    if len(possibleOptions):
      row,col = random.choice(possibleOptions)
      self.__board[row][col] = self.getRandomBlockNumber()
      return row,col

  

  def getAllRandomBlocks(self):
    allPossible=[]
    for i in range(self.__size):
      for j in range(self.__size):
        if self.__board[i][j] == 0:
          newBoard1 = copy.deepcopy(self.__board)
          newBoard2 = copy.deepcopy(self.__board)
          newBoard1[i][j] = 2
          newBoard2[i][j] = 4
          allPossible.append(newBoard1)
          allPossible.append(newBoard2)
    return allPossible

    
  def reset(self):
    self.setboard([[0 for i in range(self.__size)] for j in range(self.__size)])

  def makeNewBoard(self):
      self.generateRandomBlock()
      self.generateRandomBlock()

  def transpose(self):
	  return [list(row) for row in zip(*self.getBoard())]
  
  def shiftReverse(self,nums):
    prev = None
    store = []

    for next_ in nums:
        if not next_:
            continue
        if prev is None:
            prev = next_
        elif prev == next_:
            store.append(prev + next_)
            prev = None
        else:
            store.append(prev)
            self.__score += prev + next_
            prev = next_
    if prev is not None:
        store.append(prev)
    
    store.extend([0] * (len(nums) - len(store)))
    return store

  def shift(self,nums):
    prev = None
    store = []

    for next_ in nums:
        if not next_:
            continue
        if prev is None:
            prev = next_
        elif prev == next_:
            store.append(prev + next_)
            self.__score += prev + next_
            prev = None
        else:
            store.append(prev)
            prev = next_
    if prev is not None:
        store.append(prev)
    l = [0] * (len(nums) - len(store))
    l.extend(store)
    return l
  

  def rotate(self):
    self.__board = [ list(e) for e in zip(*self.__board)]
  
  def makeUpMove(self):
    board=[]
    self.rotate()
    for row in range(self.__size):
      board.append(self.shiftReverse(self.__board[row]))
    self.__board = board
    self.rotate()

  def makeDownMove(self):
    board=[]
    self.rotate()
    for row in range(self.__size):
      board.append(self.shift(self.__board[row]))
    self.__board = board
    self.rotate()

  def makeLeftMove(self):
    for row in range(self.__size):
        self.__board[row] = self.shiftReverse(self.__board[row])

  def makeRightMove(self):
    for row in range(self.__size):
      self.__board[row] = self.shift(self.__board[row])



  def possibleMoves(self):
    pmoves = set()
    for i in range(0,self.__size):
      for j in range(0,self.__size):
        target = self.__board[i][j]
        if i == 0 and j == 0 and target == 0:
          pmoves.add('u')
          pmoves.add('l')
        elif i==self.__size-1 and j == 0 and target == 0:
          pmoves.add('d')
          pmoves.add('l')
        elif i==self.__size-1 and j == self.__size-1 and target == 0:
          pmoves.add('d')
          pmoves.add('r')
        elif i==0 and j == self.__size-1 and target == 0:
          pmoves.add('u')
          pmoves.add('r')
        elif i in [0,self.__size-1] and j in [0,self.__size-1]:
          continue
        elif target == 0:
          return {'u','l','r','d'}
        elif (j-1 >=0 and target == self.__board[i][j-1]) or (j+1<self.__size and target == self.__board[i][j+1]):
          pmoves.add('l')
          pmoves.add('r')
        elif (i-1 >=0 and target == self.__board[i-1][j]) or (i+1<self.__size and target == self.__board[i+1][j]):
          pmoves.add('u')
          pmoves.add('d')
    return pmoves
      
  def checker(self):
    board = self.getBoard()
    for i in range(0,self.__size):
        for j in range(self.__size -1):
          if board[i][j] == board[i][j+1]:
            return True
          if board[i][j] == 0:
            return True

    for i in range(self.__size-1):
      for j in range(self.__size):
        if board[i+1][j] == board[i][j]:
            return True
    return False
  
  def makeMove(self, move):
    if move == 'u':
      self.makeUpMove()
      self.generateRandomBlock()
    elif move == 'd':
      self.makeDownMove()
      self.generateRandomBlock()
    elif move == 'r':
      self.makeRightMove()
      self.generateRandomBlock()
    elif move == 'l':
      self.makeLeftMove()
      self.generateRandomBlock()

if __name__ == "__main__":
    size = int(input("enter size: "))
    g = GameBoard(size)
    print(g.shiftReverse([2,2,4,8]))
    g.makeNewBoard()
    '''
    g.print()
    L = True
    while L:
        move = input('enter move')
        g.makeMove(move)
        g.print()
'''