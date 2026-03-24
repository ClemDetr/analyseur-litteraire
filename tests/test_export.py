from export import creer_exportateur
from texte import Texte


def test_export_html():
    texte1 = Texte(
        "Droit de la femme",
        "eMILE",
        """A LA REINE.


    MADAME,

    Peu faite au langage que l'on tient aux Rois, je n'emploierai point
    l'adulation des Courtisans pour vous faire hommage de cette singulière
    production. Mon but, Madame, est de vous parler franchement; je n'ai
    pas attendu, pour m'exprimer ainsi, l'époque de la Liberté: je me
    suis montrée avec la même énergie dans un temps où l'aveuglement des
    Despotes punissait une si noble audace.

    Lorsque tout l'Empire vous accusait et vous rendait responsable de ses
    calamités, moi seule, dans un temps de trouble et d'orage, j'ai eu la
    force de prendre votre défense. Je n'ai jamais pu me persuader qu'une
    Princesse, élevée au sein des grandeurs, eût tous les vices de la
    bassesse.

    Oui, Madame, lorsque j'ai vu le glaive levé sur vous, j'ai jeté mes
    observations entre ce glaive et la victime; mais aujourd'hui que je
    vois qu'on observe de près la foule de mutins soudoyée, & qu'elle est
    retenue par la craiHtnte des loix, je vous dirai, Madame, ce que je ne
    vous aurois pas dit alors.
    """,
        1200,
    )
    expt = creer_exportateur("html")
    assert type(expt.export(texte1)) is str
