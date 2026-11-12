from signalam.gazetteer import load_gazetteer, match_place


def test_jinka_matches_south_ethiopia():
    place = match_place("cases reported near Jinka", load_gazetteer())
    assert place and place["region"] == "South Ethiopia"


def test_amharic_place_name_matches():
    place = match_place("በጂንካ አካባቢ", load_gazetteer())
    assert place and place["name"] == "Jinka"
