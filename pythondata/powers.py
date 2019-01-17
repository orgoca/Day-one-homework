#	Ruha Toby and Carlos

#    Reads superheroes.json (in this folder)

import json

from pprint import pprint

with open('superheroes.json', 'r') as f:
	squad = json.load(f)

#    Creates an empty array called powers

allpowers = []

#    Loop thorough the members of the squad, and append the powers of each to the powers array.

members = squad['members']

for member in members:
	powers = member['powers']
	for power in powers:
		allpowers.append(power)


pprint(allpowers)