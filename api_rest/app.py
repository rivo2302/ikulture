import falcon


from requete import Requete
db =  Requete()

class listCommune:

    def on_get(self, req, resp):
        """Retour quand on fait une requete GET"""

        resp.media = db.getListCommune()

app = application = falcon.App()
app.add_route('/commune', listCommune())