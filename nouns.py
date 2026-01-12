# TODO: Move some space stuff back here?
# TODO: split back into objects and threats (subjects and objects) -- stuff
# might be in both lists?
# Or keep nouns that are sinister enough to be both (move ones that aren't into bot.y

def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

base_nouns = {
    # Basic words  / vocabulary
    # short ones
    "day_of_the_week": load("days_of_the_week"),
    "human_reaction": load("human_reactions"),
    "instrament": load("instraments.txt"),
    "magic": load("magic_stuff"),
    "operation": load("operations"),

    "people": ["femme", "people", "men", "women", "god"],
    "portal": ["seal", "hole", "gate", "door", "gateway", "doorway", "passage", "portal", "tunnel", "bridge"],
    "sexy_material": ["leather", "rubber", "g-string", "thong", "lace", "PVC", "latex", "lingerie"],
    "sound": ["requium", "symphony", "sound", "scream", "song", "melody", "song"],

    "story": load("stories"),
    "relation": load("relations"),
    "drug": load("drugs"),
    "food": load("food"),
    "spooky_evidence": load("spooky_evidence"),
    "battle": load("battles"),
    "vehicle": load("vehicles"),
    "shapes": load("shapes"),
    "body_part": load("body_parts"),
    "adventure": load("adventures"),
    "riches": load("riches"),
    "scheme": load("schemes"),
    "concept": load("concepts"),
    "material" : load("materials"),
    "appliance_tool_or_weapon": load("appliance_tool_or_weapon"),
    "time": load("times"),
    "dorks": load("dorks"),

    # simple meta rules
    "ritual_or_event": load("rituals"),
    "human": load("humans"),
    "sexy_servant": ["sex slave", "love servant", "sex toy", "lover", "concubine", "pleasure #job#"],
    "technology": ["#vehicle#", "space station", "clone", "test tube", "forcefield", "equations", "monument", "robot", "android", "computer", "doll", "effect", "factory", "gear", "hologram", "laser", "machine", "plane", "puppet", "science", "experiment", "statue", "toy", "labratory", "lab"],
    # TODO: plural forms are riches?

    # Threats
    "threatening_substance": ["chemtrail", "web", "#drug#", "blood", "slime", "meat", "poison", "elixir", "dust", "stuff", "oil", "ooze", "goop", "sludge", "goo", "ichor", ],
    "threatening_thing": load("threatening_things"),

    # TODO: some of these, eg harp, shouldn't use 'the'
    "evil_group":                       load("evil_groups"),
    "real_animal":                      load("real_animals"),
    "natural_phenomena":                load("natural_phenomena"),
    "fantasy_animal":                   load("fantasy_animals"),
    "job":                              load("jobs"),
    "ruler": load("rulers"),

    # Some threat meta...
    "all_animals": ["#fantasy_animal#", "#real_animal#"],
    #"threats": ["#named_threat#", "#threatening_substance#", "#evil_group#",
    #            "#threatening_substance#", "#evil_group#",
    #            "#threatening_thing#", "#human_reaction#",
    #            "#natural_phenomena#", "#real_animal#", "#fantasy_animal#",
    #            "#job#"],

}
