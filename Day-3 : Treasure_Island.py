print('''    
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'    ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1=input("You are at a cross road. Which way do you want to go? left or right").lower()
if input1 == 'left':
	print("You have come to a lake. There is an island in the middle of the lake.")
	input2=input("Type 'wait' to wait for a boat or 'swim' to swim across").lower()
	if input2=='wait':
		print('you have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue.')
		input3=input('which colour do you choose?').lower()
		if input3=='red':
			print("It is a room full of fire. Game over.")
		elif input3=='yello':
			print("You found the treasure! You win!")
		else:
			print("You enter a room full of beasts. Game over.")
	else:
		print("you have been attacked by a sea monstor. Game over.")
else:
	print("You fell into a hole. Game over") 
