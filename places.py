def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("#")]

# TODO: needs love!
base_places_rt = {
    "trapped_place": load("trapped_places"),
    "moment_in_time": load("moments_in_time"),
    "spooky_natural_locale": load("spooky_natural_locales"),
    "human_structure": load("human_structures"),
    "scary_parts_of_a_house": load("scary_parts_of_a_house"),
    "cosmic_place": load("cosmic_places_with_the"),
    "places_on_earth_with_the": load("places_on_earth_with_the"),

}

base_places_nrt = {
    "star": load("stars"),
    "fancy_star": ["#star# #maybe_fun_numeral#", "#greek_letter# #star#"],
    "named_planetary_body": load("named_planetary_bodies"),
    "mythological_place": load("mythological_places"),
    "places_on_earth_without_the": load("places_on_earth_without_the"),
    "cosmic_places_without_the": load("cosmic_places_without_the"),
}
