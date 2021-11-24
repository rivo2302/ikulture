from typing_extensions import Self
import falcon

from requete import Requete


db =  Requete()

class listCommune:
    """GET LISTE DE TOUTES COMMUNE"""
    def on_get(self, req, resp):
        """Retour quand on fait une requete GET"""
        resp.media = db.getListCommune()


class detailCommune :
    def __init__ (self,id):
        self.id = id

    def on_get(self, req, resp,id):
        """GET DETAIL COMMUNE"""
        resp.media = db.getDetailCommune(id)


class listPlante:
    def on_get(self, req, resp):
        """Retour quand on fait une requete GET"""
        resp.media = db.getListPlante()


class detailPlante :
    def __init__ (self,id):
        self.id = id
    def on_get(self, req, resp,id):
        """ GET DETAIL Plante """
        resp.media = db.getDetailPlante(id) 


app = application = falcon.App()


app.add_route('/commune', listCommune())
app.add_route('/commune/{id}', detailCommune(id))
app.add_route('/plante', listPlante())
app.add_route('/plante/{id}', detailPlante(id))

