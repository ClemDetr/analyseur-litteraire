"""Documents"""
from texte import Texte

class Roman(Texte):
    """class roman apparenté à texte"""
    def __init__(self, titre, auteur, contenu, annee, genre):
        super().__init__(titre, auteur, contenu, annee)
        self.genre = genre

    def resume(self) -> str:
        result = f"{self.titre} de {self.auteur}, genre : {self.genre}"
        print(result)
        return result


class Poeme(Texte):
    """class poeme apparenté à texte"""
    def __init__(self, titre, auteur, contenu, annee, vers : int):
        super().__init__(titre, auteur, contenu, annee)
        self.vers = vers

    def resume(self) -> str:
        result = f"{self.titre} de {self.auteur}, nombre de vers: {self.vers}"
        print(result)
        return result


class Article(Texte):
    """class Article apparenté à texte"""
    def __init__(self, titre, auteur, contenu, annee, revue : str):
        super().__init__(titre, auteur, contenu, annee)
        self.revue = revue

    def resume(self) -> str:
        result = f"{self.titre} de {self.auteur}, dans la revue {self.revue}"
        print(result)
        return result


if __name__ == "__main__":
    R = Roman("Machin","Pierre","Choses et Trucs","2027","Science-fictive")
    print(R)
    R.resume()
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
    print(P)
    P.resume()

    A = Article("France riche, un oxymore","Francina","C'est Faux!","2013","The Onion")
    print(A)
    A.resume()
    print("\n")

    docs =[A,R,P]
    for d in docs :
        d.resume()
