import tracery
from tracery.modifiers import base_english

#named threats (don't want 'the' ahead of them
# "ra",
# "hades",
# "oberon",
# "isis"
# "paimon",

# "satan",
# "dracula",


RULES = {

	# "library"
	"roman_numeral": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", ],
	"number": [ "2", "3", "4", "5", "6", "II", "III", "IV", "V", "VI", "VII", ],
	"color": ["beryl", "emerald", "ruby", "onyx", "purple", "copper", "golden", "silver", "red", "green", "black", "white", "blue", "glittering", "orange", "yellow", "obsidian", "ivory", "ebon", "ebony"],
	"sexy_material": ["leather", "lace", "pvc", "latex", "lingerie"],
	"title": [ "dr.", "mr.", "mrs.", "professor",],
	"magic_type": ["", "sex", "#color#", "dark", "evil", "nature"],
	"letter": [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    

	##################### Nouns #######################
	"real_animal": [ "whale", "eel", "lion", "carrion", "amoeba", "virus", "bacteria", "anaconda", "ant", "bat", "bear", "bee", "bird", "brood", "bunny", "cat", "centipede", "cheetah", "chicken", "dinosaur", "dog", "eagle", "fish", "frog", "hound", "leech", "lizard", "maggot", "mantis", "mole", "piranha", "plant", "puma", "python", "rabbit", "raven", "scorpion", "seaweed", "serpent", "shark", "snake", "spider", "termite", "tiger", "turtle", "vine", "vulture", "wasp", "worm", ],
	"evil_group": [ "communist party", "illuminati", "secret society", "league", "cabal", "unamerican activity", "lizard people", "mafia", "Vatican", "inner circle", "secret service", "CIA", "FBI", "Pentagon", "KGB", "congress", "SS", "council"],
	"battle": [ "attack", "battle", "revolution", "hunt", "counterattack", "battlefield", "bloodbath", "mutiny", "invasion", "war", "massacre", "holocaust", ],
    "job": [ "comptroller", "trucker", "engineer", "alchemist", "architect", "autarch", "avenger", "baron", "biker", "bimbo", "boss", "bureaucrat", "butcher", "cannibal", "cheerleader", "clown", "commander", "commando", "communist", "cop", "crusader", "cultist", "czar", "defender", "detective", "diver", "duke", "duplicator", "emperor", "empress", "exorcist", "football player", "geisha", "gladiator", "goddess", "groupie", "harlot", "hunter", "invader", "king", "knight", "legionnaire", "librarian", "lord", "luchador", "master", "night", "ninja", "nun", "occultist", "pirate", "president", "priest", "prince", "princess", "private eye", "professor", "pyromaniac", "queen", "rabbi", "raider", "ronin", "samurai", "scientist", "secret agent", "seer", "servant", "slayer", "snatcher", "sorceror", "taxman", "trooper", "villager", "witch", "wizard", "astronaut", "barbarian", "commando", "conqueror", "cop", "destroyer", "judge", "raider", "rider", "soldier", "surgeon", "thief", "warlock", "mage", "superhero", "supervillain", "hero", "villain"],
	"food": [ "fruit", "water", "mushroom", "casserole", "toast", "mold", "egg", "tofu", ],
	"natural_phenomena": [ "ash", "cloud", "comet", "fire", "wave", "flood", "fog", "hail", "hurricane", "inferno", "mist", "pool", "rain", "sandstorm", "shadow", "snow", "summer", "tornado", "typhoon", "vapor", "water", "wind", "winter", "smoke", "smog"],
    "shapes": [ "color", "stain", "circle", "pentagram", "hexagon", "element", "colour", "orb", "chaos", "blob", "cube", "flash", "form", "monolith", "sphere", ],
	"spooky_objects_tools_or_weapons": [ "armor", "blade", "candy", "crown", "crystal ball", "drill", "gun", "hammer", "helm", "key", "lance", "mace", "masque", "plate", "rifle", "ring", "saber", "scepter", "shield", "shovel", "sword", "trapdoor", "mask", "capsule", "mirror", "band"],
	"portals": ["gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
	"technology": ["android", "blade", "car", "computer", "doll", "effect", "elevator", "factory", "gear", "hologram", "laser", "machine", "mystereon", "plane", "puppet", "robot", "rocket", "saucer", "ship", "battleship", "tank", "science", "spaceship", "starship", "statue", "toy", "truck", "ufo", "automaton", ],
    "fantasy_animal": [ "alien", "angel", "bigfoot", "chimera", "chupacabra", "cockatrice", "cyborg", "demon", "dragon", "elf", "fairy", "fury", "gargoyle", "ghost", "ghoul", "giant", "gnome", "goblin", "god", "golem", "gorgon", "gremlin", "grue", "hobgoblin", "homunculus", "hydra", "imp", "kobold", "kraken", "leprechaun", "lepus", "leviathan", "lich", "lictor", "lycanthrope", "mermaid", "merman", "monster", "mummy", "mutant", "ogre", "phoenix", "poltergeist", "santa claus", "sasquatch", "satyr", "shapeshifter", "siren", "soul", "spectre", "spirit", "stalker", "troll", "undead", "unicorn", "vampire", "werewolf", "wight", "yeti", "zombie", "snowman"],
	"humans": [ "man", "teenager", "girl", "boy", "woman", "student"],
	"threatening_thing": [ "creep", "beast", "terror", "creature", "it", "thing", "threat", "lurker", "being", "maniac", "corpse", ],
	"scary_phenomena" : [ "hunger", "dream", "horror", "madness", "death", "urge", "fever", "consciousness", "nausea", "pain", "madness", "anguish", "scream"],
	"threatening_substance" : [ "drug", "cocaine", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "grime", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],
	
	"threat": [ "#food#", "#humans#", "#natural_phenomena#", "#ritual#", "#scary_phenomena#", "#spooky_objects_tools_or_weapons#", "#threatening_substance#", "#threatening_thing#", "#body_part#", "#fantasy_animal#", "#job#", "#real_animal#", "#technology#", "#portals#"],
	"body_part": [ "lip", "wing", "blood", "bone", "buns", "bosom", "brain", "claw", "eye", "finger", "flesh", "foot", "gut", "hand", "heart", "jaw", "maw", "mind", "mouth", "muscle", "organ", "skull", "spine", "stomach", "tendon", "tendril", "tentacle", ],
	"scary_parts_of_a_house" : [ "attic", "basement", "bed", "cellar", "closet", "fireplace", "floorboards", "rug", "painting", "furnace", "kitchen", "room", "sewer", "shed", "stairs", "walls", "well", ],
	"story": [ "legend", "secret", "cycle", "fable", "fate", "saga", "tale", "tales", ],
	"moment_in_time": [ "day", "night", "year", "solstice", "time", "dawn", "rise", "dusk", ],
	"ritual": [ "#color# mass", "boogaloo", "dance", "festival", "funeral", "christmas", "opera", "orgy", "party", "pyre", "rite", "ritual", "sacrifice", ],
	"mythological_places" : [ "hell", "atlantis", "valhalla", "underworld", "astral plane", "the plane of leng", "miskatonic university", "Innsmouth", "hades", "avalon", "Shangra La", "El Dorado", "carcosa", "R'lyeh", "Omicron Persei #number#", "vulcan", ],
	"spooky_locale_without_the": [ "swamp", "island", "lake", "tower", "mountain", "hill", ],
	"spooky_locale": [ "void", "barren", "barrier", "caldera", "carnival", "bazzar", "castle", "cave", "continent", "crater", "crypt", "dungeon", "field", "forest", "grave", "graveyard", "cemetery", "grotto", "hill", "hive", "island", "jungle", "keep", "kingdom", "lagoon", "lagoon", "lake", "mausoleum", "mine", "mountain", "rim", "ruin", "sands", "sepulcher", "shipwreck", "shores", "swamp", "throne", "tomb", "torture chamber", "tower", "valley", "vault", "volcano", "wilderness", "fortress", "labrynth", "pit", ],
	"water_and_oceans_with_the" :[ "sea", "deep", "depths", "reef"],
	"dwelling_place" : [ "village", "hotel", "house", "mansion", "fort", "town", "colony", "cabin", "city", "realm", "zone", "-ville", ],
	"time_related" : [ "time", "the future", "forever", "tomorrow", "the year 2000", "the year 5000", "the year 10000", "the 41st Millennium", ],
	"menacing_places_on_earth_without_the": [ "Antarctica", "Babylonia", "Basque Country", "Bavaria", "Egypt", "L.A.", "New Jersey", "Tibet", "area 51", "groom lake", "main street USA", "mesoptamia", "mongolia", "siberia", "soviet russia", "tampa", "yucca flats"],
	"menacing_places_on_earth_with_the": ["Orient", "atlantic", "far east", "north", "nile", "north pole", "outback", "Himalayas", "pacific"],
	"unpleasant_places_without_the" : [ "prison", "jail",],
	"unpleasant_places_with_the" :[ "suburbs", "fair", "silo", "mall", "science fair", "DMV", "library", ],
	"religious_buildings_with_the" : [ "church", "abbey", "cathedral", "pagoda", "chapel", "reliquary", "synagogue", "mosque", "temple", ],

	##################### Adjectives #######################
	"cosmic_adj" :["hallucinogenic", "terminal", "alien", "cosmic", "crawling", "endless", "eternal", "final", "gibbous", "gloaming", "groaning", "hoary", "indescribable", "infinite", "occult", "outer", "star", "stygian", "timeless", ],
	"decayed_adj" : [ "caustic", "acrid", "bubbling", "demolished", "diseased", "disgusting", "dying", "fetid", "melting", "one-eyed", "putrid", "rotting", ],
	"evil_adj" : [ "twisted", "abominable", "aggressive", "corrupt", "dark", "deadly", "demonic", "depraved", "deranged", "dread", "evil", "ferocious", "godless", "grim", "haunted", "homocidal", "horrendous", "horrifying", "infernal", "inhuman", "insane", "insidious", "killer", "laughing", "lurking", "macabre", "mad", "remorseless", "satanic", "shadowy", "sinister", "skeletal", "spooky", "terrifying", "unstoppable", "vampiric", "violent", "mindless", "wrathful", "enraged", "furious", ],
	"horror_movie_adj" : [ "blood-soaked", "cannibal", "charnel", "grind-", "grind", "chainsaw", "bloody", "slasher", "gore-encrusted", ],
	"magical_adj": [ "hexed", "accursed", "magic", "magical", "supernatural", "telepathic", "voodoo", "telekinetic", "precognitive", "clairvoyant", "pyrokinetic", "vedic", "sorcerous", "cursed", "forbidden", "mysterious", "ghost", "ghostly", ],
	"material_adj" : [ "stone", "iron", "metal", "gold", "platinum", "silver", "lead", "wax", "clay", "crystal", "bone", "hollow", "glowing", ],
	"natural_adj" : [ "albino", "amorphous", "frozen", "burning", "boiling", "backwoods", "blood-sucking", "chimeric", "dead", "flesh-eating", "fungal", "gelatinous", "heavy", "jungle", "living", "man-eating", "nocturnal", "protoplasmic", "rabid", "sentient", "starving", "untamed", "wild", "woodland", ],
	"nuclear_science_y_adj" : [ "nuclear", "atomic", "radioactive", "toxic", "mutated", ],
	"old_adj" : [ "eldrich", "prehistoric", "medieval", "long-lost", "lost", "primal", "primeval", "forgotten", "cyclopean", "ancient", "abandoned", ],
	"religion_or_culture_adj" : [ "noble", "highborn", "Aztec", "Egyptian", "eastern", "western", "christian", "jewish", "holy", "sacred", "hebrew", "Mormon", "neanderthal", "heathen", "shamanistic", "Norse", "soviet", "communist", ],
	"sexploitation_adj": [ "kinky", "BDSM", "promiscuous", "raunchy", "dirty", "hedonistic", "desperate", "pent-up", "carnal", "freaky", "deviant", "fleshy", "sexy", "lavacious", "lecherous", "leather", ],
	"silly_adj" : [ "teenage", "surfing", "strange", "weird", "dancing"],
	"size_related_adj": [ "micro", "micro-", "mega", "mega-", "shrinking", "giant", "transforming", "colossal", "titanic", "enormous", "indestructible", "mighty", ],
	"space_age_adj" : [ "robo-", "astro", "rocket", "solar", "genetic", "neon", "space", "mecha-", "mechano-", "techno-", "electric", "electro-mechanical", "cybernetic", "stellar", "turbo", "uber-", "photonic", "temporal", "holographic", "time", "transdimensional", "ultra", "futuristic", "techno", "space age", ],
	"undead_adj" : [ "undead", "reborn", "reanimated", ],
	"unseen_adj": [ "invisible", "immaterial", "empty", "vacant", "phantasm", "phantom", "subterranean", "transparent", ],
	"wonderous_adj" : [ "amazing", "awesome", "fantastic", "glorious", "incredible", "mystical", "terrible", ],

	# Maybes
	"adverb": [ "of", "in", "to", "that came from", "from", "before", "corrupted by", "from beyond", "on the", "on the edge of", "beyond", "inside", "above", "within"],
	"maybe_adj": [ "", "#adj#"],
	"maybe_roman_numeral": [ "", "#roman_numeral#"],

	# Basics
    "shortform":       ["#threat#"],
    "shortpluralform": ["#threat.s#"],
	"possessive_form": ["#threat#'s"],
    "form":       [ "#maybe_adj# #shortform#", ],
    "pluralform": [ "#maybe_adj# #shortpluralform#", ],

	"full_title": [
		"#title#",

		"#title# #silly_suffix#",

		# The Sword of the lictor
        "The #object# of the #pluralform#",

		# The masque of the red death
		"The #object# of the #adj# #object#",

		# Ilsa: she wolf of the ss
		"#form#: #threat# of the #evil_group#",

		# Shadow over innsmouth
		"The #object# #adverb# #place#",

		# "star wars"
		"#adj# #battle#",

		# "grind-house"
		"#place#",

		# the day of the triffids
		# the night of the lepus
		"The #moment_in_time# of the #pluralform#",

		# The blood on satan's claw
		"The #threatening_substance# on the #fantasy_animal#'s #body_part#",
		"The #threatening_substance# in the #fantasy_animal#'s #body_part#",

		# Beyond the valley of the dolls
        "#adverb# the #spooky_locale# of the #pluralform#",

		# sky captain and the world of tomorrow
		"#form# and the world of #time_related#",

        "#iconic_structure#",
		"#silly_sequels#",

	],

	"iconic_structure" : [
		"The #form# that Couldn't be Killed",
		"The #form# that Couldn't be Stopped",
		"The #form# that Wouldn't Die#",
		"The Wild, Wild World of the #form#",
		"The Wild, Wild World of the #pluralform#",
		"They called me '#form#'", 
        "#shortform#-Geddon",
        "#shortform#-nado",
        "#shortform#-zilla",
        "30 #shortform.s# in 30 Days",
        "30 #shortform.s#, 30 Days",
        "Death by #form#",
        "Death by #pluralform#",
        "I Became #form.a#",
        "I Married #form.a#",
        "I Walked with #pluralform#",
        "I Walked with the #form#",
        "I Walked with the #pluralform#",
        "I Was a Teenage #form#",
        "My Wife is #form.a#",

		# Vampire hunter D
		"#shortform# #job# '#letter#'",
	],


    "title": [
		"#silly_prefix# #form#",

		# unsorted:
        "#object# of the #form#",
        "#shortform# #object#",
		"#adj# #job#: The #object# of the #form#",
		"#adj# #object#",
		"#adj# #object# of the #pluralform#",

		# basic form
        "#form#!",
        "The #form#",
		"The #adj# #adj# #shortform#",

		# battles
        "#form# VS. #form#",
        "The #form# and the #form#",
        "#shortform#-zilla VS #shortform#-ra",

		# body part form
        "#body_part# #shortform#",
        "The #body_part# of the #shortform#",

		# job
		"#form# #job#",
		"#shortform# #job#",
        "#job# #shortform# and the #form# #adverb# #place#",
        "#job# #shortform# and the #shortform# #adverb# #place#",
        "#job# #adverb# #place#",

		# form from place
		# escape from NY
		"Escape from #place#",
		"Voyage to #place#",
		"Journey to #place#",

        "The #form# #adverb# #place#",
        "The #shortform# #adverb# #place#",
		"#pluralform# #adverb# #place#",

		# forms I want to appear more rarely
		"#sexploitation_title#",
    ],

	"silly_sequels" : [
		"#place# #number#: The #form#",
		"#place# #number#: Return of the #form#",
		"#place# #number#: #form# #object#",
		"#place# #number#: #object# of the #form#",
		"#form# #number#: #adverb# #place#",
		"The #form# #number#: #adverb# #place#",
	],

	"sexploitation_title" : [
        "#form# de Sade",
        "Sex Slaves of the #form#",
        "The Loves of the #form#",
        "Sexy #threat.s# in Cages",
        "The #form# Lovers",
        "#form# in #sexy_material#",
        "#pluralform# in #sexy_material#",
	],

	"silly_suffix": [
		"! kill! kill!",
		": The revenge",
		": The return",
		": #space_age_adj# #ritual#",
		": #story# of the #threat#",
		" XXX",
	],

	"silly_prefix": [
		"Code Name:",
		"David Winters presents:",
		"Alias:",
		"Danger!!",
		"Fear the",
		"Dread the",
	],

    "object": [
		# TODO: Move some space stuff back here?
		"#battle#",
		"#body_part#",
		"#dwelling_place#",
		"#job#",
		"#moment_in_time#",
		"#natural_phenomena#",
		"#ritual#",
		"#scary_parts_of_a_house#",
		"#scary_phenomena#",
		"#shapes#",
		"#spooky_locale#",
		"#story#",
		"#technology#",
		"#portals#",
		"#threatening_substance#",
		"#spooky_objects_tools_or_weapons#",

		# random
		"revenge",
		"fracture",

		# fighting force
        "legion",
		"army",
		"soldiers",

		# sounds
		"sound",
		"song",
		"melody",

		# space stuff
		"planet",
		"galaxy",
		"comet",
		"moon",

		#thoughts / states
        "vigil",
		"betrayal",
		"lies",
		"promises",
		"wishes",

		# inspiration / action
		"laugh",
        "call",
		"quest",
		"escape",
		"adventure",
		"journey",

		# systems of government / groups
		"anarchy",
		"domain",
		"alliance",
		"cult",
		"monarchy",
		"fellowship",
		"reign",
		"empire",

		# magical stuff
		"#magic_type# magic",
		"#magic_type# magick",
		"#magic_type# tome",
		"#magic_type# spellbook",

		# riches
		"diamonds",
        "harvest",
        "gold",
        "treasure",

		# spooky evidence
		"vision",
		"clue",
		"visions",
		"stare",
		"tracks",
		"sign",
		"footprints",
		"fossil",
        "shadow",
		"touch",
		"sacrifice",
		"whispers",
		"echoes",
		"stench",
		"shard",
		"bone",
		"ruin",
		"trail",

		# scheme
		"grudge",
		"plan",
		"study",
		"plot",
        "revenge",
		"compact",
		"embrace",
		"conspiracy",
		"pact",
		"bargain",

		# partner
        "bride",
		"mate",
		"child",
		"baby",

    ],

	"space_places" : [
		"space",
        "eclipse",
		"constellation",

		"phobos",
		"io",
		"mars",
		"mercury",
		"sol",
		"neptune",
		"jupiter",
		"pluto",
		"saturn",
		"titan",
		"uranus",
		"venus",
		"planet x",

		"another galaxy",
		"another universe",
		"another dimension",
		"another world",
		"the stars",
		"the solar system",
		"the moon",
		"the astroid belt",

		# stars or planets around them
		"altair #maybe_roman_numeral#",
		"Andromeda #maybe_roman_numeral#",
		"cygnus #maybe_roman_numeral#",
		"pegasus #maybe_roman_numeral#",
		"orion #maybe_roman_numeral#",
		"corona borealis #maybe_roman_numeral#",
		"cetus #maybe_roman_numeral#",
	],

	"simple_places" : [
		"below",
		"beyond",
		"underground",
		"the earth",
		"the center of the earth",
		"20,000 fathoms",
		"#space_places#",
		"#time_related#",
	],

	"place": [
		"#simple_places#",

		"the #maybe_adj# #water_and_oceans_with_the#",
		"the #maybe_adj# #menacing_places_on_earth_with_the#",
		"the #maybe_adj# #unpleasant_places_with_the#",
		"the #maybe_adj# #scary_parts_of_a_house#",
		"the #maybe_adj# #spooky_locale#",
		"the #maybe_adj# #religious_buildings_with_the#",

		"#maybe_adj# #unpleasant_places_without_the#",
		"#maybe_adj# #mythological_places#",
		"#maybe_adj# #menacing_places_on_earth_without_the#",
		"#maybe_adj# #spooky_locale_without_the#",
		"#maybe_adj# #dwelling_place#",
	],

	"adj": [
		"#color#",
		"#material_adj#",
		"#sexploitation_adj#",
		"#old_adj#",
		"#nuclear_science_y_adj#",
		"#magical_adj#",
		"#space_age_adj#",
		"#decayed_adj#",
		"#evil_adj#",
		"#natural_adj#",
		"#cosmic_adj#",
		"#wonderous_adj#",
		"#horror_movie_adj#",
		"#size_related_adj#",
		"#undead_adj#",
		"#religion_or_culture_adj#",
		"#unseen_adj#",
		"#silly_adj#",

	]
}


grammar = tracery.Grammar(RULES)
grammar.add_modifiers(base_english)
for i in range(1000):
	title = grammar.flatten("#full_title#")
	
	# merge adjectives / prefixes / suffixes
	#title = title.replace("- ", "")
	#title = title.replace(" -", "")
	title = title.replace("  ", " ")

	# fix spacing
	title = title.replace("' ", "'")
	title = title.replace(" : ", ": ")
	
	# fix plurals
	title = title.replace("womans", "women")
	title = title.replace(" mans ", " men ")
	title = title.replace(" Mans ", " men ")
	title = title.replace("elfs", "elves")
	title = title.replace("nauseas", "nausea")

	# capitalize
	title = title.strip().title()

	# fix title case errors
	title = title.replace("'S ", "'s ")
	title = title.replace(" Of ", " of ")
	title = title.replace(" The ", " the ")
	title = title.replace(" Cia", " CIA")
	title = title.replace(" Fbi", " FBI")
	title = title.replace("'T ", "'t ")
	title = title.replace(" Xxx", " XXX")
	title = title.replace(" Ss", " SS")
	title = title.replace(" Ii ", " II ")
	title = title.replace(" Ii:", " II:")
	title = title.replace(" Iii ", " III ")
	title = title.replace(" Iii:", " III:")
	title = title.replace(" Iv ", " IV ")
	title = title.replace(" Iv:", " IV:")
	title = title.replace(" Vi ", " VI ")
	title = title.replace(" Vi:", " VI:")
	title = title.replace(" Vii ", " VII ")
	title = title.replace(" Vii:", " VII:")
	title = title.replace("41St", "41st")
	print(title)
