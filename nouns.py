# TODO: Move some space stuff back here?
# TODO: split back into objects and threats (subjects and objects) -- stuff
# might be in both lists?
# Or keep nouns that are sinister enough to be both (move ones that aren't into bot.y

def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

base_nouns = {
    # Basic words  / vocabulary
    "day_of_the_week": load("days_of_the_week"),
    "human_reaction": load("human_reactions"),
    "instrament": load("instraments"),
    "magic": load("magic_stuff"),
    "operation": load("operations"),
    "people": load("people"),
    "portal": load("portals"),
    "sexy_material": load("sexy_materials"),
    "sound": load("sounds"),
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
    "ritual_or_event": load("rituals"),
    "threatening_thing": load("threatening_things"),

    # simple meta rules
    "human": 				load("humans"),
    "sexy_servant": 			load("sexy_servants"),
    "technology": 			load("technology"),
    "threatening_substance": 		load("threatening_substances"),

    # "threats"
    "real_animal":                      load("real_animals"),
    "natural_phenomena":                load("natural_phenomena"),
    "fantasy_animal":                   load("fantasy_animals"),
    "job":                              load("jobs"),
    "ruler": 				load("rulers"),
    # meta rules
    # TODO: some of these, eg harp, shouldn't use 'the'
    "evil_group":                       load("evil_groups"),
    "all_animals": ["#fantasy_animal#", "#real_animal#"],
    #"threats": ["#named_threat#", "#threatening_substance#", "#evil_group#",
    #            "#threatening_substance#", "#evil_group#",
    #            "#threatening_thing#", "#human_reaction#",
    #            "#natural_phenomena#", "#real_animal#", "#fantasy_animal#",
    #            "#job#"],

}
