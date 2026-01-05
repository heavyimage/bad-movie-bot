
# TODO: try to have an example title to explain the rule!
full_titles = [
    # prefix and suffix
    "#silly_prefix# #threat#",
    "#silly_prefix# #form#",
    "#form# #silly_suffix#",

    # unsorted:
    "#noun# of the #form#",
    "#threat# #noun#",
    "#adj# #job#: The #noun# of the #form#",
    "#adj# #noun#",
    "#adj# #noun# of the #pluralform#",

    # basic form
    "#form#!",
    "The #form#",
    "The #adj# #adj# #threat#",

    # one person X machine
    "One #person# #threat# Machine",

    # battles
    "#form# vs. #form#",
    "The #form# and the #form#",
    "#threat#-zilla VS #threat#-ra",

    # body part form
    "#body_part# #threat#",
    "#body_part# of #threat#",
    "The #body_part# of the #threat#",

    # the place that was turned to material
    # TODO: replace #place# with #maybe_adj_#place"
    "The #place_without_the# that was turned to #material_adj#",
    "The #place_without_the# that became #material_adj#",

    # magic job
    "#magic_type_adj# #magic# #job#",

    # carnival of souls
    "#maybe_the# #noun# of #threat.s#",

    # TODO: replace #place# with #maybe_adj_#place"
    "The #place# of #material_adj#",

    "#title# #surname# and the #form#",

    # TODO: The Million Eyes of Sumuru
    "The #large_count_singular_adj# #body_part.s# of the #threat#",
    "The #large_count_singular_adj# #body_part.s# of the #threat.s#",

    # TODO: night of 1000 dreams
    "#moment_in_time# of a #large_count_singular_adj# #concept.s#",

    # fear and loathing
    "#concept# and #concept#",

    # Beyond Good and Evil
    "#adverb# #concept# and #concept#",

    # Beyond Justice
    "#adverb# #concept#",

    # "Blue Justice"
    "#adj# #concept#",

    # Firestarter
    "#natural_phenomena#starter",

    # job
    "#form# #job#",
    "#threat# #job#",

    # TODO: replace #place# with #maybe_adj_#place"
    "#job# #threat# and the #form# #adverb# #place#",
    "#job# #threat# and the #threat# #adverb# #place#",
    "#job# #adverb# #place#",
    "#job# #noun#",

    # Samurai cop
    "#job# #job#",

    # The treasure of the sierra madres
    "The #maybe_old_adj# #riches# of #adj# #place#",

    # Mountain of the cannibal god
    # TODO: replace #place# with #maybe_adj_#place"
    "#place_without_the# of the #form#",

    # Plan 9 from outer space
    # TODO: replace #place# with #maybe_adj_#place"
    "#operation# #number# from #place#",

    # Assignment: earth
    # TODO: replace #place# with #maybe_adj_#place"
    "#operation#: #place#",

    # Phase IV
    "#operation# #number#",

    # escape from NY
    # TODO: this needs a lot of work...
    # TODO: replace #place# with #maybe_adj_#place"?????
    "#maybe_the# #maybe_adj# #adventure# #adverb# #place#",

    # The love witch
    "The #noun# #job#",

    # TODO: replace #place# with #maybe_adj_#place"
    "The #form# #adverb# #place#",
    "#maybe_the# #threat# #adverb# #place#",

    # The blood on satan's claw
    "The #threatening_substance# on the #fantasy_animal#'s #body_part#",
    "The #threatening_substance# in the #fantasy_animal#'s #body_part#",

    # The Sword of the lictor
    "The #noun# of the #pluralform#",

    # The masque of the red death
    "The #noun# of the #adj# #noun#",

    # TODO: replace #place# with #maybe_adj_#place"
    "The #portal# #adverb# #place#",

    # Ilsa: she wolf of the ss
    "#form#: #threat# of the #evil_group#",

    # Shadow over innsmouth
    # TODO: replace #place# with #maybe_adj_#place"
    "The #noun# #adverb# #place#",

    # "star wars"
    "#adj# #battle#",

    # "Battle of Los Angeles"
    # TODO: replace with #maybe_adj_#place"
    "#battle#: #maybe_adj# #place#",

    # "grind-house"
    "#place#",

    # the day of the triffids
    # the night of the lepus
    "The #moment_in_time# of the #pluralform#",

    # Beyond the valley of the dolls
    "#adverb# the #spooky_locale# of the #pluralform#",

    # sky captain and the world of tomorrow
    "#adj# #job# and the world of #simple_places#",

    # Vampire hunter D
    "#threat# #job# '#letter#'",

    # Daughters of the Sun
    "#human# of the #natural_phenomena#",
    "#human.s# of the #natural_phenomena#",

    # The door in time
    "The #portal# #adverb# #cosmic_place#",
    "The #portal# #adverb# the #cosmic_place#",
    # The infinite gate
    "The #cosmic_adj# #portal#",

    # a few other ones
    "The #form# that Couldn't be Killed",
    "The #form# that Couldn't be Stopped",
    "The #form# that Wouldn't Die#",
    "The Wild, Wild World of the #form#",
    "The Wild, Wild World of the #pluralform#",
    "They called me '#form#'",
    "#threat#geddon",
    "#threat#nado",
    "#threat#zilla",
    "#threat#drome",
    "30 #threat.s# in 30 Days",
    "30 #threat.s#, 30 Days",
    "Death by #form#",
    "Death by #pluralform#",
    "I Became #form.a#",
    "I Married #form.a#",
    "My dad married #threat.a#",
    "My mom married #threat.a#",
    "I Walked with #pluralform#",
    "I Walked with the #form#",
    "I Walked with the #pluralform#",
    "I was in league with #form.a#",
    # TODO: replace #place# with #maybe_adj_#place"
    "I #moved# #place#",
    "I Was a Teenage #form#",
    "I attended #adj.a# #ritual#",

    # sexploitation
    # "Daughter of the dinosaur people"
    "#partner# of the #real_animal#-people",
    "My #partner# is #form.a#",
    "#partner# of #threat#",
    "#partner# of #named_threat#",
    "#partner# from #star#",
    "#partner# of #mythological_places#",
    "My #partner# is #adj.a# #sexy_servant#",
    "My #partner# is the #adj# #sexy_servant# of #threat.s#",
    "My #partner# is the #adj# #sexy_servant# of #job.s#",
    "She was a #adj# #threat#",
    "#sexy_servant.s# of the #form#",
    "#adj# love potion#",
    "#form# de Sade",
    "Sexy #threat.s# in #plural_trapped_place#",
    "The #form# Lovers",
    "#form# in #sexy_material#",
    "#pluralform# in #sexy_material#",

    # forms I want to appear more rarely
    "#silly_sequels#",
]
