"""Exportateurs"""
from abc import ABC, abstractmethod
from texte import Texte



class Exportateur (ABC):
    """classe exportateur"""
    @abstractmethod
    def export(self, texte : "Texte") :...

class ExportateurHTML(Exportateur):
    """Export html docs"""
    def export(self, texte : "Texte"):
        return f"<h1 >{texte.titre} </h1 > <p >{texte.contenu} </p>"

class ExportateurCSV(Exportateur):
    """Export csv docs"""
    def export(self, texte):
        return "\n". join ( f"{m} ,{c}" for m , c in texte.frequences().items () )
