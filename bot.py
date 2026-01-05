import tracery
from tracery.modifiers import base_english

# Split up stuff!
from adjectives import base_adjectives
from nouns import base_nouns, base_threats
from full_titles import full_titles



# TODO:sanity check duplicates
# TODO: sort out "the"
# TODO: 'form' is too vague...

#named threats (don't want 'the' ahead of them

# the plane of leng
# sort adverbs
# adjective / noun agreement?
#"#magic_type_adj# #magic#",
# https://en.wikipedia.org/wiki/Erotic_thriller#1980s%E2%80%931990s:_Classic_period
"breed"
"wolf-man",
"filth"
"part XXX"
"invincible"
"#threat# lives"
"murderous"
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
	"cardinal_direction": ["north", "south", "east", "west"],
    "roman_numeral": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", ],
    "number": [ "2", "3", "4", "5", "6", "II", "III", "IV", "V", "VI", "VII", "#greek_letter#"],
    "title": [ "dr.", "mr.", "mrs.", "professor",],
    "letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x", "y", "z"],
    "funny_year": ["19XX", "20XX", "2000", "3001", "5000", "10,000"],
    "greek_letter": ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa",
                     "lamda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",],
    "day_of_the_week": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],


    # Load external 
    "adj": [f"#{adj}#" for adj in base_adjectives],
    "noun": [f"#{noun}#" for noun in base_nouns],
    "threat": [f"#{threat}#" for threat in base_threats],



    ##### WTF ZONE ####
    # TODO:
    #"events": ["toast"],
    "moved" : ["walked into", "was sent to", "traveled to", "returned from", "came back from", "time-traveled to", "slid into", "fell into", "was transported to", ],
    "adverb": ["of", "in", "to", "that came from", "from", "before", "corrupted by", "from beyond", "on", "on the edge of", "beyond", "inside", "above", "within"],
    "surname" :["#places_on_earth_with_the#", "#places_on_earth_without_the#", "#moment_in_time#", "#mythological_places#" , "#spooky_locale_without_the#", "#spooky_locale#", "Jones", "Smith", "O'Brian"],
    
    #### COMPOUND RULES ####

    # Maybes
    "maybe_adj":         ["", "", "#adj#"],
    "maybe_old_adj":     ["", "#old_adj#"],
    "maybe_fun_numeral": ["", "#roman_numeral#", "#greek_letter#"],
    "maybe_the":         ["", "the"],

    # Basics
    "form":       ["#maybe_adj# #threat#", ],
    "pluralform": ["#maybe_adj# #threat.s#", ],
    "fun_numeral": ["#roman_numeral#", "#greek_letter#"],

    "place_without_the" : [
        "#water_and_oceans_with_the#",
        "#places_on_earth_with_the#",
        "#unpleasant_places_with_the#",
        "#scary_parts_of_a_house#",
        "#spooky_locale#",
        "#religious_buildings_with_the#",
    ],

    "place_with_the" : [
        "#plural_trapped_place#",
        "#mythological_places#",
        "#places_on_earth_without_the#",
        "#spooky_locale_without_the#",
        "#dwelling_place#",
    ],

    "place": [
        "#simple_places#",
        "the #place_without_the#",
        "#place_with_the#",
    ],

    "may_adj_place": [
        "the #maybe_adj# #place_without_the#",
        "#maybe_adj# #place_with_the#",
    ],

    ### title encomplexification ###

	# TODO: replace #place# with #maybe_adj_#place"
    "silly_sequels" : [
        "#place# #number#: The #form#",
        "#place# #number#: Return of the #form#",
        "#place# #number#: Chapter #fun_numeral",
        "#place# #number#: Revenge of the #form#",
        "#place# #number#: #form# #noun#",
        "#place# #number#: #noun# of the #form#",
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
RULES.update(base_threats)
RULES['full_title'] = full_titles

# TODO: capitalize both parts of a hyphenation
def custom_capitalize(text):
    capitalized_words = []
    #print(">>>" + text + "<<<")
    for word in text.split():
        if word.lower in DONT_CAP:
            capitalized_words.append(word)
        else:
            #print(word)
            if len(word) == 1:
                fix = word
            elif "-" in word:
                fix = "-".join([custom_capitalize(c) for c in word.split("-")])
            elif word[0] == "'":
                fix = f"'{word[1].upper()}{word[2:]}"
            else:
                fix = f"{word[0].upper()}{word[1:]}"
            capitalized_words.append(fix)
    return ' '.join(capitalized_words)


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
    title = title.replace(" mans", " men")
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
