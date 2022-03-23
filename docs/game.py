from sys import exit, argv
from random import randint

if len(argv) > 1:
	script, name = argv
else:
	name = input("What is your name?\n>")

class Scene(object):
	def enter(self):
		print("This scene is not yet configured.")
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		final_scene = self.scene_map.next_scene('finished')

		while current_scene != final_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter()

class Death(Scene):
	reasons = [
		"Death's a bitch",
		"Hehe",
		"Welcome to heaven"
	]

	def enter(self):
		print(Death.reasons[randint(0, len(self.reasons)-1)])
		exit(1)

class BunkerRoom(Scene):
	def enter(self):
		print(f"Hello {name}! You've woken up in the Winchester Bunker.\nIt's probably a dream so the timelines won't make sense here.")

		while True:
			answer = input("What do you do next?\n>")
			
			if "find dean" or "find sam" in answer.lower():
				print("OK {}, let's go find the boys".format(name))
				break
			elif "open door" in answer.lower():
				print("OK {}, let's go explore".format(name))
				break
			else:
				print("I didn't catch that.")
			print("I don't know what you want") 

		print("The door opens. Do you go left or right?")
		answer = input("> ")
		if 'l' in answer.lower():
			return 'kitchen_scene'
		else:
			return 'kitchen_scene'

class KitchenScene(Scene):
	def enter(self):
		print(f"So, {name}, you find yourself in the kitchen.")
		print("Dean is hogging all the food! What do you do?")

		Dean_stopped = False
		while True: 
			solution = input("> ")
			if "other food" in solution:
				print("Where? Dean's eating it!")
			elif "distract" in solution:
				print("Good idea!")
				Dean_stopped = True
			elif "steal" in solution and Dean_stopped == True:
				print("Tada! Well done")
				return 'library'
			elif "steal" in solution and Dean_stopped == False:
				reason = "Dean punches you. Hard."
				return 'death'
			elif "go hungry" in solution:
				reason = "You gave up"
				return 'death' 
			else:
				print("Didn't work")
class Library(Scene):
	def enter(self):
		print(f"So {name}, you find Sam in the library researching the lore.")
		print("He's stuck - who should he call?\nBobby?\nCass\nCrowley?")

		while True:
			call = input("> ")
			voicemails = {"bobby" : "idjit! I'm busy", 
				"cass" : "you have reached my voicemail, make your voice a mail",
				"john" : "if this is an emergency, call my son Dean",
				"rowena" : "oh boys",
				"dean": "leave your name, number and nightmare at the tone."
				}
			if call in voicemails:
				print(voicemails.get(call))
			else:
				return 'dungeon'

class Dungeon(Scene):
	def enter(self):
		print(f"So {name}, you're now in the dungeon")
		print("Sam has tied the monster to the chair.")
		print("What do you use?")
		print("A. Holy Water \nB. Silver \n C.Angel Blade \nD. Witch Killing Bullets")

		def monsters():
			value = randint(0,10)
			if value > 7: 
				monster = "demon"
			elif value > 3:
				monster = "shifter"
			else: 
				monster = "witch"
			return monster 

		monster = monsters() 
		while True:
			decision = input("> ")
			rules = [
				decision.lower() == 'a' and monster == 'demon',
				decision.lower() == 'd' and monster == 'witch',
				decision.lower() == 'b' and monster == 'shifter',
				decision.lower() == 'c'
				]
		
			if any(rules):
				print("Well done")
				return 'metatron'
			elif "reset" in decision:
				monster = monsters()			
			else:
				print("lol that did nothing!") 


class Metatron(Scene):
	def enter(self):
		print("Metatron is back! How do you catch him?")
		count = 0 

		while True:
			answer = input("> ").lower()
			answer = ["holy oil" in answer, "devils trap" in answer, "enochian handcuffs" in answer, "grace" in answer]
			responses = {"holy oil"  : "10/10, interrogate him!",
				"devils trap" : "Whoops wrong one. Now you're dead.",
				"enochian handcuffs" : "Nerd",
				"grace" : "You need an angel"
				}
			outcomes = {"holy oil"  : 'finished',
				"devil's trap" : "death",
				"enochian handcuffs" : "finished",
				"grace" : "0"
				}

			if any(answers):
				print(responses.get(answer))
				if outcomes.get(answer)!= 0:
					return	 outcomes.get(answer)
			elif count < 3:
				print("Try again!")
				count += 1
			else:
				return 'death'
				
class Finished(Scene):
	def enter(self):
		print("You won! Congrats!")
		return 'finished'

class Map(object):
	scenes = {'bunker_room' : BunkerRoom(),
		'kitchen_scene' : KitchenScene(),
		'death': Death(),
		'finished': Finished(),
		'library' : Library(),
		'dungeon' : Dungeon(),
		'metatron': Metatron()
		}
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('bunker_room')
a_game = Engine(a_map)
a_game.play()
