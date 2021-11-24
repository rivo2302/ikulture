import psycopg2
from psycopg2 import Error

from  conf import DATABASE

class Requete() :
    """
        Une classe où  on va mettre toutes les différents requêtes à  la base de données.
    """

    def __init__(self):
        """
        Initialisation de la base de données 
        """
        self.__connect()


    def __connect(self):
        """
        Connection à la base de données Postgresql
        """
        self.db =  psycopg2.connect(
            user=DATABASE["user"],
            password=DATABASE["password"],
            host=DATABASE["host"],
            port=DATABASE["port"],
            database=DATABASE["database"]
        )
        self.cursor = self.db.cursor()

    def getListCommune(self):

        req = """
            SELECT id, nom, latitude , longitude 
            FROM commune  
            Where longitude  IS NOT NULL
            """
        self.cursor.execute(req)
        res =  self.cursor.fetchall()
        return res 

    def getDetailCommune(self,id):

        req = """
            SELECT id, nom 
            FROM commune 
            WHERE id = %s
        """
        self.cursor.execute(req, (id,))
        res = self.cursor.fetchone()
        return res

        
    def _close(self):
        self.db.close()



