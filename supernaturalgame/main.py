from sys import exit, argv
from random import randint
from classes import *

if len(argv) > 1:
	script, name = argv
else:
	name = input("What is your name?\n>")

class Map(object):
	scenes = {'bunker_room_scene' : BunkerRoom(),
		'kitchen_scene' : KitchenScene(),
		'death': Death(),
		'finished': Finished(),
		'library_scene' : Library(),
		'dungeon_scene' : Dungeon(),
		'metatron_scene': Metatron()
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('bunker_room_scene')
a_game = Engine(a_map, name)
a_game.play(name)
