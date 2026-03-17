"""Analyseurs"""
from abc import ABC, abstractmethod
from texte import Texte
from documents import Poeme

class AnalyseurTexte (ABC):
    """class analyseur de texte"""
    @abstractmethod
    def analyser(self, texte: "Texte") -> dict: ...
    def analyser_corpus(self, docs: list["Texte"]) -> list[dict]:
        """analyseur de corpus"""
        return [self.analyser(d) for d in docs]

# a = AnalyseurTexte()  # TypeError !
class CompteurMots(AnalyseurTexte):
    """compteur de mots"""
    def analyser(self, texte: "Texte") -> dict:
        mots = texte.resume().lower().split()
        return {"total": len(mots), "uniques": len(set(mots))}


class AnalyseurFreq(AnalyseurTexte):
    """analyseur de fréquence"""
    def analyser(self, texte: "Texte") -> dict:
        return texte.frequences().most_common(10)


class AnalyseurLongueur(AnalyseurTexte):
    """analyseur de longueur"""
    def analyser(self, texte: "Texte") -> dict:
        return f"""nombre mot : {texte.nombre_mots()}, nombre phrase : {texte.nombre_phrases()}, """
    def analyser_corpus(self, docs: list["Texte"]) -> list[dict]:
        """analyseur de corpus"""
        effectif = 0
        result =""
        for d in docs :
            effectif += d.nombre_phrases()
            result += self.analyser(d) +"\n"
        return f"{result}moyenne de phrases : {effectif/len(docs)}"


Te = Texte("jdnac","iojfoj","fiadajdkcmak adwipjm apw jmkdkwmq'à od kés. od", -245)
Po = Texte("acnloncol","ahocown","alsnénck aoi  apjajdwip  ajiwj aoi.", 239)
P = Poeme("Femmes damnées", "Charles Baudelaire",
    """Comme un bétail pensif sur le sable couchées,
    Elles tournent leurs yeux vers l’horizon des mers,
    Et leurs pieds se cherchant et leurs mains rapprochées
    Ont de douces langueurs et des frissons amers.

    Les unes, cœurs épris des longues confidences,
    Dans le fond des bosquets où jasent les ruisseaux,
    Vont épelant l’amour des craintives enfances
    Et creusent le bois vert des jeunes arbrisseaux ;

    D’autres, comme des sœurs, marchent lentes et graves
    À travers les rochers pleins d’apparitions,
    Où saint Antoine a vu surgir comme des laves
    Les seins nus et pourprés de ses tentations ;

    Il en est, aux lueurs des résines croulantes,
    Qui dans le creux muet des vieux antres païens
    T’appellent au secours de leurs fièvres hurlantes,
    Ô Bacchus, endormeur des remords anciens !

    Et d’autres, dont la gorge aime les scapulaires,
    Qui, recélant un fouet sous leurs longs vêtements,
    Mêlent, dans le bois sombre et les nuits solitaires,
    L’écume du plaisir aux larmes des tourments.

    Ô vierges, ô démons, ô monstres, ô martyres,
    De la réalité grands esprits contempteurs,
    Chercheuses d’infini, dévotes et satyres,
    Tantôt pleines de cris, tantôt pleines de pleurs,

    Vous que dans votre enfer mon âme a poursuivies,
    Pauvres sœurs, je vous aime autant que je vous plains,
    Pour vos mornes douleurs, vos soifs inassouvies,
    Et les urnes d’amour dont vos grands cœurs sont pleins ! """, 1857, 28 )
texte1 = Texte("Droit de la femme", "eMILE", """A LA REINE.


    MADAME,

    Peu faite au langage que l'on tient aux Rois, je n'emploierai point
    l'adulation des Courtisans pour vous faire hommage de cette singulière
    production. Mon but, Madame, est de vous parler franchement; je n'ai
    pas attendu, pour m'exprimer ainsi, l'époque de la Liberté: je me
    suis montrée avec la même énergie dans un temps où l'aveuglement des
    Despotes punissait une si noble audace. Modifié pour git.

    Lorsque tout l'Empire vous accusait et vous rendait responsable de ses
    calamités, moi seule, dans un temps de trouble et d'orage, j'ai eu la
    force de prendre votre défense. Je n'ai jamais pu me persuader qu'une
    Princesse, élevée au sein des grandeurs, eût tous les vices de la
    bassesse.

    Oui, Madame, lorsque j'ai vu le glaive levé sur vous, j'ai jeté mes
    observations entre ce glaive et la victime; mais aujourd'hui que je
    vois qu'on observe de près la foule de mutins soudoyée, & qu'elle est
    retenue par la crainte des loix, je vous dirai, Madame, ce que je ne
    vous aurois pas dit alors.
    """, 1200)
corpus = [Te, Po, P, texte1]

cm = CompteurMots()
print(cm.analyser(Te))
af = AnalyseurFreq()
print(af.analyser(P))
al = AnalyseurLongueur()
print(al.analyser_corpus(corpus))
