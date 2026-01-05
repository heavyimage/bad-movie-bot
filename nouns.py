# TODO: Move some space stuff back here?

base_nouns = {
    # Basic words  / vocabulary
    "partner": ["step-father", "step-mother", "mother-in-law", "father-in-law", "father", "mother", "girlfriend", "boyfriend", "twin", "husband", "wife", "boss", "partner", "bride", "spouse", "groom", "mate", "baby", "offspring"],
    "drug": ["spice", "stimulant", "heroin", "psychedelic", "drug", "marijuana", "pcp", "cocaine", "LSD", "reefer", "ganja", "angel dust"],
    "portal": ["hole", "gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
    "food": [ "carrion", "fruit", "tomato", "water", "mushroom", "casserole", "toast", "mold", "egg", "tofu", "cheese"],
    "appliance_or_tool": ["refrigerator", "saw", "hammer", "shovel", "drill", "key",],
    "weapon": ["blade", "gun", "machine gun", "guillotine", "lance", "mace", "rifle", "saber", "sword", "blaster", "raygun", "nunchuck"],
    "person": ["man", "woman", "person"],
    "story": ["elegy", "legend", "secret", "cycle", "fable", "fate", "saga", "tale", "tales", ],
    "spooky_evidence": ["crop circles", "vision", "clue", "proof", "vestage", "vision", "stare", "track", "sign", "footprint", "fossil", "shadow", "touch", "sacrific", "whisper", "echo", "stench", "shard", "bone", "ruin", "trail"],
    "operation": ["assignment", "phase", "operation", "plan", "conspiracy", "sex-change"],
    "battle": ["siege", "attack", "battle", "clash", "revolution", "hunt", "counterattack", "battlefield", "bloodbath", "mutiny", "invasion", "war", "massacre", "holocaust"],
	"vehicle": ["car", "ufo", "flying saucer", "train", "zeppelin", "truck", "rocket", "ship", "battleship", "aircraft carrier", "plane", "jet", "elevator", "tank", "spaceship", "starship", "scooter"],
    "shapes": ["geometry", "curve", "pyramid", "vector", "field", "color", "stain", "circle", "pentagram", "hexagon", "element", "colour", "orb", "blob", "cube", "flash", "form", "monolith", "sphere", ],
    "body_part": ["body", "skin", "fist", "lip", "wing", "blood", "bone", "bun", "bosom", "brain", "claw", "eye", "finger", "flesh", "foot", "gut", "hand", "heart", "jaw", "maw", "mind", "mouth", "muscle", "skull", "face", "teeth", "brow", "spine", "stomach", "gaze", "tendril", "tentacle", ],
    "sexy_material": ["the buff", "leather", "rubber", "g-string", "thong", "lace", "pvc", "latex", "lingerie"],
    "adventure": ["quest", "escape", "voyage", "odyssey", "journey", "pilgrimage", "adventure", "expedition", "encounter"],
    "riches": ["diamonds", "riches", "bounty", "harvest", "gold", "treasure", "wealth", "fortune", "prosperity", "opulence"],
    "sound": ["sound", "scream", "song", "melody", "shiver", "song"],
    "scheme": ["destiny", "scheme", "grudge", "study", "plot", "revenge", "compact", "embrace", "pact", "bargain", "vigil", "betrayal", "lies", "promises", "wishes"],
    "concept": ["vice", "love", "horror", "beauty", "evil", "doom", "damnation", "revenge", "madness", "damnation", "fear", "loathing", "wonder", "evil", "life", "chaos", "justice", "insanity", "nightmare", "hunger", "dream", "horror", "death", "urge", "fever", "consciousness", "nausea", "pain", "anguish", "eternity", "infinity", "sacrifice", "pestilence", "dogma", "courage", "vengence", "rage"],
    "magic": ["magic", "magick", "tome", "spellbook", "phylactery"],
    "instrament": ["guitar", "piano", "flute", "pan-pipes", "tubular bells"],

    # simple meta rules
    "ritual": ["sabbath", "#color# mass", "dance", "rave", "concert", "festival", "funeral", "christmas", "opera", "orgy", "party", "pyre", "rite", "ritual", "sacrifice", "circus", "carnival", "bazzar", ],
    "human": [ "#person#", "broad", "gentle#person#", "teenager", "girl", "boy", "beefcake", "chick", "dude", "children", "daughter", "son", "bimbo", "nympho", "harlot"],
    "sexy_servant": [ "sex slave", "love servant", "sex toy", "lover", "concubine", "pleasure #job#"],
    "technology": ["#vehicle#", "space station", "test tube", "forcefield", "equations", "monument", "android", "computer", "doll", "effect", "factory", "gear", "hologram", "laser", "machine", "plane", "puppet", "science", "experiment", "statue", "toy", "labratory", "lab"],
    "spooky_objects_tools_or_weapons": ["#appliance_or_tool#", "#weapon#", "armor", "ring", "candy", "crown", "crystal ball", "masque", "scepter", "shield", "mask", "capsule", "mirror", "band", "artifact", "antique", "artifact", "relic"], # TODO: plural forms are riches?

    # Places
    # TODO: needs love!
    "plural_trapped_place": ["the slaughterhouse", "cages", "prison", "jail", "#threatening_substance#", "time"],
    "moment_in_time": ["#day_of_the_week#", "age", "era", "aeon", "eon", "day", "night", "year", "solstice", "time", "dawn", "rise", "dusk", "twilight"],
    "spooky_locale_without_the": [ "swamp", "island", "land", "park", "beach", "lake", "tower", "mountain", "hill", ],
    "spooky_locale": ["lighthouse", "pyramid", "void", "barren", "barrier", "caldera", "castle", "cave", "continent", "crater", "crypt", "dungeon", "field", "forest", "grave", "graveyard", "cemetery", "grotto", "hill", "hive", "island", "jungle", "keep", "kingdom", "lagoon", "lagoon", "lake", "mausoleum", "mine", "mountain", "rim", "ruin", "sands", "sepulcher", "shipwreck", "shores", "swamp", "throne", "tomb", "torture chamber", "tower", "valley", "vault", "volcano", "wilderness", "fortress", "labrynth", "pit", ],
    "dwelling_place": [ "village", "hotel", "house", "mansion", "fort", "stalag", "base", "barracks", "town", "colony", "cabin", "city", "realm", "zone"],
    "religious_buildings_with_the": ["church", "abbey", "cathedral", "pagoda", "chapel", "reliquary", "synagogue", "mosque", "temple", ],
    "unpleasant_places_with_the": [ "suburbs", "fair", "silo", "mall", "science fair", "DMV", "library", ],
    "water_and_oceans_with_the": [ "sea", "deep", "depths", "reef"],
    "cosmic_place": [ "time", "#star# #maybe_fun_numeral#", "#star#", "#named_planetary_body#", "asterid belt", "moon", "constellation", "black hole", "space", "eclipse", "continuum", "planet", "galaxy", "nebula", "dimension", "world", "star", "solar system"],

    # TODO: proper names --> merge with named threats?
	"star": [ "altair", "andromeda", "cygnus", "pegasus", "orion", "corona borealis", "cetus", "sol", "#greek_letter# centurai"],
    "named_planetary_body": ["phobos", "io", "mars", "mercury", "neptune", "jupiter", "pluto", "saturn", "titan", "uranus", "venus", "planet x",],
    "mythological_places": ["kingdom come", "hell", "dune", "elm street", "greenwich village", "eden", "atlantis", "troy", "Olympus", "Armageddon", "valhalla", "underworld", "astral plane", "miskatonic university", "Innsmouth", "hades", "avalon", "Ga'Hoole", "Shangra-La", "El Dorado", "Hyboria", "carcosa", "R'lyeh", "#greek_letter# Ceti #number#", "#greek_letter# Persei #number#", "vulcan", "lemuria", "leng"],

    "places_on_earth_without_the": ["Manhattan", "Antarctica", "Babylonia", "Basque Country", "Africa", "Baghdad",
                                    "Persia", "harlem", "berlin", "Bavaria", "Egypt", "L.A.", "New Jersey",
                                    "Tibet", "area 51", "groom lake", "main street USA", "mesoptamia", "mongolia",
                                    "siberia", "soviet russia", "tampa", "yucca flats"],

    "places_on_earth_with_the": ["Orient", "atlantic", "far #cardinal_direction#", "#cardinal_direction#", "nile", "north pole", "outback",
                                 "Himalayas", "pacific", "antarctic", "Zambezi", "amazon",],

    "scary_parts_of_a_house": ["attic", "basement", "bed", "cellar", "closet", "fireplace", "floorboards", "rug",
								"painting", "furnace", "trapdoor", "kitchen", "room", "sewer", "garden", "backyard",
								"shed", "stairs", "walls", "well", "crawlspace", "panic room"],

    "simple_places": [ "#cosmic_place#", "forever", "tomorrow", "the earth", "the future", "the year #funny_year#", "the 41st Millennium", "the center of the earth", "below", "beyond", "above", "underground", "20,000 fathoms"],

}

base_threats = {

    # Threats
    "named_threat": ["Spiderman", "Batman", "Wonder Woman", "Ra", "Hades", "Oberon", "Isis", "Ares", "Paimon", "Satan", "Dracula", "Medusa", "Hercules", "Sumuru", "Frankenstein", "Elvira", "Caligula", "Zorro", "Merlin"],

    "threatening_substance": ["web", "#drug#", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "grime", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],

    "evil_group": ["commission", "gestapo", "communist party", "illuminati", "secret society", "league", "triumvirate",
                   "demagogue", "billionaire", "cabal", "unamerican activity", "lizard person", "mafia", "Vatican",
                   "inner circle", "secret service", "CIA", "FBI", "Pentagon", "KGB", "congress", "SS", "council",
                   "anarchy", "domain", "alliance", "cult", "monarchy", "legion",
                   "fellowshiP", "reign", "empire", "army", "fighters", "warriors"],

    "threatening_thing": ["freak", "scum", "creep", "beast", "terror", "humanoids", "creature", "it", "thing", "threat",
                          "lurker", "being", "maniac", "corpse", "threat", "curse", "laugh", "call"],

    "natural_phenomena": ["avalanche", "planet", "galaxy", "comet", "sun", "star", "moon", "ash", "cloud", "comet",
                          "fire", "wave", "flood", "fog", "hail", "hurricane", "inferno", "mist", "pool", "rain",
                          "sandstorm", "shadow", "snow", "summer", "tornado", "typhoon", "vapor", "water", "wind",
                          "winter", "smoke", "smog", "twister", "drought", "earthquake", "tidal wave", "boulder",
						  "rockslide", "el nino", "plague"],

    "real_animal": ["horse", "owl", "whale", "eel", "lion", "amoeba", "virus", "orca", "bacteria", "anaconda", "ant",
                    "bat", "bear", "bee", "bird", "brood", "bunny", "cat", "centipede", "cheetah", "chicken", "dinosaur",
                    "dog", "eagle", "fish", "frog", "hound", "leech", "lizard", "maggot", "mantis", "mole", "razorback",
                    "piranha", "hedge", "tree", "shrub", "plant", "puma", "python", "rabbit", "raven", "scorpion", "seaweed",
                    "serpent", "shark", "snake", "spider", "termite", "tiger", "turtle", "vine", "vulture", "wasp", "worm",
                    "dolphin",],

    "fantasy_animal": ["sandworm", "revenant", "phantasm", "alien", "angel", "bigfoot", "chimera", "chupacabra", "cockatrice",
                       "cyborg", "demon", "dragon", "elf", "fairy", "fury", "gargoyle", "ghost", "ghoul", "giant", "gnome",
                       "goblin", "god", "golem", "gorgon", "gremlin", "grue", "hobgoblin", "homunculus", "hydra", "imp",
                       "kobold", "kraken", "leprechaun", "lepus", "leviathan", "lich", "lictor", "lycanthrope", "mermaid",
                       "merman", "monster", "mummy", "mutant", "ogre", "phoenix", "poltergeist", "santa claus", "sasquatch",
                       "satyr", "shapeshifter", "siren", "soul", "spectre", "spirit", "stalker", "troll", "undead", "unicorn",
                       "vampire", "werewolf", "wight", "yeti", "zombie", "snowwoman", "snowman", "robot", "automaton", "succubus",
                       "incubus", "spaceman", "spacewoman", "visitor", "mysterion"],

    "job": ["master", "mistress", "captain", "teacher", "messiah", "conciliator", "junkie", "enforcer", "gangster", "roadie",
            "cowboy", "vigilante", "vixen", "marquis", "student", "mom", "dad", "runner", "surfer", "hooker", "comptroller",
            "trucker", "engineer", "alchemist", "architect", "autarch", "avenger", "baron", "biker", "bureaucrat",
            "butcher", "cannibal", "cheerleader", "clown", "commander", "commando", "communist", "cop", "crusader", "cultist",
            "czar", "defender", "detective", "diver", "duke", "duplicator", "emperor", "empress", "exorcist", "football player",
            "geisha", "gladiator", "goddess", "groupie", "hunter", "invader",
            "king", "knight", "legionnaire", "legionary", "librarian", "lord", "luchador", "master", "ninja", "nun", "occultist", "pirate", "president", "priest", "prince",
            "princess", "private eye", "professor", "pyromaniac", "queen", "rabbi", "raider", "ronin", "samurai", "scientist",
            "secret agent", "seer", "servant", "slayer", "snatcher", "sorceror", "taxman", "trooper", "villager", "witch",
            "wizard", "astronaut", "renegade", "barbarian", "commando", "conqueror", "cop", "destroyer", "judge", "raider",
            "rider", "soldier", "surgeon", "thief", "warlock", "druid", "cleric", "preacher", "mage", "superhero",
            "supervillain", "hero", "villain", "harvester", "reanimator", "nurse"],

}
