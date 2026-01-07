# TODO: Move some space stuff back here?
# TODO: split back into objects and threats (subjects and objects) -- stuff
# might be in both lists?
# Or keep nouns that are sinister enough to be both (move ones that aren't into bot.y

def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines()]

base_nouns = {
    # Basic words  / vocabulary
    "relation": ["mom", "dad", "ex-wife", "ex-husband", "grandpa", "grandma", "step-father", "step-mother", "mother-in-law", "father-in-law", "father", "mother", "girlfriend", "boyfriend", "twin", "husband", "wife", "boss", "partner", "bride", "spouse", "groom", "baby", "offspring"],
    "drug": ["spice", "stimulant", "heroin", "psychedelic", "drug", "marijuana", "PCP", "cocaine", "LSD", "reefer", "ganja", "angel dust"],
    "portal": ["seal", "hole", "gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
    "food": [ "carrion", "fruit", "tomato", "water", "mushroom", "casserole", "toast", "mold", "egg", "tofu", "cheese"],
    "story": ["elegy", "legend", "secret", "cycle", "fable", "fate", "saga", "tale", "tales", ],
    "day_of_the_week": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
    "spooky_evidence": ["sigil", "talisman", "crop circles", "vision", "clue", "proof", "vestage", "vision", "stare", "track", "sign", "footprint", "fossil", "shadow", "touch", "sacrific", "whisper", "echo", "stench", "shard", "bone", "ruin", "trail"],
    "operation": ["codename", "protocol", "assignment", "phase", "operation", "plan", "conspiracy"],
    "battle": ["ambush", "siege", "attack", "battle", "clash", "revolution", "hunt", "counterattack", "battlefield", "bloodbath", "mutiny", "invasion", "war", "massacre", "holocaust"],
	"vehicle": ["car", "UFO", "black helicopter", "flying saucer", "train", "zeppelin", "truck", "rocket", "ship", "battleship", "aircraft carrier", "plane", "jet", "elevator", "tank", "spaceship", "starship", "scooter"],
    "shapes": ["square", "circle", "rune", "diagram", "pictogram", "geometry", "curve", "pyramid", "vector", "field", "color", "stain", "circle", "pentagram", "hexagon", "colour", "orb", "blob", "cube", "flash", "form", "monolith", "sphere", ],
    "body_part": ["body", "skin", "fist", "lip", "wing", "blood", "bone", "bun", "bosom", "brain", "claw", "eye", "finger", "flesh", "foot", "gut", "hand", "heart", "jaw", "maw", "mind", "mouth", "muscle", "skull", "face", "teeth", "brow", "spine", "stomach", "gaze", "tendril", "tentacle", ],
    "sexy_material": ["leather", "rubber", "g-string", "thong", "lace", "pvc", "latex", "lingerie"],
    "adventure": ["crusade", "romp", "quest", "escape", "voyage", "odyssey", "journey", "pilgrimage", "adventure", "expedition", "encounter"],
    "riches": ["diamonds", "riches", "bounty", "harvest", "gold", "treasure", "wealth", "fortune", "prosperity", "opulence"],
    "sound": ["requium", "symphony", "sound", "scream", "song", "melody", "song"],
    "scheme": ["coverup", "mutiny", "perversion", "study", "experiment", "destiny", "scheme", "grudge", "study", "plot", "revenge", "compact", "embrace", "pact", "bargain", "vigil", "betrayal", "lies", "promises", "wishes"],
    "concept": ["vice", "peace", "war", "vibe", "love", "horror", "beauty", "destiny", "evil", "doom", "damnation", "revenge", "madness", "damnation", "fear", "loathing", "wonder", "evil", "life", "chaos", "justice", "insanity", "nightmare", "hunger", "dream", "horror", "death", "urge", "fever", "consciousness", "nausea", "pain", "anguish", "eternity", "infinity", "sacrifice", "pestilence", "dogma", "courage", "vengence", "rage"],
    "magic": ["magic", "magick", "tome", "spellbook", "phylactery"],
    "instrament": ["guitar", "piano", "flute", "pan-pipes", "tubular bells"],
    "material" : ["water", "fire", "earth", "stone", "iron", "metal", "steel", "titanium", "aluminum", "cobalt", "plutonium", "thorium", "uranium", "gold", "silver", "lead", "wax", "clay", "crystal", "bone", "hollow", "glowing", "shining", "glittering"],
    "people": ["femme", "butch", "people", "men", "women"],
    "events": ["toast", "banquet", "dinner", "dance", "ball", "masquerade",],

    "appliance_tool_or_weapon": ["ark", "refrigerator", "saw", "hammer", "drill", "key", "coin", "lucre", "money", "crucifix", "dial", "mechanism", "chainsaw", "armor", "ring", "candy", "crown", "cross", "bible", "crystal ball", "masque", "scepter", "shield", "mask", "capsule", "mirror", "band", "antique", "artifact", "relic", "spear", "blade", "gun", "machine gun", "guillotine", "lance", "mace", "rifle", "saber", "sword", "blaster", "raygun", "nunchuck"],

    # simple meta rules
    "ritual": ["sabbath", "#color# mass", "dance", "rave", "concert", "festival", "funeral", "christmas", "opera", "orgy", "party", "pyre", "rite", "ritual", "sacrifice", "circus", "carnival", "bazzar", ],
    "human": [ "#person#", "broad", "gentle#person#", "teenager", "girl", "boy", "beefcake", "chick", "dude", "children", "daughter", "son", "bimbo", "nympho", "harlot"],
    "sexy_servant": [ "sex slave", "love servant", "sex toy", "lover", "concubine", "pleasure #job#"],
    "technology": ["#vehicle#", "space station", "test tube", "forcefield", "equations", "monument", "android", "computer", "doll", "effect", "factory", "gear", "hologram", "laser", "machine", "plane", "puppet", "science", "experiment", "statue", "toy", "labratory", "lab"],
    # TODO: plural forms are riches?

    # Threats

    "threatening_substance": ["chemtrail", "web", "#drug#", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "grime", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],
    "threatening_thing": ["AI", "freak", "scum", "creep", "beast", "terror", "humanoids", "creature", "it", "thing", "threat", "lurker", "being", "maniac", "corpse", "threat", "curse", "call", "reaper"],

    # short ones
    "human_reaction": ["smile", "shiver", "scream", "laugh", "frown", "scowl"],

    # TODO: some of these, eg harp, shouldn't use 'the'
    "evil_group":                       load("evil_groups"),
    "real_animal":                      load("real_animals"),
    "natural_phenomena":                load("natural_phenomena"),
    "fantasy_animal":                   load("fantasy_animals"),
    "job":                              load("jobs"),

    "ruler": ["king", "lord", "queen", "prince", "princess", "baron", "duke",
              "earl", "emperor", "kaiser", "pope", "Padishah", "vizier",
              "shogun", "Emir", "chieftain", "sheikh"],

    # Some threat meta...
    "all_animals": ["#fantasy_animal#", "#real_animal#"],
    #"threats": ["#named_threat#", "#threatening_substance#", "#evil_group#",
    #            "#threatening_substance#", "#evil_group#",
    #            "#threatening_thing#", "#human_reaction#",
    #            "#natural_phenomena#", "#real_animal#", "#fantasy_animal#",
    #            "#job#"],

}
