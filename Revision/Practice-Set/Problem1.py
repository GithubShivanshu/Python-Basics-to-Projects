from playsound3.playsound3 import playsound
# playsound module is used to play audio files/mp3 files in python.
print("Playing your audio now... 🎧")

# ''' ''' is used to print multi-line strings in python.
print('''Yeah, you can be the greatest, you can be the best
You can be the King Kong bangin' on your chest
You can beat the world, you can win the war
You can talk to God, go banging on his door
You can throw your hands up, you can beat the clock
You can move a mountain, you can break rocks
Some will call that practice, some will call that luck
But either way you're going to the history books
Standing in the Hall of Fame
And the world's gonna know your name
'Cause you burn with the brightest flame
And the world's gonna know your name
And you'll be on the walls of the Hall of Fame
You can go the distance, you can run a mile
You can walk straight through hell with a smile
You can be a hero, you can get the gold
Breaking all the records they thought would never be broke
Yeah, do it for your people, do it for your pride
Are you ever gonna know if you never even try?
Do it for your country, do it for your name
'Cause there's gonna be a day when you're
Standing in the Hall of Fame
And the world's gonna know your name
'Cause you burn with the brightest flame
And the world's gonna know your name
And you'll be on the walls of the Hall of Fame
You'll be on the walls of the Hall of Fame
Be students, be teachers
Be politicians, be preachers, yeah (yeah)
Be believers, be leaders
Be astronauts, be champions
Be truth seekers
Be students, be teachers
Be politicians, be preachers, yeah (yeah)
Be believers, be leaders
Be astronauts, be champions
Standing in the Hall of Fame
And the world's gonna know your name
'Cause you burn with the brightest flame (oh-oh)
And the world's gonna know your name
And you'll be on the walls of the Hall of Fame
Yeah, you can be the greatest, you can be the best
You can be the King Kong bangin' on your chest
You can beat the world, you can win the war
You can talk to God, go bangin' on his door
You can throw your hands up, you can beat the clock
You can move a mountain, you can break rocks
Some will call it practice, some will call that luck
But either way you're going to the history books
Standing in the Hall of Fame''')

# try and except block is used to handle exceptions in python.
try:
 playsound("Revision/Practice-Set/HallOfFame.mp3") # download the mp3 file from the internet and place it in the same directory as this python file to play the audio.
except KeyboardInterrupt:  # KeyboardInterrupt is used to handle the exception when the user interrupts the program using Ctrl+C.
 print("\n🎵 Music stopped. Have a great day!")