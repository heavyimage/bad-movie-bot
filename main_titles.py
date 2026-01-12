
# TODO: try to have an example title to explain the rule!
# TODO: ideally try to slim this down as much as possible
main_titles = [

    # basic forms
    "#ma_noun#!",
    "The #ma_noun#",
    "The #adj#, #adj# #noun#",
    "#noun# #noun#",
    "#adj# #job#: The #noun# of the #ma_noun#",
    "#adj# #noun#",
    "#ma_noun# of the #ma_noun#",
    "The #ma_noun# and the #ma_noun#",

    # body part form
    "#body_part# #noun#",
    "#body_part# of #noun#",
    "The #body_part# of the #noun#",

    # job
    "#ma_noun# #job#",
    "#noun# #job#",

    "The #scheme# of the #noun#",

    # TODO: this needs a lot of work...
    # TODO: replace #place# with #maybe_adj_#place"?????
    #"#maybe_the# #maybe_adj# #adventure# #preposition# #place#",
    "#smart_place# that was turned to #material#",
    "#smart_place# that became #material#",
    "#smart_place# of #material_adj#",
    "The #portal# #preposition# #smart_place#",
    "I attended #maybe_adj.a# #ritual_or_event#",
    "#job# #noun# and the #ma_noun# #preposition# #smart_place#",
    "#job# #noun# and the #noun# #preposition# #smart_place#",
    "#job# #preposition# #smart_place#",
    "The #ma_noun# #preposition# #smart_place#",
    "#maybe_the# #noun# #preposition# #smart_place#",


    ### GENRE WORK ###

    # mondo cane
    "The Wild, Wild World of the #ma_noun#",
    "The Wild, Wild World of the #ma_nouns#",
    "They called me '#ma_noun#'",
    "#noun##threat_suffix#",
    "30 #noun.s# in 30 Days",
    "30 #noun.s#, 30 Days",

    # Bad horror
    "Death by #ma_noun#",
    "Death by #ma_nouns#",
    "The #ma_noun# that #impossible_verb# be Killed",
    "The #ma_noun# that #impossible_verb# be Stopped",
    "The #ma_noun# that #impossible_verb# Die#",
    "The #noun# that #impossible_verb# Die#",
    "I #ominous_place_actions# #smart_place#",
    "I #ominous_place_actions# #smart_ma_place#",
    "I #ominous_noun_actions_past# the #ma_noun#",
    "I #ominous_noun_actions_past# the #ma_nouns#",
    "I was in league with #ma_noun.a#",

    # Cursed relations
    # TODO: fuse became / married
    "My #relation# Became #ma_noun.a#",
    "My #relation# Married #noun.a#",

    "#relation# from #smart_place#",
    "#relation# of #smart_place#",
    "#relation# of #noun.s#",
    "#relation# of #name#",
    "#relation# of the #job#",

    # sexploitation
    "She was a #adj# #noun#",
    "#sexy_servant.s# of the #ma_noun#",
    "#adj# love potion#",
    "#ma_noun# de Sade",
    "#maybe_adj# #noun.s# in the #trapped_place#",
    "The #noun# in the #trapped_place#",
    "The #ma_noun# Lovers",
    "#ma_noun# in #sexy_material#",
    "#ma_nouns# in #sexy_material#",
    "My #relation# is #adj.a# #sexy_servant#",
    "My #relation# is #ma_noun.a#",
    "My #relation# is the #adj# #sexy_servant# of #job.s#",
    "My #relation# is the #adj# #sexy_servant# of #noun.s#",


    ### TARGET  FILM TITLES ###
    # one person X machine
    "One #person# #noun# Machine",

    # magic job
    "#magic_type_adj# #magic# #job#",

    # (the) carnival of souls
    "#maybe_the# #noun# of #noun.s#",

    # texas chainsaw massacre
    "#evocative_nations# #appliance_tool_or_weapon# #battle#",

    # Demon door
    "#evil_adj# #portal#",

    # The Seventh Seal
    "The #numeric# #portal#",

    # Close Encounters, lol
    "#adj# Encounters of the #numeric# kind",

    # Ilsa: she wolf of the ss
    "#ma_noun#: #noun# of the #evil_group#",

    # Why did you eat my mother?!"
    "Why did you #ominous_noun_actions_present# my #relation#?!",

    # Shadow over innsmouth
    # hell comes to frogdown
    "The #concept# over #smart_ma_place#",
    "The #concept# from #smart_ma_place#",
    "The #concept# that came to #smart_ma_place#",
    "#concept# comes to #smart_ma_place#",

    # Picnic at hanging rock
    "#ritual_or_event# at #smart_ma_place#",

    # "star wars"
    "#adj# #battle#",

    # "Battle of Los Angeles"
    "#battle#: #smart_ma_place#",

    # "grind-house", forbidden planet
    "#adj# #smart_place#",

    # Daughters of the Sun
    "#human# of the #natural_phenomena#",
    "#human.s# of the #natural_phenomena#",

    # The door in time
    "The #portal# #preposition# #smart_place#",
    # The infinite gate
    "The #cosmic_adj# #portal#",

    # D-war
    "#letter#-#battle#",

    # I have no mouth but I must scream
    "I have no #body_part# but I must #human_reaction#",

    # "Daughter of the dinosaur people"
    "#relation# of the #all_animals#-#people#",

    # I was a teenage warewolf
    "I Was a #silly_adj# #ma_noun#",

    # hitchiker's guide to the galaxy
    "The #job#'s guide to #smart_place#",

    # the day of the triffids
    # the night of the lepus
    "The #moment_in_time# of the #ma_nouns#",

    # Beyond the valley of the dolls
    "#preposition# the #spooky_natural_locale# of the #ma_nouns#",

    # sky captain and the world of tomorrow
    "#adj# #job# and the world of #smart_place.s#",

    # Vampire hunter D
    "#noun# #job# '#letter#'",

    # TODO: The Million Eyes of Sumuru
    "The #large_count_singular_adj# #body_part.s# of the #noun#",
    "The #large_count_singular_adj# #body_part.s# of the #noun.s#",

    # TODO: night of 1000 dreams
    "#moment_in_time# of a #large_count_singular_adj# #concept.s#",

    # fear and loathing
    "#concept# and #concept#",

    # Beyond Good and Evil
    "#preposition# #concept# and #concept#",

    # Beyond Justice
    "#preposition# #concept#",

    # "Blue Justice"
    "#adj# #concept#",

    # The shadow over innsouth
    "The #concept# #preposition# #smart_place#",

    # Firestarter
    "#natural_phenomena#starter",

    # The hills have eyes
    "The #spooky_natural_locale.s# have #body_part.s#",

    # The cabin in the woods
    "The #human_structure# in the #spooky_natural_locale.s#",

    # Superman lives!
    "#noun# lives!",

    # librarian counterattack
    "#job# #noun#",

    # Samurai cop
    "#job# #job#",

    # The treasure of the sierra madres
    "The #maybe_old_adj# #riches# of #adj# #smart_place#",

    # Mountain of the cannibal god
    # TODO: replace #place# with #maybe_adj_#place"
    "#smart_place# of the #ma_noun#",

    # Plan 9 from outer space
    # TODO: replace #place# with #maybe_adj_#place"
    "#operation# #fun_number# from #smart_place#",

    # Assignment: earth
    # TODO: replace #place# with #maybe_adj_#place"
    "#operation#: #smart_place#",

    # Phase IV
    "#operation# #fun_number#",

    # The hydra protocol
    "The #noun# #operation#",
    "The #name# #operation#",
    "#smart_place# #operation.s#",

    # escape from NY
    "#adventure# #preposition# #smart_place#",
    # The love witch
    "The #noun# #job#",

    # The blood on satan's claw
    "The #threatening_substance# on the #fantasy_animal#'s #body_part#",
    "The #threatening_substance# in the #fantasy_animal#'s #body_part#",

    # The Sword of the lictor
    "The #noun# of the #ma_nouns#",

    # The masque of the red death
    "The #noun# of the #adj# #noun#",

    # Indiana Jones and the raiders of the lost ark
    "#title# #surname# and the #job# of the #adj# #appliance_tool_or_weapon#",

    # Indiana Jones and the temple of doom
    "#title# #surname# and the #human_structure# of #concept#",

    # Indiana Jones and last crusade
    "#title# #surname# and the #ordering# #adventure#",

    # indiana Jones and the dial of destiny
    "#title# #surname# and the #appliance_tool_or_weapon# of #concept#",

    # The cranes are flying
    "The #all_animals.s# are flying",

    # don't fear the reaper
    "Don't #fear# the #noun#",

    # Ice Station Zebra
    "Ice Station #real_animal#",

    # Something like Ilsa she-wolf of the SS
    "#name#: She-#all_animals# of the #evil_group#", 

    # Santa Claus conquers the Martians
    "#name# conquers the #noun.s#",

    # Godzilla films
    "#noun#-#threat_suffix# vs. #noun#-#threat_suffix#",

    # Superman vs batman: dawn of justice
    "#name# vs. #name#: #moment_in_time# of #concept#",

    # other Battles
    "#name# vs. #name#",
    "#name# vs. the #ma_noun#",
    "#name# vs. the #ma_noun.s#",
    "The #ma_noun# vs. the #ma_noun#",

    # Witchcraft Through the Ages
    "#job#craft through the #time.s#",

    # Space 1999
    "#place_nrt#: #funny_year#",
    "#place_rt#: #funny_year#", # ignore 'the' in this context?

    # Back to the future
    "Back to #smart_place#",

    # heart of darkness
    "#body_part# of #concept#",

    # Superman: dawn of justice
    "#name#: #moment_in_time# of #concept#",

    #Fat Guy Goes Nutzoid!!
    "#adj# #human# goes #crazy_adj#!!",

    # harder constructions?
    "#noun#dotcom",

    # love actually
    "#concept# Actually",

    # Martha Marcy May Marlene
    "Martha #name# #name# Marlene",

    # Precious: Based on the Novel “Push” by Sapphire 
    "#adj#: Based on the Novel '#noun#' by #material#",

    # Octopussy
    "#adj#pussy",

    # Blade Runner
    "#appliance_tool_or_weapon# #job#",
    "#appliance_tool_or_weapon# #job# 20#digit##digit#",

    # Flesh Market
    "#body_part# #ritual_or_event#",

    # The creature from the black lagoon
    "The #threatening_thing# from #smart_a_place#",
]
