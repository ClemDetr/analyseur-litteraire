from nettoyeur import nettoyer
from texte import Texte


def test_nettoyage():
    texte = Texte("Poème", "Baudelaire", "L'Ete, a Paris", 2013)
    assert nettoyer(texte) == "lete a paris"
