import divination
import gallow

print('-----------------')
print('Choose the game')
print('-----------------')
game = 0

while (game != 1 and game !=2):
	game = int(input("(1)- Gallow, (2)- Divination: "))
	
if (game == 1):
	gallow.play()
elif(game == 2):
	divination.play()