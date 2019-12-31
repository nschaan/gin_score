class Game:
	def __init__(self):
		self.usScore = 0
		self.themScore = 0


def gameScore(total, handScore):
	total = total + handScore
	return(total)

gameOne = Game()
handScore = -10
gameOne.themScore = gameScore(gameOne.themScore, handScore)
print(gameOne.themScore)
handScore = -20
gameOne.themScore = gameScore(gameOne.themScore, handScore)
print(gameOne.themScore)