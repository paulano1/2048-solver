import random
from board import GameBoard
from Matrix import Eval
#score 
#code for random
#generation of the key
class Game():
  def __init__(self):
    self.score = 0
    

  def randomGame(self):
    gameBoard = GameBoard(4)
    gameBoard.makeNewBoard()
    while gameBoard.checker():
      choices = gameBoard.possibleMoves()
      move = random.choice(list(choices))
      print(move)
      gameBoard.makeMove(move)
      gameBoard.generateRandomBlock()
      gameBoard.print()

  def playGame(self):
    gameBoard = GameBoard(4)
    gameBoard.makeNewBoard()
    while gameBoard.checker():
      move, maxvalue = self.expectimax(gameBoard)
      print(move)
      gameBoard.makeMove(move)
      gameBoard.generateRandomBlock()
      gameBoard.print()

  def zeroCounter(self,board, n=0):
    score = 0
    for col in board:
        score += col.count(n)
    return score

  def expectimax(self, state, isMaxTurn=True, currentDepth=0, maxDepth = 4):
    if currentDepth>maxDepth:
      if state.checker():
        eval = Eval(state.getBoard())
        return eval.getScore()
      else:
        return float('-inf')
    if isMaxTurn:
      maxValue = float('-inf')
      bestMove='na'
      for move in state.possibleMoves():
        newState = state.clone()
        newState.makeMove(move)
        moveValue = self.expectimax(newState, False, currentDepth+1)
        if moveValue>=maxValue:
          bestMove = move
          maxValue = moveValue
      if currentDepth == 0:
        return bestMove, maxValue
      return maxValue
    else:
      sum=0
      count=0
      for currentBoard in state.getAllRandomBlocks():
        newState = state.clone()
        newState.setBoard(currentBoard)
        sum+=self.expectimax(newState, True, currentDepth+1)
        count+=1
      if count != 0:
        return sum/count
      else:
        return 0










#Zero Counter
def zeroCounter(board, n=0):
    score = 0
    for col in board:
        score += col.count(n)
    return score
#Monotonicity
def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))








if __name__ == "__main__":
  game=Game()
  game.playGame()
    
    