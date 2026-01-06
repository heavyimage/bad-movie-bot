import tracery
from tracery.modifiers import base_english

# Split up stuff!
from adjectives import base_adjectives
from nouns import base_nouns
from places import base_places_rt, base_places_nrt
from full_titles import full_titles



# TODO:sanity check duplicates
# TODO: sort out "the"

#named threats (don't want 'the' ahead of them

# the plane of leng
# adjective / noun agreement?
#"#magic_type_adj# #magic#",
# https://en.wikipedia.org/wiki/Erotic_thriller#1980s%E2%80%931990s:_Classic_period
"breed"
"wolf-man",
"filth"
"part XXX"
"invincible"
"grave",
"reign"
"country",
"school",
"barbed wire",
"revenge",
"fracture",
"sex",

# From: https://prowritingaid.com/list-of-words-not-capitalized-in-titles
DONT_CAP = ["a", "and", "as", "at", "be", "but", "became", "by", "down", "for", "from",
                   "if", "in", "into", "like", "near", "nor", "of", "off ",
                   "on", "once", "onto", "or", "over", "past", "so", "than",
                   "that", "to", "upon", "vs.", "was", "when", "with", "yet"]

RULES = {
    ##################### Basic Rules #######################

    # Putting them here means they won't be used as "nouns" or "adjectives"
	"cardinal_direction": ["north", "south", "east", "west"],
    "roman_numeral": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", ],
    "number": [ "2", "3", "4", "5", "6", "II", "III", "IV", "V", "VI", "VII", "#greek_letter#"],
    "title": [ "wing commander", "sgt.", "dr.", "mr.", "mrs.", "professor",],
    "letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x", "y", "z"],
    "numeric": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"],
    "funny_year": ["19XX", "20XX", "2000", "3001", "5000", "10,000"],
    "greek_letter": ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lamda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",],
    "large_count_singular_adj": ["uncountable", "endless", "hundred", "thousand", "million", "billion", "trillion"],
    "threat_suffix": ["nado", "geddon", "zilla", "drome"],
    "magic_type_adj": ["sex", "#color#", "dark", "evil", "nature"],
    "impossible_verb": ["couldn't", "wouldn't", "could never"],
    "person": ["man", "woman", "person", "robot"],
    "fear": ["fear", "dread", "avoid", "flee"],

    #"preposition": ["about", "above", "across", "after", "against", "among",
    #                "around", "at", "before", "behind", "below", "beside",
    #                "between", "beyond", "by", "down", "during", "for", "from", "in",
    #                "inside", "into", "near", "of", "off", "on", "out", "over",
    #                "through", "to", "toward", "under", "up", "with", "within"],
    # just use the ones that imply coming from somewhere
    "preposition": ["above", "across", "among",
                    "around", "at", "before", "behind", "below",
                    "beyond", "from", "in",
                    "inside", "near", "of", "on", "over",
                    "through", "to", "under", "with", "within"],

    "surname" :["#places_on_earth#", "#moment_in_time#", "#mythological_places#"
                , "#spooky_locale#", "Lee", "Jones", "Rodríguez", "Johnson",
                "Williams", "Gonzalez", "#color#", "Smith", "O'Brian"],


    # slightly meta here
    "fun_numeral": ["#roman_numeral#", "#greek_letter#"],

    # Load external 
    "adj": [f"#{adj}#" for adj in base_adjectives],
    "noun": [f"#{noun}#" for noun in base_nouns],
    "place_rt": [f"#{place}#" for place in base_places_rt],
    "place_nrt": [f"#{place}#" for place in base_places_nrt],

    ##### WTF ZONE ####
    # TODO:
    #"???": ["that came from", "corrupted by", "from beyond", "on the edge of", "above the"]
    
    # Verbs?
    "ominous_place_actions": ["explored", "studied", "walked", "was sent to", "traveled to", "returned from", "woke up in", "was transported to"],
    "ominous_noun_actions_past": ["watched", "killed", "froze", "burned", "ate", "tortured", "dissected", "dissolved", "studied", "became", "married", "swallowed"],
    "ominous_noun_actions_present": ["kill", "freeze", "burn", "eat", "torture", "dissect", "dissolve", "study", "become", "marry", "swallow"],
    
    #### COMPOUND RULES ####

    # Maybes
    "maybe_adj":         ["", "", "#adj#"],
    "maybe_old_adj":     ["", "#old_adj#"],
    "maybe_fun_numeral": ["", "#roman_numeral#", "#greek_letter#"],
    "maybe_the":         ["", "the"],
    "maybe_adj_place":   ["#maybe_adj# #smart_place#"],

    "smart_place": ["the #place_rt#", "#place_nrt#"],
    "smart_ma_place": ["the #maybe_adj# #place_rt#", "#maybe_adj# #place_nrt#"],

    # Basics
    "ma_noun":       ["#maybe_adj# #noun#", ],
    "ma_nouns": ["#maybe_adj# #noun.s#", ],


    ### title encomplexification ###

	# TODO: replace #place# with #maybe_adj_#place"
    "silly_sequels" : [
        "#smart_place# #number#: The #ma_noun#",
        "#smart_place# #number#: Return of the #ma_noun#",
        "#smart_place# #number#: Chapter #fun_numeral",
        "#smart_place# #number#: Revenge of the #ma_noun#",
        "#smart_place# #number#: #ma_noun# #noun#",
        "#smart_place# #number#: #noun# of the #ma_noun#",
        "#ma_noun# #number#: #preposition# #smart_place#",
        "The #ma_noun# #number#: #preposition# #smart_place#",
        "The #ma_noun# #number#: #smart_place#",
    ],
    "silly_suffix": [
        "! kill! kill!",
        " a go-go",
        " (yellow)",
        " (blue)",
        ": The revenge",
        ": The return",
        ": #space_age_adj# #ritual#",
        ": #story# of the #noun#",
        " XXX",
    ],

    "silly_prefix": [
        "Manos: The #noun.s# of",
        "Code Name:",
        "David Winters presents:",
        "Alias:",
        "Danger!!",
        "Warning:",
        "Fear the",
        "Dread the",
    ],

    
}

# Load remote lists
RULES.update(base_adjectives)
RULES.update(base_nouns)
RULES.update(base_places_rt)
RULES.update(base_places_nrt)
RULES['full_title'] = full_titles

# TODO: capitalize both parts of a hyphenation
def custom_capitalize(text):
    capitalized_words = []
    for word in text.split():
        if word.lower in DONT_CAP:
            capitalized_words.append(word)
        else:
            if len(word) == 1:
                fix = word
            elif "-" in word:
                fix = "-".join([custom_capitalize(c) for c in word.split("-")])
            elif word[0] == "'":
                fix = f"'{word[1].upper()}{word[2:]}"
            else:
                fix = f"{word[0].upper()}{word[1:]}"
            capitalized_words.append(fix)
    result = ' '.join(capitalized_words)
    if len(result) == 0:
        return ""
    return result[0].upper() + result[1:]


def clean(title):
    ## merge adjectives / prefixes / suffixes
    #title = title.replace("- ", "")
    #title = title.replace(" -", "")
    #title = title.replace("  ", " ")

    ## fix spacing
    #title = title.replace("' ", "'")
    #title = title.replace(" : ", ": ")

    # fix plurals
    title = title.replace("teethes", "teeth")
    title = title.replace("womans", "women")
    title = title.replace(" mans ", " men ")
    title = title.replace("elfs", "elves")
    title = title.replace("nauseas", "nausea")
    title = title.replace("bloods", "blood")
    title = title.replace("foots", "feet")
    title = title.replace("gentlemans", "gentlemen")
    title = title.replace("gentlewomans", "gentlewomen")
    title = title.replace("spacemans", "spacemen")
    title = title.replace("spacewomans", "spacewomen")
    title = title.replace("snowmans", "snowmen")
    title = title.replace("snowwomans", "snowwomen")

    # capitalize
    #title = title.strip().title()
    title = custom_capitalize(title.strip())

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
    
    return title


def main():
    grammar = tracery.Grammar(RULES)
    grammar.add_modifiers(base_english)
    for i in range(1000):
        title = grammar.flatten("#full_title#")

        title = clean(title)

        print(title)

if __name__ == "__main__":
    main()
