import requete
req = requete.Requete()
import falcon
class listCommune:

    def on_get(self, req, resp):
        """Retour quand on foait une requete GET"""
        
        resp.media = req.getListCommune()

app = application = falcon.App()
app.add_route('/commune', listCommune())