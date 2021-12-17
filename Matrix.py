import math

class Eval():
    def __init__(self, board):
        self.__board = board
        self.__size = len(board[0])
        self.__smooth = self.smoothness(0.0204)
        self.__mono = self.mono(0.204)
        self.__maxVal = self.maxval(0.204)
        self.__empty = self.empty(0.551)
    
    def getSmooth(self):
        return self.__smooth
    def getMono(self):
        return self.__mono
    def getEmpty(self):
        return self.__empty
    def getMax(self):
        return self.__maxVal

    def getScore(self):
        return(self.__mono + self.__empty)

    def non_increasing(self, row):
      return all(x>=y for x, y in zip(row, row[1:]))

    def non_decreasing(self, row):
      return all(x<=y for x, y in zip(row, row[1:]))
    
    def monotonic(self, row):
      return self.non_increasing(row) or self.non_decreasing(row)

    def ab(self, v1,v2):
      return abs(v1 - v2)
      
    def transpose(self, board):
	    return [list(row) for row in zip(*board)]
    
    def mono(self, weight):
      m = [0] * self.__size
      best = self.__size * 2
      for i in range(self.__size):
        if self.monotonic(self.__board[i]):
          m[i] += 1
      b = self.transpose(self.__board)
      for j in range(self.__size):
        if self.monotonic(b[j]):
          m[j]+=1
      return (sum(m)/best)*weight
 
    def max(self, dis):
        pass
    def maxval(self, weight):
        val = max(max(self.__board, key=max))
        if val != 0:
            return (math.log(val)/math.log(2))*weight
        return 0

    def empty(self, weight):
        score = 0
        best = self.__size * self.__size
        for col in self.__board:
            score += col.count(0)
        if score != 0:
            return (score/best) * weight
        return 0
    
    def smoothness(self, weight):
      sum = 0
      for i in range(len(self.__board)):
        for j in range(len(self.__board)):
          if i-1>=0:
            sum += abs(self.__board[i][j] - self.__board[i-1][j])
          if j-1>=0:
            sum += abs(self.__board[i][j] - self.__board[i][j-1])
      #print(sum)
      return (-sum/)

'''board = [[128,64,32],            
        [64,256,8],         
        [32,16,4],
        [16,8,2]]'''




