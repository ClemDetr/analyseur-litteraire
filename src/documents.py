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

if __name__ == "__main__":
    R = Roman("Machin","Pierre","Choses et Trucs","2027","Science-fictive")
    print(R)
    R.resume()
