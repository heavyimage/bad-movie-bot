import tracery
from tracery.modifiers import base_english

import logging
import time
from random import choice
from mastodon import Mastodon

HASHTAG_INTERVAL = 10
HASHTAGS = ["#cinema", "#flims", "#movies", "#badmovie#"]

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

# TODO:
# sanity check duplicates
# named threats (don't want 'the' ahead of them
# the plane of leng
# adjective / noun agreement?
#"#magic_type_adj# #magic#",
# https://en.wikipedia.org/wiki/Erotic_thriller#1980s%E2%80%931990s:_Classic_period
# "breed"
# "wolf-man",
# "filth"
# "part XXX"
# "invincible"
# "grave",
# "reign"
# "country",
# "school",
# "barbed wire",
# "revenge",
# "fracture",
# "sex",

# From: https://prowritingaid.com/list-of-words-not-capitalized-in-titles
DONT_CAP = ["a", "and", "as", "at", "be", "but", "became", "by", "down", "for", "from",
                   "if", "in", "into", "like", "near", "nor", "of", "off ",
                   "on", "once", "onto", "or", "over", "past", "so", "than",
                   "that", "to", "upon", "vs.", "was", "when", "with", "yet"]

def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines()]

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
    "numeric": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"],

    "large_count_singular_adj": ["uncountable", "endless", "hundred", "thousand", "million", "billion", "trillion"],
    "threat_suffix": ["nado", "geddon", "zilla", "drome", "ra"],
    "magic_type_adj": ["sex", "#color#", "dark", "evil", "nature"],
    "impossible_verb": ["couldn't", "wouldn't", "could never"],
    "person": ["man", "woman", "person", "robot"],
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
    "surname" :["#places_on_earth#", "#moment_in_time#", "#mythological_places#"
                , "#spooky_locale#", "Lee", "Jones", "Rodríguez", "Johnson",
                "Williams", "Gonzalez", "#color#", "Smith", "O'Brian"],

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
        "#main_title# #fun_number#: Chapter #fun_numeral#",
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
        " (yellow)",
        " (blue)",
        ": The revenge",
        ": The return",
        ": #space_age_adj# #ritual_or_event#",
        ": #story# of the #noun#",
        " XXX",
    ],

    "silly_prefix": [
        "Manos: The #noun.s# of",
        "Transformers #digit##digit#: ",
        "Code Name:",
        "David Winters presents:",
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
        "#silly_prefix# #noun#",
        "#silly_prefix# #ma_noun#",
        "#ma_noun# #silly_suffix#",
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
    ## merge adjectives / prefixes / suffixes
    #title = title.replace("- ", "")
    #title = title.replace(" -", "")
    #title = title.replace("  ", " ")

    ## fix spacing
    #title = title.replace("' ", "'")
    #title = title.replace(" : ", ": ")

    # fix plurals
    title = title.replace("Teethes", "Teeth")
    title = title.replace("Tearses", "Tears")
    title = title.replace("Womans", "Women")
    title = title.replace(" Mans ", " Men ")
    title = title.replace(" Mens", " Men")
    title = title.replace("Elfs", "Elves")
    title = title.replace(" Cheetahes", " Cheetahs")
    title = title.replace("Nauseas", "Nausea")
    title = title.replace("Bloods", "Blood")
    title = title.replace("Foots", "Feet")
    title = title.replace("Gentlemans", "Gentlemen")
    title = title.replace("Gentlewomans", "Gentlewomen")
    title = title.replace("Spacemans", "Spacemen")
    title = title.replace("Spacewomans", "Spacewomen")
    title = title.replace("Snowmans", "Snowmen")
    title = title.replace("Snowwomans", "Snowwomen")

    # capitalize
    #title = title.strip().title()
    title = custom_capitalize(title.strip())

    # fix title case errors
    title = title.replace("'S ", "'s ")
    title = title.replace(" Of ", " of ")
    title = title.replace(" The ", " the ")
    title = title.replace("'T ", "'t ")
    title = title.replace(" : ", ": ")
    title = title.replace("- ", "-")
    title = title.replace("41St", "41st")
    title = title.replace(" stuffs", " stuff")

    return title


def main():
    """ entry point """

    # build gammar
    grammar = tracery.Grammar(RULES)
    grammar.add_modifiers(base_english)

    counter = 0
    followers = set()

    logger.info("Serving: https://mastodon.social/@daveryderbot")

    # get api object
    api = get_api()

    # Main loop
    while True:

        # generate the title!
        title = clean(grammar.flatten("#full_title#"))

        # toot
        msg = title
        if counter % HASHTAG_INTERVAL == 0:
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

        # sleep for 3 hours
        time.sleep(60 * 60 * 3)

def test():
    for i in range(1000):
        grammar = tracery.Grammar(RULES)
        title = clean(grammar.flatten("#full_title#"))
        print(title)

if __name__ == "__main__":
    main()
    #test()
