import tracery
from tracery.modifiers import base_english

from common import load, testload

import logging
import time
from random import choice
from mastodon import Mastodon

HASHTAG_INTERVAL = 30
HASHTAGS = ["#cinema", "#flims", "#movies", "#badmovie", "#schlock", "#bmovie"]

REMOVE_ARTICLE = [
    "Palantir",
    "CERN",
    "George Soros",
    "Generation X",
    "HAARP",
    "Majestic 12",
    "Opus Dei",
]

PLURAL_FIXES = {
    "Wines": "Wine",
    "Teethes": "Teeth",
    "Tearses": "Tears",
    "Stuffs": "Stuff",
    " Mans": " Men",
    " Mens": " Men",
    " Womens": " Women",
    " Womans": " Women",
    "Elfs": "Elves",
    "Cheetahes": "Cheetahs",
    "Barbarianses": "Barbarians",
    "Millenialses": "Millenials",
    "Nauseas": "Nausea",
    "Bloods": "Blood",
    " Foots": " Feet",
    "Gentlemans": "Gentlemen",
    "Gentlewomans": "Gentlewomen",
    "Spacemans": "Spacemen",
    "Spacewomans": "Spacewomen",
    "Snowmans": "Snowmen",
    "Snowwomans": "Snowwomen",
}

# Split up stuff!
from adjectives import base_adjectives
from nouns import base_nouns
from places import base_places_rt, base_places_nrt
from main_titles import main_titles

# Setup logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:\t%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger = logging.getLogger()

def get_api():
    """ Access and authorize mastodon using secret token file """
    api = Mastodon(
        access_token = 'token.secret',
        api_base_url = 'https://mastodon.social/'
    )
    return api

def get_all_followers(api):
    """ Get the accounts we are following and keep only the account names """
    accounts = []
    user_id = api.account_verify_credentials().id
    following = api.account_followers(user_id)
    while following != None :
        accounts += list(map(lambda x: x.acct, following))
        following = api.fetch_next(following)
    return accounts

# From: https://prowritingaid.com/list-of-words-not-capitalized-in-titles
DONT_CAP = ["a", "and", "as", "at", "be", "but", "became", "by", "down", "for", "from",
                   "if", "in", "into", "like", "near", "nor", "of", "off ",
                   "on", "once", "onto", "or", "over", "past", "so", "than",
                   "that", "to", "upon", "vs.", "was", "when", "with", "yet"]

RULES = {
    ##################### Basic Rules #######################

    # Putting them here means they won't be used as "nouns" or "adjectives"
	"cardinal_direction": ["north", "south", "east", "west"],

    # numbers
    "roman_numeral": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
    "greek_letter": ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lamda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",],
    "digit" :["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    # slighty meta here...
    "fun_number": ["#digit#", "#roman_numeral#", "#greek_letter#"],

    # Years
    "maybe_era": ["AD", "BC", ""],
    "funny_year": ["year 0", "41st Millennium", "19XX", "20XX", "1999", "2000", "2001", "3001", "5000", "10,000", "#digit##digit##digit##digit# #maybe_era#", "#digit##digit##digit##digit##digit# #maybe_era#", "#digit##digit##digit##digit##digit##digit# #maybe_era#"],

    "title": ["sgt.", "dr.", "mr.", "mrs.", "professor",],
    "letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x", "y", "z"],
    "nato_alphabet": ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu "],
    "numeric": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"],

    "large_count_singular_adj": ["uncountable", "endless", "hundred", "thousand", "million", "billion", "trillion"],
    "threat_suffix": ["nado", "geddon", "zilla", "drome", "ra"],
    "magic_type_adj": ["sex", "#color#", "dark", "evil", "nature"],
    "impossible_verb": ["couldn't", "wouldn't", "could never"],
    "fear": ["fear", "dread", "avoid", "flee"],


    # just use the ones that imply coming from somewhere
    # TODO: split into for nouns and places?
    "preposition": ["above", "across", "among",
                    "around", "at", "before", "behind", "below",
                    "beyond", "from", "in",
                    "inside", "near", "of", "on", "over",
                    "through", "to", "under", "with", "within", "that came to"],

    # names (some meta)
    "name": load("names"),
    "surname": load("surnames"),

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
    "ominous_noun_actions_present": ["kill", "freeze", "fertilize", "burn", "eat", "torture", "dissect", "dissolve", "study", "become", "marry", "swallow"],

    # Maybes
    "maybe_adj":         ["", "", "#adj#"],
    "maybe_old_adj":     ["", "#old_adj#"],
    "maybe_fun_numeral": ["", "#roman_numeral#", "#greek_letter#"],
    "maybe_the":         ["", "the"],
    "maybe_adj_place":   ["#maybe_adj# #smart_place#"],

    "smart_place": ["the #place_rt#", "#place_nrt#"],
    "smart_ma_place": ["the #maybe_adj# #place_rt#", "#maybe_adj# #place_nrt#"],
    "smart_a_place": ["the #adj# #place_rt#", "#adj# #place_nrt#"],

    # Basics
    "ma_noun":       ["#maybe_adj# #noun#", ],
    "ma_nouns": ["#maybe_adj# #noun.s#", ],


    ### title encomplexification ###

	# TODO: replace #place# with #maybe_adj_#place"
    "silly_sequel" : [
        "#main_title# #fun_number#: The #ma_noun#",
        "#main_title# #fun_number#: Return of the #ma_noun#",
        "#main_title# #fun_number#: Chapter #fun_number#",
        "#main_title# #fun_number#: Revenge of the #ma_noun#",
        "#main_title# #fun_number#: The Squeakquel",
        "#main_title# #fun_number#: #ma_noun# #noun#",
        # ...Secret of the ooze
        "#main_title# #fun_number#: #noun# of the #ma_noun#",
        "#main_title# #fun_number#: and the #noun# of the #ma_noun#",
        "#main_title# #fun_number#: #preposition# #smart_place#",
        "#main_title# #fun_number#: #preposition# #smart_place#",
        "#main_title# #fun_number#: #smart_place#",
    ],


    "silly_suffix": [
        "! kill! kill!",
        " a go-go",
        " (Yellow)",
        " (Blue)",
        ": The revenge",
        ": The return",
        ": #space_age_adj# #ritual_or_event#",
        ": #adventure# of the #noun#",
        " XXX",
    ],

    "silly_prefix": [
        "Transformers #digit##digit#: ",
        "Code Name:",
        "David Winters presents:",
        "Uwe Boll presents:",
        "Alias:",
        "Danger!!",
        "Warning:",
        "Fear the",
        "Dread the",
        "Tyler Perry’s",
    ],

    "full_title" : [
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",
        "#main_title#",

        "#alternate#",
        ],

    # Alternate titles that happen rarely
    "alternate": [
        # sequels
        "#silly_sequel#",

        # prefix and suffix
        "#silly_prefix# #main_title.capitalize#",
        "#main_title# #silly_suffix#",
    ],


}

# Load remote lists
RULES.update(base_adjectives)
RULES.update(base_nouns)
RULES.update(base_places_rt)
RULES.update(base_places_nrt)
RULES['main_title'] = main_titles

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
    # capitalize
    title = custom_capitalize(title.strip())

    # fix plurals
    for k,v in PLURAL_FIXES.items():
        title = title.replace(k, v)

    # some orgs NEVER have 'the' 
    # TODO: kinda gross to hard code this...
    for org in REMOVE_ARTICLE:
        title = title.replace(f"The {org}", f"{org}")
        title = title.replace(f"the {org}", f"{org}")

    title = title.replace("' ", "'") # they called me ' alpha'

    # fix title case errors
    title = title.replace(" And ", " and ")
    title = title.replace("'S ", "'s ")
    title = title.replace(" Of ", " of ")
    title = title.replace(" The ", " the ")
    title = title.replace("'T ", "'t ")
    title = title.replace(" : ", ": ")
    title = title.replace("- ", "-")
    title = title.replace("41St", "41st")


    # HACK to fix eg "I was in league with a android"
    # a --> for vowel words
    for vowel in "aeiou":
        title = title.replace(f" a {vowel.upper()}", f" an {vowel.upper()}")

    return title


def main():
    """ entry point """

    # build gammar
    grammar = tracery.Grammar(RULES)
    grammar.add_modifiers(base_english)

    counter = 0
    followers = set()

    logger.info("Serving: https://mastodon.social/@z_movie_generator")

    # get api object
    api = get_api()

    # Main loop
    while True:

        # generate the title!
        title = clean(grammar.flatten("#full_title#"))

        # toot
        msg = title
        if (counter + 1) % HASHTAG_INTERVAL == 0:
            msg = f"{msg} {choice(HASHTAGS)}"
        api.status_post(msg)
        counter += 1

        # log
        logger.info("Posted msg #%s: %s" % (counter, msg))

        # Check for new followers:
        for handle in get_all_followers(api):
            if handle not in followers:
                logger.info("New Follower: %s" % handle)
                followers.add(handle)

        # sleep for 1 hour
        time.sleep(60 * 60)

def test():
    for i in range(1000):
        grammar = tracery.Grammar(RULES)
        grammar.add_modifiers(base_english)
        title = clean(grammar.flatten("#full_title#"))
        print(title)

if __name__ == "__main__":
    main()
    #test()
