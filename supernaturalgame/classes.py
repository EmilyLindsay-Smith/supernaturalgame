from random import randint

class Scene(object):
	def enter(self, name):
		print("This scene is not yet configured.")
		exit(1)

class Engine(object):
	def __init__(self, scene_map, name):
		self.scene_map = scene_map

	def play(self, name):
		current_scene = self.scene_map.opening_scene()
		final_scene = self.scene_map.next_scene('finished')

		while current_scene != final_scene:
			next_scene_name = current_scene.enter(name)
			current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter(name)

class Death(Scene):
	quips = [
		"Death's a bitch",
		"Welcome to Hell",
		"Welcome to The Empty",
		"Welcome to Heaven",
		"Welcome to Purgatory"
		]

	def enter(self, name):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)

class BunkerRoom(Scene):
	def enter(self, name):
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
			return 'library_scene'

class KitchenScene(Scene):
	def enter(self, name):
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
				return 'library_scene'
			elif "steal" in solution and Dean_stopped == False:
				print("Dean punches you. Hard.")
				print("Your heart gives you")
				return 'death'
			elif "go hungry" in solution:
				print("You gave up, so you die of starvation unable to think of alternative solutions.")
				return 'death' 
			else:
				print("Didn't work")
class Library(Scene):
	def enter(self, name):
		print(f"So {name}, you find Sam in the library researching the lore.")
		print("He's stuck - who should he call?\nBobby?\nCass\nCrowley\nJohn\nRowena\nDean?")

		while True:
			call = input("> ").lower()
			voicemails = {"bobby" : "idjit! I'm busy", 
				"cass" : "you have reached my voicemail, make your voice a mail",
				"john" : "if this is an emergency, call my son Dean",
				"rowena" : "oh boys",
				"dean": "leave your name, number and nightmare at the tone."
				}
			if call in voicemails:
				print(voicemails.get(call))
				print("That didn't help, who's next?")
			else:
				print("I've found the monster, I'll bring him to your dungeon")
				return 'dungeon_scene'

class Dungeon(Scene):

	def enter(self, name):
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
				decision.lower() == 'a' or 'holy water' and monster == 'demon',
				decision.lower() == 'd' or 'witch killing bullets' and monster == 'witch',
				decision.lower() == 'b' or 'silver' and monster == 'shifter',
				decision.lower() == 'c' or 'angel blade'
				]
		
			if any(rules):
				print("Well done")
				return 'metatron_scene'
			elif "reset" in decision:
				monster = monsters()			
			else:
				print("lol that did nothing!") 


class Metatron(Scene):
	def enter(self, name):
		print("Metatron is back! How do you catch him?")
		print("If you're stuck, say 'clue'")
		count = 0 

		while True:
			answer = input("> ").lower().replace("'", "")
			answers = ["holy oil" in answer, "devils trap" in answer, "enochian handcuffs" in answer, "grace" in answer, "clue" in answer]
			responses = {"holy oil"  : "10/10, interrogate him!",
					"devils trap" : "Whoops wrong one. Now you're dead.",
					"enochian handcuffs" : "Nerd",
					"grace" : "You need an angel",
					"clue" : "Have you forgotten the options? Here they are:\nHoly Oil\nDevils Trap\nEnochian Handcuffs\n Grace"
					}
			outcomes = {"holy oil"  : 'finished',
					"devils trap" : "death",
					"enochian handcuffs" : "finished",
					"grace" : "0",
					"clue" : "0", 
					}

			if any(answers):
				print(responses.get(answer))
				if outcomes.get(answer)!= "0":
					return	 outcomes.get(answer)
				elif count < 3:
					print("Try again!")
					count += 1
				else:
					print("Devil's traps are for DEMONS not angels. Metatron gets out easily and kills you")
					return 'death'
			else:
				print("Try again!")
				
class Finished(Scene):
	def enter(self, name):
		print("You won! Congrats!")
		return 'finished'
