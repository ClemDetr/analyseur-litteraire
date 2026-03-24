from abc import ABC, abstractmethod

from texte import Texte


# Ancien module (ne pas modifier !)
class LecteurCSV:
    def lire_lignes(self, chemin: str) -> list[dict]:
        import csv  # noqa: PLC0415

        with open(chemin) as f:  # noqa: PTH123
            return list(csv.DictReader(f))


# Notre interface
class ChargeurTextes(ABC):
    @abstractmethod
    def charger(self, source: str) -> list["Texte"]: ...


# L'Adapter : traduit l'ancien vers le nouveau (crée un nouveau texte pour chaque ligne)
class AdaptateurCSV(ChargeurTextes):
    def __init__(self, lecteur: LecteurCSV):
        self._lecteur = lecteur

    def charger(self, source: str) -> list["Texte"]:
        return [
            Texte(ligne["titre"], ligne["auteur"], ligne["texte"], ligne["annee"])
            for ligne in self._lecteur.lire_lignes(source)
        ]
