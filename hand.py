class Game:
	def __init__(self):
		self.usScore = int(0)
		self.themScore = int(0)


def gameScore(handScore):
	if handScore < 0:
		if gameOne.themScore > 0:
			print("Second")
			print("Game1 ",gameOne.themScore)
			print("Game2 ",gameTwo.themScore)
			print()
			gameOne.themScore = (handScore * -1) + gameOne.themScore
			gameTwo.themScore = (handScore * -1) + gameTwo.themScore
			return gameTwo.themScore, gameOne.themScore
		else:
			print("First")
			gameOne.themScore = (handScore * -1) + gameOne.themScore
			return gameOne.themScore
	else:
		if gameOne.usScore > 0:
			gameOne.usScore =+ handScore
			gameTwo.usScore =+ handScore
		else:
			gameOne.usScore =+ handScore


gameOne = Game()
gameTwo = Game()

handScore = -10
gameScore(handScore)
print(gameOne.themScore)
print(gameTwo.themScore)
handScore = -20
gameScore(handScore)
print()
print(gameOne.themScore)
print(gameTwo.themScore)