def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

##################### Adjectives #######################
base_adjectives = {

"horror_movie_adj" : ["undead", "reborn", "reanimated", "blood-soaked", "cannibal", "cannibalistic", "charnel", "grind-", "grind", "chainsaw", "bloody", "slasher", "gore-encrusted", ],
"magical_adj": [ "hexed", "accursed", "magic", "magical", "supernatural", "telepathic", "voodoo", "telekinetic", "precognitive", "clairvoyant", "pyrokinetic", "vedic", "sorcerous", "cursed", "forbidden", "mysterious", "ghost", "ghostly", ],
"natural_adj" : ["bamboo", "psychotic", "chitinous", "flaming", "fiery", "psycho-", "flying", "albino", "amorphous", "frozen", "burning", "backwoods", "blood-sucking", "chimeric", "dead", "flesh-eating", "fungal", "gelatinous", "heavy", "jungle", "living", "man-eating", "nocturnal", "protoplasmic", "rabid", "sentient", "starving", "untamed", "wild", "woodland", ],
"old_adj" : [ "eldrich", "prehistoric", "medieval", "long-lost", "lost", "primal", "primeval", "forgotten", "cyclopean", "ancient", "abandoned", "primordial", ],
"silly_adj" : ["biblically-accurate", "teenage", "surfing", "strange", "weird", "convulsing", "new-wave", "middle-age", "undercover"],
"wonderous_adj" : ["uber", "ultra", "fabulous", "amazing", "fantastic", "glorious", "incredible", "mystical", "terrible", ],
"color": ["crimson", "ruby", "brown", "beryl", "chromatic", "emerald", "scarlet", "ruby", "onyx", "purple", "copper", "golden", "silver", "red", "green", "black", "white", "blue", "orange", "yellow", "obsidian", "ebon", "cobalt", "azure"],
"unseen_adj": ["invisible", "immaterial", "empty", "vacant", "phantom", "subterranean", "transparent", ],
"material_adj" : ["ruby", "sapphire", "brass", "copper", "water", "fire", "earthen", "stone", "iron", "metal", "stainless steel", "titanium", "aluminum", "cobalt", "plutonium", "thorium", "uranium", "gold", "silver", "lead", "wax", "clay", "crystal", "bone", "hollow", "glowing", "shining", "glittering", "stainless"],
"cosmic_adj": ["forever", "neverending", "spectral", "shuddering", "silent", "ruined", "lovecraftian", "non-euclidean", "hallucinogenic", "terminal", "alien", "astral", "cosmic", "crawling", "endless", "eternal", "final", "gibbous", "groaning", "indescribable", "infinite", "occult", "outer", "stygian", "timeless" ],
"size_related_adj": ["micro", "micro-", "mega", "mega-", "shrinking", "giant", "transforming", "colossal", "titanic", "enormous", "indestructible", "mighty", ],
"sexploitation_adj": ["perverted", "queer", "femme", "butch", "uptight", "gender", "nude", "perky", "moist", "sex-change", "sensual", "buxom", "well-endowed", "passionate", "transsexual", "foxy", "immoral", "kinky", "BDSM", "promiscuous", "raunchy", "dirty", "hedonistic", "desperate", "pent-up", "carnal", "freaky", "deviant", "fleshy", "sexy", "disco", "free-love", "pleasurable", "lavacious", "lecherous", "leather", "buff", "horny", "gay", "lesbian", "trans", "transvestite"],
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
