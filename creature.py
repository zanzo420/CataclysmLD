# defines base creature in the base. all monsters, players, npcs, and critters derive from this.
from collections import defaultdict
from bodypart import Bodypart
class Creature:
    def __init__(self):
        self.stats = defaultdict(dict)
        self.stats['strength']['base'] = 10
        self.stats['strength']['max'] = 20
        self.stats['dexterity']['base'] = 10
        self.stats['dexterity']['max'] = 20
        self.stats['intelligence']['base'] = 10
        self.stats['intelligence']['max'] = 20
        self.stats['perception']['base'] = 10
        self.stats['perception']['max'] = 20
        self.stats['constitution']['base'] = 10
        self.stats['constitution']['max'] = 20
        self.known_recipes = [] # known_recipes[0] = Recipe(ident, favorite) -  pull full recipe info from RecipeManager['ident'] - NPCs may know recipes that's why its in Creature
        self.command_queue = [] # what each creature wants to do this turn and the upcoming turns. contains a list of Action(s) that are processed by the server.
        self.gender = 'male'
        self.radiation = 0 # radiation level. hurts some helps others.
        self.name = None # is optional
        self.affected_by = [] #TODO: create afflictions.
        self.in_vehicle = False # other wise have a reference to the vehicle it's in.
        self.controlling_vehicle = False
        self.possible_actions = ['move', 'attack', 'sneak', 'craft', 'activate', 'wear', 'remove', 'reload'] # what is this creature able to do?
        self.actions_per_turn = 1 # actions per turn (per second). (moving 5 ft a second is average walking speed)
        self.next_action_available = 0 # how many turns until we can take an action. if this is greater then 0 subtract 1 per turn until 0. add to this per action.
        self.hallucination = False # set True for no_clip, does_no_damage, chase_creature
        self.tile_id = 1706 # base tile_id for new creatures.
        self.dodges_per_turn = 0
        self.blocks_per_turn = 0
        self.move_mode = 'walk' # 'walk', 'run', 'sneak'

        # list of body parts this creature has. normal human has 2 arms, 2 hands, 2 legs, torso, head, and 2 feet. head and torso are both vital organs.
        # body_parts are where items get equipped.
        self.body_parts = [Bodypart('HEAD', False), Bodypart('TORSO', False), Bodypart('ARM'), Bodypart('ARM'), Bodypart('LEG'), Bodypart('LEG'), Bodypart('FOOT'), Bodypart('FOOT'), Bodypart('HAND'), Bodypart('HAND')]
        self.items_held = [] # a special location that acts as a container for moving items between positions, equipped, and not in containers.
