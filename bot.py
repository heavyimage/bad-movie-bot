import tracery
import json
from tracery.modifiers import base_english

with open("rules.json") as f:
    rules = json.loads(f.read())

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
for i in range(1000):
    print(grammar.flatten("#origin#"))
