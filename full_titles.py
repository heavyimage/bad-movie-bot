
# TODO: try to have an example title to explain the rule!
full_titles = [
    # prefix and suffix
    "#silly_prefix# #noun#",
    "#silly_prefix# #ma_noun#",
    "#ma_noun# #silly_suffix#",

    # unsorted:
    "#noun# of the #ma_noun#",
    "#noun# #noun#",
    "#adj# #job#: The #noun# of the #ma_noun#",
    "#adj# #noun#",
    "#adj# #noun# of the #ma_nouns#",

    # basic form
    "#ma_noun#!",
    "The #ma_noun#",
    "The #adj# #adj# #noun#",

    # one person X machine
    "One #person# #noun# Machine",

    # battles
    "#ma_noun# vs. #ma_noun#",
    "The #ma_noun# and the #ma_noun#",
    "#noun#-zilla VS #noun#-ra",

    # body part form
    "#body_part# #noun#",
    "#body_part# of #noun#",
    "The #body_part# of the #noun#",

    # the place that was turned to material
    # TODO: replace #place# with #maybe_adj_#place"
    "#smart_place# that was turned to #material#",
    "#smart_place# that became #material#",
    # TODO: replace #place# with #maybe_adj_#place"
    "#smart_place# of #material_adj#",

    # magic job
    "#magic_type_adj# #magic# #job#",

    # (the) carnival of souls
    "#maybe_the# #noun# of #noun.s#",

    # texas chainsaw massacre
    "#evocative_nations# #spooky_objects_tools_or_weapons# #battle#",

    "#title# #surname# and the #ma_noun#",

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

    # job
    "#ma_noun# #job#",
    "#noun# #job#",

    # The hills have eyes
    "#smart_place.s# have #body_part.s#",

    # The cabin in the woods
    "The #building# in the #spooky_locale.s#",

    # Superman lives!
    "#noun# lives!",

    # TODO: replace #place# with #maybe_adj_#place"
    "#job# #noun# and the #ma_noun# #preposition# #smart_place#",
    "#job# #noun# and the #noun# #preposition# #smart_place#",
    "#job# #preposition# #smart_place#",

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
    "#operation# #number# from #smart_place#",

    # Assignment: earth
    # TODO: replace #place# with #maybe_adj_#place"
    "#operation#: #smart_place#",

    # Phase IV
    "#operation# #number#",

    # The hydra protocol
    "The #noun# #operation#",
    "#smart_place# #operation.s#",

    # escape from NY
    # #TODO: place/the fail!
    "#adventure# #preposition# #smart_place#",

    # TODO: this needs a lot of work...
    # TODO: replace #place# with #maybe_adj_#place"?????
    #"#maybe_the# #maybe_adj# #adventure# #preposition# #place#",

    # The love witch
    "The #noun# #job#",

    # TODO: replace #place# with #maybe_adj_#place"
    "The #ma_noun# #preposition# #smart_place#",
    "#maybe_the# #noun# #preposition# #smart_place#",

    # The blood on satan's claw
    "The #threatening_substance# on the #fantasy_animal#'s #body_part#",
    "The #threatening_substance# in the #fantasy_animal#'s #body_part#",

    # The Sword of the lictor
    "The #noun# of the #ma_nouns#",

    # The masque of the red death
    "The #noun# of the #adj# #noun#",

    # TODO: replace #place# with #maybe_adj_#place"
    "The #portal# #preposition# #smart_place#",

    # Ilsa: she wolf of the ss
    "#ma_noun#: #noun# of the #evil_group#",

    # Why did you eat my mother?!"
    "Why did you #danger_verb# my #relation#?!",

    # Shadow over innsmouth
    # TODO: replace #place# with #maybe_adj_#place"
    "The #noun# #preposition# #smart_place#",

    # "star wars"
    "#adj# #battle#",

    # "Battle of Los Angeles"
    # TODO: replace with #maybe_adj_#place"
    "#battle#: #maybe_adj# #smart_place#",

    # "grind-house"
    "#adj# #smart_place#",

    # the day of the triffids
    # the night of the lepus
    "The #moment_in_time# of the #ma_nouns#",

    # Beyond the valley of the dolls
    "#preposition# the #spooky_locale# of the #ma_nouns#",

    # sky captain and the world of tomorrow
    "#adj# #job# and the world of #smart_place.s#",

    # Vampire hunter D
    "#noun# #job# '#letter#'",

    "The #scheme# of the #noun#",

    # Daughters of the Sun
    "#human# of the #natural_phenomena#",
    "#human.s# of the #natural_phenomena#",

    # The door in time
    "The #portal# #preposition# #smart_place#",
    # The infinite gate
    "The #cosmic_adj# #portal#",

    # D-war
    "#letter#-#battle#",

    # a few other ones
    "The #ma_noun# that #impossible_verb# be Killed",
    "The #ma_noun# that #impossible_verb# be Stopped",
    "The #ma_noun# that #impossible_verb# Die#",
    "The Wild, Wild World of the #ma_noun#",
    "The Wild, Wild World of the #ma_nouns#",
    "They called me '#ma_noun#'",
    "#noun##threat_suffix#",
    "30 #noun.s# in 30 Days",
    "30 #noun.s#, 30 Days",
    "Death by #ma_noun#",
    "Death by #ma_nouns#",

    # Demon door
    "#evil_adj# #portal#",

    # Cursed relations
    "My #relation# Became #ma_noun.a#",
    "#relation# Became #ma_noun.a#",
    "My #relation# #ominous_action# #noun.a#",
    "#relation# #ominous_action# #ma_noun.a#",
    "#relation# from #smart_place#",
    "#relation# of #smart_place#",
    "#relation# of #named_noun#",
    "#relation# of #noun#",
    # "Daughter of the dinosaur people"
    "#relation# of the #real_animal#-people",

    "My #relation# is #adj.a# #sexy_servant#",
    "My #relation# is #ma_noun.a#",
    "My #relation# is the #adj# #sexy_servant# of #job.s#",
    "My #relation# is the #adj# #sexy_servant# of #noun.s#",

    "I #ominous_action# #preposition# #ma_nouns#",
    "I #ominous_action# the #ma_noun#", # TODO: need prepositions?
    "I #ominous_action# the #ma_nouns#", # TODO: need prepositions
    "I was in league with #ma_noun.a#",

    # TODO: replace #place# with #maybe_adj_#place"
    "I #ominous_action# #smart_place#",
    "I attended #adj.a# #ritual#",

    # I was a teenage warewolf
    "I Was a #silly_adj# #ma_noun#",

    # sexploitation
    "She was a #adj# #noun#",
    "#sexy_servant.s# of the #ma_noun#",
    "#adj# love potion#",
    "#ma_noun# de Sade",
    "#maybe_adj# #noun.s# in #trapped_place#",
    "The #noun# in #trapped_place#",
    "The #ma_noun# Lovers",
    "#ma_noun# in #sexy_material#",
    "#ma_nouns# in #sexy_material#",

    # hitchiker's guide to the galaxy
    "The #job#'s guide to #smart_place#",

    # forms I want to appear more rarely
    "#silly_sequels#",
]
