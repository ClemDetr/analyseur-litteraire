from adapter import AdaptateurCSV, LecteurCSV


def test_lire_lignes():
    lcsv = LecteurCSV().lire_lignes("./tests/test.csv")
    assert lcsv == [
        {
            "titre": "titlerer",
            "auteur": "miss author",
            "texte": "contenu du livre organisÃ©",
            "annee": "173",
        },
        {
            "titre": "machin",
            "auteur": "truc",
            "texte": "chose en boucle",
            "annee": "41435",
        },
        {
            "titre": "troisiÃ¨me",
            "auteur": "miss author",
            "texte": "noa died spoiler",
            "annee": "41784",
        },
    ]


def test_creation_texte_from_csv():

    adpt = AdaptateurCSV(LecteurCSV())
    txt_list = adpt.charger("./tests/test.csv")
    assert len(txt_list) == 3  # noqa: PLR2004
