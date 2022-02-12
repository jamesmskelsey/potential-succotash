from character_match import is_character_match


def test_matches_add_DAD():
    assert is_character_match('add', 'DAd') == True

def test_does_not_match_add_DAD_exclamation():
    assert is_character_match('add', 'DAD!') == False
    