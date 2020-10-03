import pygame

# Starting the mixer 
pygame.mixer.init() 

# Loading the song 
pygame.mixer.music.load("song.mp3") 

# Setting the volume 
pygame.mixer.music.set_volume(0.7) 

# Start playing the song 
pygame.mixer.music.play() 

# infinite loop 
while True: 
	
	print("Press 'p' to pause, 'r' to resume") 
	print("Press 'e' to exit the program") 
	query = input(" ") 
	
	if query == 'p': 

		# Pausing the music 
		pygame.mixer.music.pause()	 
	elif query == 'r': 

		# Resuming the music 
		pygame.mixer.music.unpause() 
	elif query == 'e': 

		# Stop the mixer 
		pygame.mixer.music.stop() 
		break
