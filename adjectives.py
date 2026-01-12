def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

##################### Adjectives #######################
base_adjectives = {

"horror_movie_adj" : ["undead", "reborn", "reanimated", "blood-soaked", "cannibal", "cannibalistic", "charnel", "grind-", "grind", "chainsaw", "bloody", "slasher", "gore-encrusted", ],
"magical_adj": [ "hexed", "accursed", "magic", "magical", "supernatural", "telepathic", "voodoo", "telekinetic", "precognitive", "clairvoyant", "pyrokinetic", "vedic", "sorcerous", "cursed", "forbidden", "mysterious", "ghost", "ghostly", ],
"natural_adj" : ["bamboo", "psychotic", "chitinous", "flaming", "fiery", "psycho-", "flying", "albino", "amorphous", "frozen", "burning", "backwoods", "blood-sucking", "chimeric", "dead", "flesh-eating", "fungal", "gelatinous", "heavy", "jungle", "living", "man-eating", "nocturnal", "protoplasmic", "rabid", "sentient", "starving", "untamed", "wild", "woodland", ],
"old_adj" : [ "eldrich", "prehistoric", "medieval", "long-lost", "lost", "primal", "primeval", "forgotten", "cyclopean", "ancient", "abandoned", "primordial", ],
"silly_adj" : load("silly_adjs"),
"wonderous_adj" : load("wonderous_adjs.txt"),
"color": load("colors"),
"unseen_adj": load("unseen_adjs"),
"material_adj" : load("material_adjs"),
"cosmic_adj": load("cosmic_adjs"),
"size_related_adj": load("size_related_adjs"),
"sexploitation_adj": load("sexploitation_adjs"),
"space_age_adj" : load("space_age_adjs"),
"decayed_adj" : load("decayed_adjs"),
"evil_adj" : load("evil_adjs"),
"crazy_adj": load("crazy_adjs"),
"hippy_adj": load("hippy_adjs"),
"religion_or_culture_adj" : load("religion_or_culture_adjs"),
"evocative_nations": load("evocative_nations"),
"ordering": load("ordering"),

# needed for close encounters of the third kind but kinda awkward everywhere else...
# "distance": ["close", "nearby"],

}
