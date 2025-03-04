import tracery
from tracery.modifiers import base_english

# The Million Eyes of Sumuru
#named threats (don't want 'the' ahead of them
# "ra",
# "hades",
# "oberon",
# "isis"
# "paimon",
# "satan",
# "dracula",
# "elvira",

# the plane of leng
# sort adverbs
# adjective / noun agreement?
# https://en.wikipedia.org/wiki/Erotic_thriller#1980s%E2%80%931990s:_Classic_period


RULES = {

	# "library"
	"roman_numeral": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", ],
	"number": [ "2", "3", "4", "5", "6", "II", "III", "IV", "V", "VI", "VII", ],
	"color": ["beryl", "emerald", "scarlet", "ruby", "onyx", "purple", "copper", "golden", "silver", "red", "green", "black", "white", "blue", "glittering", "orange", "yellow", "obsidian", "ivory", "ebon", "ebony"],
	"sexy_material": ["the buff", "leather", "rubber", "lace", "pvc", "latex", "lingerie"],
	"title": [ "dr.", "mr.", "mrs.", "professor",],
	"magic_type": ["", "sex", "#color#", "dark", "evil", "nature"],
	"letter": [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
	"moved" : [ "walked into", "was sent to", "traveled to", "returned from", "came back from", "time-traveled to", "slid into", "fell into", "was transported to", ],
	"partner" : ["girlfriend", "boyfriend", "twin", "husband", "wife", "boss", "partner", "bride", "spouse", "groom", "mate", "baby"],

	"drug": ["spice", "stimulant", "heroin", "psychedelic", "drug", "marijuana", "pcp", "cocaine", "LSD", "reefer", "ganja", "angel dust"],
	"riches": ["diamonds", "riches", "bounty", "harvest", "gold", "treasure", "wealth", "fortune", "prosperity", "opulence"],

	##################### Nouns #######################
	"sexy_servant" : [ "Sex Slave", "Love Servant", "Sex Toy", "Lover", "Concubine", "Pleasure mistress", "Pleasure master"],
	"real_animal": ["horse", "owl", "whale", "eel", "lion", "amoeba", "virus", "orca", "bacteria", "anaconda", "ant", "bat", "bear", "bee", "bird", "brood", "bunny", "cat", "centipede", "cheetah", "chicken", "dinosaur", "dog", "eagle", "fish", "frog", "hound", "leech", "lizard", "maggot", "mantis", "mole", "razorback", "piranha", "hedge", "tree", "shrub", "plant", "puma", "python", "rabbit", "raven", "scorpion", "seaweed", "serpent", "shark", "snake", "spider", "termite", "tiger", "turtle", "vine", "vulture", "wasp", "worm", ],
	"evil_group": [ "gestapo", "communist party", "illuminati", "secret society", "league", "triumvirate", "demagogue", "billionaire", "cabal", "unamerican activity", "lizard person", "mafia", "Vatican", "inner circle", "secret service", "CIA", "FBI", "Pentagon", "KGB", "congress", "SS", "council", "anarchy", "domain", "alliance", "cult", "monarchy", "fellowship", "reign", "empire"],
	"battle": [ "attack", "battle", "clash", "revolution", "hunt", "counterattack", "battlefield", "bloodbath", "mutiny", "invasion", "war", "massacre", "holocaust", ],
    "job": [ "messiah", "conciliator", "junkie", "enforcer", "gangster", "roadie", "cowboy", "vigilante", "vixen", "marquis", "student", "mom", "dad", "father", "mother", "runner", "surfer", "hooker", "comptroller", "trucker", "engineer", "alchemist", "architect", "autarch", "avenger", "baron", "biker", "bimbo", "bureaucrat", "butcher", "cannibal", "cheerleader", "clown", "commander", "commando", "communist", "cop", "crusader", "cultist", "czar", "defender", "detective", "diver", "duke", "duplicator", "emperor", "empress", "exorcist", "football player", "geisha", "gladiator", "goddess", "groupie", "harlot", "hunter", "invader", "king", "knight", "legionnaire", "librarian", "lord", "luchador", "master", "ninja", "nun", "occultist", "pirate", "president", "priest", "prince", "princess", "private eye", "professor", "pyromaniac", "queen", "rabbi", "raider", "ronin", "samurai", "scientist", "secret agent", "seer", "servant", "slayer", "snatcher", "sorceror", "taxman", "trooper", "villager", "witch", "wizard", "astronaut", "renegade", "barbarian", "commando", "conqueror", "cop", "destroyer", "judge", "raider", "rider", "soldier", "surgeon", "thief", "warlock", "druid", "cleric", "preacher", "mage", "superhero", "supervillain", "hero", "villain"],
	"food": [ "fruit", "water", "mushroom", "casserole", "toast", "mold", "egg", "tofu", "cheese"],
	"natural_phenomena": [ "planet", "galaxy", "comet", "sun", "star", "moon", "ash", "cloud", "comet", "fire", "wave", "flood", "fog", "hail", "hurricane", "inferno", "mist", "pool", "rain", "sandstorm", "shadow", "snow", "summer", "tornado", "typhoon", "vapor", "water", "wind", "winter", "smoke", "smog"],
    "shapes": [ "pyramid", "vector", "field", "color", "stain", "circle", "pentagram", "hexagon", "element", "colour", "orb", "chaos", "blob", "cube", "flash", "form", "monolith", "sphere", ],
	"spooky_objects_tools_or_weapons": [ "armor", "blade", "candy", "crown", "crystal ball", "drill", "relic", "artifact", "antique", "gun", "machinegun", "saw", "hammer", "amulet", "guillotine", "key", "lance", "mace", "masque", "plate", "rifle", "ring", "saber", "scepter", "shield", "shovel", "sword", "trapdoor", "mask", "capsule", "blaster", "mirror", "band"],
	"portal": ["gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
	"technology": ["test tube", "zeppelin", "forcefield", "equations", "raygun", "monument", "android", "blade", "car", "train", "computer", "doll", "effect", "elevator", "factory", "gear", "hologram", "laser", "machine", "mystereon", "plane", "puppet", "robot", "rocket", "saucer", "ship", "battleship", "tank", "science", "experiment", "spaceship", "starship", "statue", "toy", "truck", "ufo", "automaton", ],
    "fantasy_animal": [ "revenant", "phantasm", "alien", "angel", "bigfoot", "chimera", "chupacabra", "cockatrice", "cyborg", "demon", "dragon", "elf", "fairy", "fury", "gargoyle", "ghost", "ghoul", "giant", "gnome", "goblin", "god", "golem", "gorgon", "gremlin", "grue", "hobgoblin", "homunculus", "hydra", "imp", "kobold", "kraken", "leprechaun", "lepus", "leviathan", "lich", "lictor", "lycanthrope", "mermaid", "merman", "monster", "mummy", "mutant", "ogre", "phoenix", "poltergeist", "santa claus", "sasquatch", "satyr", "shapeshifter", "siren", "soul", "spectre", "spirit", "stalker", "troll", "undead", "unicorn", "vampire", "werewolf", "wight", "yeti", "zombie", "snowwoman", "snowman"],
	"humans": [ "man", "teenager", "girl", "boy", "woman", "chick", "dude", "children", "daughter", "son"],
	"threatening_thing": [ "freaks", "scum", "creep", "beast", "terror", "humanoids", "creature", "it", "thing", "threat", "lurker", "being", "maniac", "corpse", ],
	"scary_phenomena" : [ "nightmare", "hunger", "dream", "horror", "madness", "death", "urge", "fever", "consciousness", "nausea", "pain", "madness", "anguish", "scream"],
	"threatening_substance" : [ "web", "#drug#", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "grime", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],
	
	"body_part": [ "fist", "lip", "wing", "blood", "bone", "bun", "bosom", "brain", "claw", "eye", "finger", "flesh", "foot", "gut", "hand", "heart", "jaw", "maw", "mind", "mouth", "muscle", "organ", "skull", "face", "teeth", "brow", "spine", "stomach", "gaze", "tendril", "tentacle", ],
	"scary_parts_of_a_house" : [ "attic", "basement", "bed", "cellar", "closet", "fireplace", "floorboards", "rug", "painting", "furnace", "kitchen", "room", "sewer", "garden", "backyard", "shed", "stairs", "walls", "well", ],
	"story": ["elegy", "legend", "secret", "cycle", "fable", "fate", "saga", "tale", "tales", ],
	"moment_in_time": [  "age", "era", "aeon", "eon", "day", "night", "year", "solstice", "time", "dawn", "rise", "dusk", "twilight"],
	"ritual": [ "sabbath", "#color# mass", "dance", "rave", "concert", "festival", "funeral", "christmas", "opera", "orgy", "party", "pyre", "rite", "ritual", "sacrifice", ],
	"mythological_places" : [ "hell", "elm street", "greenwich village", "eden", "atlantis", "troy", "Olympus", "Armageddon", "valhalla", "underworld", "astral plane", "miskatonic university", "Innsmouth", "hades", "avalon", "Ga'Hoole", "Shangra-La", "El Dorado", "carcosa", "R'lyeh", "Tau Ceti #number#", "Omicron Persei #number#", "vulcan", ],
	"spooky_locale_without_the": [ "swamp", "island", "lake", "tower", "mountain", "hill", ],
	"spooky_locale": [ "continuum", "lighthouse", "pyramid", "void", "barren", "barrier", "caldera", "carnival", "bazzar", "castle", "cave", "continent", "crater", "crypt", "dungeon", "field", "forest", "grave", "graveyard", "cemetery", "grotto", "hill", "hive", "island", "jungle", "keep", "kingdom", "lagoon", "lagoon", "lake", "mausoleum", "mine", "mountain", "rim", "ruin", "sands", "sepulcher", "shipwreck", "shores", "swamp", "throne", "tomb", "torture chamber", "tower", "valley", "vault", "volcano", "wilderness", "fortress", "labrynth", "pit", ],
	"water_and_oceans_with_the" :[ "sea", "deep", "depths", "reef"],
	"dwelling_place" : [ "village", "hotel", "house", "mansion", "fort", "stalag", "base", "barracks", "town", "colony", "cabin", "city", "realm", "zone"],
	"menacing_places_on_earth_without_the": [ "Antarctica", "Babylonia", "Basque Country", "Baghdad", "Persia", "harlem", "berlin", "Bavaria", "Egypt", "L.A.", "New Jersey", "Tibet", "area 51", "groom lake", "main street USA", "mesoptamia", "mongolia", "siberia", "soviet russia", "tampa", "yucca flats"],
	"menacing_places_on_earth_with_the": ["Orient", "atlantic", "far east", "north", "nile", "north pole", "outback", "Himalayas", "pacific"],
	"unpleasant_places_without_the" : [ "prison", "jail",],
	"unpleasant_places_with_the" :[ "suburbs", "fair", "silo", "mall", "science fair", "DMV", "library", ],
	"religious_buildings_with_the" : [ "church", "abbey", "cathedral", "pagoda", "chapel", "reliquary", "synagogue", "mosque", "temple", ],

	##################### Adjectives #######################
	"cosmic_adj" :["silent", "ruined", "lovecraftian", "non-euclidean", "hallucinogenic", "terminal", "alien", "cosmic", "crawling", "endless", "eternal", "final", "gibbous", "gloaming", "groaning", "hoary", "indescribable", "infinite", "occult", "outer", "star", "stygian", "timeless", ],
	"decayed_adj" : ["paralyzing", "caustic", "acrid", "bubbling", "demolished", "diseased", "disgusting", "dying", "fetid", "melting", "one-eyed", "putrid", "rotting", ],
	"evil_adj" : [ "twisted", "abominable", "aggressive", "corrupt", "dark", "deadly", "demonic", "depraved", "deranged", "dread", "evil", "ferocious", "godless", "grim", "haunted", "homicidal", "horrifying", "infernal", "inhuman", "insane", "insidious", "killer", "laughing", "lurking", "macabre", "mad", "remorseless", "satanic", "shadowy", "sinister", "skeletal", "spooky", "terrifying", "unstoppable", "vampiric", "violent", "mindless", "wrathful", "enraged", "furious", ],
	"horror_movie_adj" : [ "blood-soaked", "cannibal", "charnel", "grind-", "grind", "chainsaw", "bloody", "slasher", "gore-encrusted", ],
	"magical_adj": [ "hexed", "accursed", "magic", "magical", "supernatural", "telepathic", "voodoo", "telekinetic", "precognitive", "clairvoyant", "pyrokinetic", "vedic", "sorcerous", "cursed", "forbidden", "mysterious", "ghost", "ghostly", ],
	"material_adj" : [ "water", "fire", "earth", "stone", "iron", "metal", "titanium", "aluminum", "cobalt", "plutonium", "thorium", "uranium", "gold", "silver", "lead", "wax", "clay", "crystal", "bone"],
	"material_properties" : ["hollow", "glowing"],
	"natural_adj" : [ "flaming", "fiery", "psycho-", "flying", "albino", "amorphous", "frozen", "burning", "boiling", "backwoods", "blood-sucking", "chimeric", "dead", "flesh-eating", "fungal", "gelatinous", "heavy", "jungle", "living", "man-eating", "nocturnal", "protoplasmic", "rabid", "sentient", "starving", "untamed", "wild", "woodland", ],
	"nuclear_science_y_adj" : [ "nuclear", "atomic", "radioactive", "toxic", "mutated", ],
	"old_adj" : [ "eldrich", "prehistoric", "medieval", "long-lost", "lost", "primal", "primeval", "forgotten", "cyclopean", "ancient", "abandoned", ],
	"religion_or_culture_adj" : [ "noble", "highborn", "Mayan", "Aztec", "Egyptian", "eastern", "western", "christian", "jewish", "holy", "sacred", "hebrew", "Mormon", "neanderthal", "heathen", "shamanistic", "Norse", "soviet", "communist", ],
	"sexploitation_adj": [ "transsexual", "foxy", "immoral", "kinky", "BDSM", "promiscuous", "raunchy", "dirty", "hedonistic", "desperate", "pent-up", "carnal", "freaky", "deviant", "fleshy", "sexy", "disco", "free-love", "pleasurable", "lavacious", "lecherous", "leather", ],
	"silly_adj" : [ "teenage", "surfing", "strange", "weird", "convulsing", "new-wave"],
	"size_related_adj": [ "retro", "micro", "micro-", "mega", "mega-", "shrinking", "giant", "transforming", "colossal", "titanic", "enormous", "indestructible", "mighty", ],
	"space_age_adj" : [ "video", "film", "experimental", "robo-", "astro", "rocket", "solar", "genetic", "neon", "space", "mecha-", "mechano-", "techno-", "electric", "electro-mechanical", "cybernetic", "stellar", "turbo", "uber-", "photonic", "temporal", "holographic", "time", "transdimensional", "ultra", "futuristic", "techno", "space age", ],
	"undead_adj" : [ "undead", "reborn", "reanimated", ],
	"unseen_adj": [ "invisible", "immaterial", "empty", "vacant", "phantom", "subterranean", "transparent", ],
	"wonderous_adj" : [ "amazing", "fantastic", "glorious", "incredible", "mystical", "terrible", ],

	# Maybes
	"adverb": [ "of", "in", "to", "that came from", "from", "before", "corrupted by", "from beyond", "on", "on the edge of", "beyond", "inside", "above", "within"],
	"maybe_adj": [ "", "#adj#", "#adj#"],
	"maybe_old_adj": ["", "#old_adj#"],
	"maybe_roman_numeral": [ "", "#roman_numeral#"],

	# Basics
    "shortform":       ["#threat#"],
    "shortpluralform": ["#threat.s#"],
	"possessive_form": ["#threat#'s"],
    "form":       [ "#maybe_adj# #shortform#", ],
    "pluralform": [ "#maybe_adj# #shortpluralform#", ],



    "full_title": [

		# prefix and suffix
		"#silly_prefix# #shortform#",
		"#silly_prefix# #form#",
		"#form# #silly_suffix#",

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

		# one person X machine
		"One Man #shortform# Machine",
		"One Woman #shortform# Machine",
		"One Man #shortform# #shortform#",
		"One Woman #shortform# #shortform#",

		# battles
        "#form# VS. #form#",
        "The #form# and the #form#",
        "#shortform#-zilla VS #shortform#-ra",

		# body part form
        "#body_part# #shortform#",
        "The #body_part# of the #shortform#",

		# the place that was turned to material
		"The #place_without_the# that was turned to #material_adj#",
		"The #place_without_the# that became #material_adj#",

		# magic job
		"#magic_type# magic #job#",

		# carnival of souls
		"#object# of #shortpluralform#",
		"The #object# of #shortpluralform#",

		"The #place# of #material_adj#",

		# job
		"#form# #job#",
		"#shortform# #job#",
        "#job# #shortform# and the #form# #adverb# #place#",
        "#job# #shortform# and the #shortform# #adverb# #place#",
        "#job# #adverb# #place#",
		"#job# #object#",
		# Samurai cop
		"#job# #job#",

		# The treasure of the sierra madres
		"The #maybe_old_adj# #riches# of #place#",

		# Mountain of the cannibal god
		"#place_without_the# of the #form#",

		# Plan 9 from outer space
		"Plan #number# from #place#",

		# form from place
		# escape from NY
		"The escape from #place#",
		"The voyage to #place#",
		"The journey to #place#",

		# The love witch
		"The #object# #job#",

        "The #form# #adverb# #place#",
        "The #shortform# #adverb# #place#",
		"#pluralform# #adverb# #place#",

		# The blood on satan's claw
		"The #threatening_substance# on the #fantasy_animal#'s #body_part#",
		"The #threatening_substance# in the #fantasy_animal#'s #body_part#",

		# The Sword of the lictor
        "The #object# of the #pluralform#",

		# The masque of the red death
		"The #object# of the #adj# #object#",

		"The #portal# to #place#",
		"The #portal# back to #place#",

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

		# Beyond the valley of the dolls
        "#adverb# the #spooky_locale# of the #pluralform#",

		# sky captain and the world of tomorrow
		"#form# and the world of #simple_places#",

		# Vampire hunter D
		"#shortform# #job# '#letter#'",

		# Daughters of the Sun
		"#humans# of the #natural_phenomena#", 
		"#humans.s# of the #natural_phenomena#", 

		# a few other ones
		"The #form# that Couldn't be Killed",
		"The #form# that Couldn't be Stopped",
		"The #form# that Wouldn't Die#",
		"The Wild, Wild World of the #form#",
		"The Wild, Wild World of the #pluralform#",
		"They called me '#form#'", 
        "#shortform# -Geddon",
        "#shortform# -nado",
        "#shortform# -zilla",
        "30 #shortform.s# in 30 Days",
        "30 #shortform.s#, 30 Days",
        "Death by #form#",
        "Death by #pluralform#",
        "I Became #form.a#",
        "I Married #form.a#",
        "I Walked with #pluralform#",
        "I Walked with the #form#",
        "I Walked with the #pluralform#",
		"I Was in league with #form.a#",
        "I #moved# #place#",
        "I Was a Teenage #form#",
        "My #partner# is #form.a#",
		"I attended #adj.a# #ritual#",

		# sexploitation
        "My #partner# is #adj.a# #sexy_servant#",
        "My #partner# is the #adj# #sexy_servant# of #shortpluralform#",
        "My #partner# is the #adj# #sexy_servant# of #job.s#",
        "#sexy_servant.s# of the #form#",
		"#adj# love potion#",
        "#form# de Sade",
        "Sexy #threat.s# in Cages",
        "The #form# Lovers",
        "#form# in #sexy_material#",
        "#pluralform# in #sexy_material#",

		# forms I want to appear more rarely
		"#silly_sequels#",
	],

	"silly_sequels" : [
		"#place# #number#: The #form#",
		"#place# #number#: Return of the #form#",
		"#place# #number#: Revenge of the #form#",
		"#place# #number#: #form# #object#",
		"#place# #number#: #object# of the #form#",
		"#form# #number#: #adverb# #place#",
		"The #form# #number#: #adverb# #place#",
		"The #form# #number#: #place#",
	],
	"silly_suffix": [
		"! kill! kill!",
		" a go-go",
		" (yellow)",
		" (blue)",
		": The revenge",
		": The return",
		": #space_age_adj# #ritual#",
		": #story# of the #threat#",
		" XXX",
	],

	"silly_prefix": [
		"Manos: The #object.s# of",
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
		"#real_animal#",
		"#technology#",
		"#evil_group#",
		"#portal#",
		"#threatening_substance#",
		"#spooky_objects_tools_or_weapons#",
		"#drug#",
		"#partner#",
		"#riches#",

		# random
		"curve",
		"country",
		"sex-change operation",
		"school",
		"carrion",
		"crop circles",
		"barbed wire",
		"revenge",
		"fracture",
		"vice",
		"hole",
		"sex",

		# fighting force
        "legion",
		"army",

		# sounds
		"sound",
		"song",
		"melody",
		"shiver",

		#thoughts / states
		"love",
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

		# magical stuff
		"#magic_type# magic",
		"#magic_type# magick",
		"#magic_type# tome",
		"#magic_type# spellbook",

		# spooky evidence
		"vision",
		"clue",
		"proof",
		"vestage",
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

    ],

	"threat": [
		"#food#",
		"#humans#",
		"#natural_phenomena#",
		"#ritual#",
		"#scary_phenomena#",
		"#spooky_objects_tools_or_weapons#",
		"#shapes#",
		"#threatening_substance#",
		"#threatening_thing#",
		"#evil_group#",
		"#body_part#",
		"#fantasy_animal#",
		"#job#",
		"#real_animal#",
		"#technology#",
		#"#portal#"
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
		"#space_places#",

		"forever",
		"tomorrow",
		"the earth",
		"the future",
		"the year 2000",
		"the year 3000",
		"the year 5000",
		"the year 10000",
		"the 41st Millennium",
		"the center of the earth",

		"below",
		"beyond",
		"above",
		"underground",
		"20,000 fathoms",
	],

	"place_without_the" : [
		"#water_and_oceans_with_the#",
		"#menacing_places_on_earth_with_the#",
		"#unpleasant_places_with_the#",
		"#scary_parts_of_a_house#",
		"#spooky_locale#",
		"#religious_buildings_with_the#",
	],

	"place_with_the" : [
		"#unpleasant_places_without_the#",
		"#mythological_places#",
		"#menacing_places_on_earth_without_the#",
		"#spooky_locale_without_the#",
		"#dwelling_place#",
	],

	"place": [
		"#simple_places#",
		"the #maybe_adj# #place_without_the#",
		"#maybe_adj# #place_with_the#",

	],

	"adj": [
		"#color#",
		"#material_adj#",
		"#material_properties#", 
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
	title = title.replace("- ", "")
	title = title.replace(" -", "")
	title = title.replace("  ", " ")

	# fix spacing
	title = title.replace("' ", "'")
	title = title.replace(" : ", ": ")
	
	# fix plurals
	title = title.replace("womans", "women")
	title = title.replace(" mans", " men")
	title = title.replace("elfs", "elves")
	title = title.replace("nauseas", "nausea")
	title = title.replace("bloods", "blood")
	title = title.replace("foots", "feet")
	title = title.replace("snowmans", "snowmen")
	title = title.replace("snowwomans", "snowwomen")
	

	# capitalize
	title = title.strip().title()

	# fix title case errors
	title = title.replace("'S ", "'s ")
	title = title.replace(" Of ", " of ")
	title = title.replace(" The ", " the ")
	title = title.replace(" Cia", " CIA")
	title = title.replace(" Lsd", " LSD")
	title = title.replace("Lsd:", "LSD:")
	title = title.replace(" Dmv", " DMV")
	title = title.replace(" Bdsm", " BDSM")
	title = title.replace(" Fbi", " FBI")
	title = title.replace(" Pvc", " PVC")
	title = title.replace(" cheetahes", " cheetahs")
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
