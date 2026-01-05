# TODO: Move some space stuff back here?
# TODO: split back into objects and threats (subjects and objects) -- stuff might be in both lists!

base_nouns = {
    # Basic words  / vocabulary
    "relation": ["mom", "dad", "ex-wife", "ex-husband", "grandpa", "grandma", "step-father", "step-mother", "mother-in-law", "father-in-law", "father", "mother", "girlfriend", "boyfriend", "twin", "husband", "wife", "boss", "partner", "bride", "spouse", "groom", "mate", "baby", "offspring"],
    "drug": ["spice", "stimulant", "heroin", "psychedelic", "drug", "marijuana", "pcp", "cocaine", "LSD", "reefer", "ganja", "angel dust"],
    "portal": ["hole", "gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
    "food": [ "carrion", "fruit", "tomato", "water", "mushroom", "casserole", "toast", "mold", "egg", "tofu", "cheese"],
    "appliance_or_tool": ["refrigerator", "saw", "hammer", "shovel", "drill", "key",],
    "weapon": ["spear", "blade", "gun", "machine gun", "guillotine", "lance", "mace", "rifle", "saber", "sword", "blaster", "raygun", "nunchuck"],
    "person": ["man", "woman", "person"],
    "story": ["elegy", "legend", "secret", "cycle", "fable", "fate", "saga", "tale", "tales", ],
    "day_of_the_week": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
    "spooky_evidence": ["crop circles", "vision", "clue", "proof", "vestage", "vision", "stare", "track", "sign", "footprint", "fossil", "shadow", "touch", "sacrific", "whisper", "echo", "stench", "shard", "bone", "ruin", "trail"],
    "operation": ["protocol", "assignment", "phase", "operation", "plan", "conspiracy"],
    "battle": ["siege", "attack", "battle", "clash", "revolution", "hunt", "counterattack", "battlefield", "bloodbath", "mutiny", "invasion", "war", "massacre", "holocaust"],
	"vehicle": ["car", "ufo", "flying saucer", "train", "zeppelin", "truck", "rocket", "ship", "battleship", "aircraft carrier", "plane", "jet", "elevator", "tank", "spaceship", "starship", "scooter"],
    "shapes": ["geometry", "curve", "pyramid", "vector", "field", "color", "stain", "circle", "pentagram", "hexagon", "element", "colour", "orb", "blob", "cube", "flash", "form", "monolith", "sphere", ],
    "body_part": ["body", "skin", "fist", "lip", "wing", "blood", "bone", "bun", "bosom", "brain", "claw", "eye", "finger", "flesh", "foot", "gut", "hand", "heart", "jaw", "maw", "mind", "mouth", "muscle", "skull", "face", "teeth", "brow", "spine", "stomach", "gaze", "tendril", "tentacle", ],
    "sexy_material": ["the buff", "leather", "rubber", "g-string", "thong", "lace", "pvc", "latex", "lingerie"],
    "adventure": ["quest", "escape", "voyage", "odyssey", "journey", "pilgrimage", "adventure", "expedition", "encounter"],
    "riches": ["diamonds", "riches", "bounty", "harvest", "gold", "treasure", "wealth", "fortune", "prosperity", "opulence"],
    "sound": ["sound", "scream", "song", "melody", "song"],
    "scheme": ["study", "experiment", "destiny", "scheme", "grudge", "study", "plot", "revenge", "compact", "embrace", "pact", "bargain", "vigil", "betrayal", "lies", "promises", "wishes"],
    "concept": ["vice", "love", "horror", "beauty", "evil", "doom", "damnation", "revenge", "madness", "damnation", "fear", "loathing", "wonder", "evil", "life", "chaos", "justice", "insanity", "nightmare", "hunger", "dream", "horror", "death", "urges", "fever", "consciousness", "nausea", "pain", "anguish", "eternity", "infinity", "sacrifice", "pestilence", "dogma", "courage", "vengence", "rage"],
    "magic": ["magic", "magick", "tome", "spellbook", "phylactery"],
    "instrament": ["guitar", "piano", "flute", "pan-pipes", "tubular bells"],
    "material" : ["water", "fire", "earth", "stone", "iron", "metal", "stainless steel", "titanium", "aluminum", "cobalt", "plutonium", "thorium", "uranium", "gold", "silver", "lead", "wax", "clay", "crystal", "bone", "hollow", "glowing", "shining", "glittering"],

    # simple meta rules
    "ritual": ["sabbath", "#color# mass", "dance", "rave", "concert", "festival", "funeral", "christmas", "opera", "orgy", "party", "pyre", "rite", "ritual", "sacrifice", "circus", "carnival", "bazzar", ],
    "human": [ "#person#", "broad", "gentle#person#", "teenager", "girl", "boy", "beefcake", "chick", "dude", "children", "daughter", "son", "bimbo", "nympho", "harlot"],
    "sexy_servant": [ "sex slave", "love servant", "sex toy", "lover", "concubine", "pleasure #job#"],
    "technology": ["#vehicle#", "space station", "test tube", "forcefield", "equations", "monument", "android", "computer", "doll", "effect", "factory", "gear", "hologram", "laser", "machine", "plane", "puppet", "science", "experiment", "statue", "toy", "labratory", "lab"],
    "spooky_objects_tools_or_weapons": ["chainsaw", "#appliance_or_tool#", "#weapon#", "armor", "ring", "candy", "crown", "cross", "bible", "crystal ball", "masque", "scepter", "shield", "mask", "capsule", "mirror", "band", "artifact", "antique", "artifact", "relic"], # TODO: plural forms are riches?

    # Threats
    "named_noun": ["The Devil", "Spiderman", "Batman", "Wonder Woman", "Ra", "Hades", "Oberon", "Isis", "Ares", "Paimon", "Satan", "Dracula", "Medusa", "Hercules", "Sumuru", "Frankenstein", "Elvira", "Caligula", "Zorro", "Merlin"],

    "threatening_substance": ["web", "#drug#", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "grime", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],

    "evil_group": ["commission", "gestapo", "communist party", "illuminati", "secret society", "league", "triumvirate",
                   "demagogue", "billionaire", "cabal", "unamerican activity", "lizard person", "mafia", "Vatican",
                   "inner circle", "secret service", "CIA", "FBI", "Pentagon", "KGB", "congress", "SS", "council",
                   "anarchy", "domain", "alliance", "cult", "monarchy", "legion",
                   "fellowship", "empire", "army", "fighters", "warriors"],

    "threatening_thing": ["freak", "scum", "creep", "beast", "terror", "humanoids", "creature", "it", "thing", "threat",
                          "lurker", "being", "maniac", "corpse", "threat", "curse", "call"],

    "human_reaction": ["smile", "shiver", "scream", "laugh", "frown", "scowl"],

    "natural_phenomena": ["avalanche", "planet", "galaxy", "comet", "sun", "star", "moon", "ash", "cloud", "comet",
                          "fire", "wave", "flood", "fog", "hail", "hurricane", "inferno", "mist", "pool", "rain",
                          "sandstorm", "shadow", "snow", "summer", "tornado", "typhoon", "vapor", "water", "wind",
                          "winter", "smoke", "smog", "twister", "drought", "earthquake", "tidal wave", "boulder",
						  "rockslide", "el nino", "plague", "outbreak", "pandemic"],

    "real_animal": ["horse", "owl", "whale", "eel", "lion", "amoeba", "virus", "orca", "bacteria", "anaconda", "ant",
                    "bat", "bear", "bee", "bird", "brood", "bunny", "cat", "centipede", "cheetah", "chicken", "dinosaur",
                    "dog", "eagle", "fish", "frog", "hound", "leech", "lizard", "maggot", "mantis", "mole", "razorback",
                    "piranha", "hedge", "tree", "shrub", "plant", "puma", "python", "rabbit", "raven", "scorpion", "seaweed",
                    "serpent", "shark", "snake", "spider", "termite", "tiger", "turtle", "vine", "vulture", "wasp", "worm",
                    "dolphin", "squid", "octopus", "pussycat"],

    "fantasy_animal": ["pegasus", "sandworm", "revenant", "phantasm", "alien", "angel", "bigfoot", "chimera", "chupacabra", "cockatrice",
                       "cyborg", "demon", "dragon", "elf", "fairy", "fury", "gargoyle", "ghost", "ghoul", "giant", "gnome",
                       "goblin", "god", "golem", "gorgon", "gremlin", "grue", "hobgoblin", "homunculus", "hydra", "imp",
                       "kobold", "kraken", "leprechaun", "lepus", "leviathan", "lich", "lictor", "lycanthrope", "mermaid",
                       "merman", "monster", "mummy", "mutant", "ogre", "phoenix", "poltergeist", "santa claus", "sasquatch",
                       "satyr", "shapeshifter", "siren", "soul", "spectre", "spirit", "stalker", "troll", "undead", "unicorn",
                       "vampire", "werewolf", "wight", "yeti", "zombie", "snowwoman", "snowman", "robot", "automaton", "succubus",
                       "incubus", "spaceman", "spacewoman", "visitor", "mysterion"],

    "job": ["master", "mistress", "captain", "teacher", "messiah", "conciliator", "junkie", "enforcer", "gangster", "roadie",
            "cowboy", "vigilante", "vixen", "marquis", "student", "runner", "surfer", "hooker", "comptroller",
            "trucker", "engineer", "alchemist", "architect", "autarch", "avenger", "baron", "biker", "bureaucrat",
            "butcher", "cannibal", "cheerleader", "clown", "commander", "commando", "communist", "cop", "crusader", "cultist",
            "czar", "defender", "detective", "diver", "duke", "duplicator", "emperor", "empress", "exorcist", "football player",
            "geisha", "gladiator", "goddess", "groupie", "hunter", "invader",
            "king", "knight", "legionnaire", "legionary", "librarian", "lord", "luchador", "master", "ninja", "nun", "occultist", "pirate", "president", "priest", "prince",
            "princess", "private eye", "professor", "pyromaniac", "queen", "rabbi", "raider", "ronin", "samurai", "scientist",
            "secret agent", "seer", "servant", "slayer", "snatcher", "sorceror", "taxman", "trooper", "villager", "witch",
            "wizard", "astronaut", "renegade", "barbarian", "commando", "conqueror", "cop", "destroyer", "judge", "raider",
            "rider", "soldier", "surgeon", "thief", "warlock", "druid", "cleric", "preacher", "mage", "superhero",
            "supervillain", "hero", "villain", "harvester", "reanimator",
            "nurse", "schoolgirl", "boozehound", "addict", "POW", "hitchiker"],

}
