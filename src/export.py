"""Exportateurs"""

from abc import ABC, abstractmethod

from texte import Texte  # noqa: TC001


class Exportateur(ABC):
    """classe exportateur"""

    @abstractmethod
    def export(self, texte: "Texte"): ...


class ExportateurHTML(Exportateur):
    """Export html docs"""

    def export(self, texte: "Texte"):
        return f"<h1 >{texte.titre} </h1 > <p >{texte.contenu} </p>"


class ExportateurCSV(Exportateur):
    """Export csv docs"""

    def export(self, texte):
        return "\n".join(f"{m} ,{c}" for m, c in texte.frequences().items())


class ExportateurMarkdown(Exportateur):
    """Export md file"""

    def export(self, texte):
        return f"{texte.titre}\n{texte.auteur}, {texte.annee}\n{texte.contenu}"


EXPORTATEURS: dict[str, type[Exportateur]] = {
    "html": ExportateurHTML,
    "csv": ExportateurCSV,
    "md": ExportateurMarkdown,
}


def creer_exportateur(extformat: str) -> Exportateur:
    cls = EXPORTATEURS.get(extformat)
    if cls is None:
        e = f"Format inconnu : {extformat}"
        raise ValueError(e)
    return cls()
