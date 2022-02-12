from caesar_cipher import caesar_cipher


def test_returns_correctly_shifted_string():
    assert caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!"
    assert caesar_cipher("Hello zach168! Yes here.",
                         5) == "Mjqqt efhm168! Djx mjwj."
    assert caesar_cipher("Hello Zach168! Yes here.", -
                         5) == "Czggj Uvxc168! Tzn czmz."
