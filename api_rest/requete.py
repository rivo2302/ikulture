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


    def _close(self):
        self.db.close()

req =  Requete()