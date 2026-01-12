def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

##################### Adjectives #######################
base_adjectives = {

"horror_movie_adj": 		load("horror_movie_adjs"),
"magical_adj": 			load("magical_adjs"),
"natural_adj":  		load("natural_adjs"),
"old_adj":  			load("old_adjs"),
"silly_adj":  			load("silly_adjs"),
"wonderous_adj":  		load("wonderous_adjs"),
"color": 			load("colors"),
"unseen_adj": 			load("unseen_adjs"),
"material_adj":  		load("material_adjs"),
"cosmic_adj": 			load("cosmic_adjs"),
"size_related_adj": 		load("size_related_adjs"),
"sexploitation_adj": 		load("sexploitation_adjs"),
"space_age_adj":  		load("space_age_adjs"),
"decayed_adj":  		load("decayed_adjs"),
"evil_adj":  			load("evil_adjs"),
"crazy_adj": 			load("crazy_adjs"),
"hippy_adj": 			load("hippy_adjs"),
"religion_or_culture_adj":  	load("religion_or_culture_adjs"),
"evocative_nations": 		load("evocative_nations"),
"ordering": 			load("ordering"),

# needed for close encounters of the third kind but kinda awkward everywhere else...
# "distance": ["close", "nearby"],

}
