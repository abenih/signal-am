from signalam.normalise import normalise_text
from signalam.lexicon import load_lexicons, score_text


def test_cholera_scores_above_threshold_amharic():
    scores = score_text(normalise_text("ባሕር ዳር — ኮሌራ ተጠርጥሯል፣ ተቅማጥ አለ"), load_lexicons())
    assert "cholera" in scores and scores["cholera"]["score"] >= 3


def test_below_threshold_text_scores_nothing():
    assert score_text("rain expected this week, farmers welcome it", load_lexicons()) == {}
