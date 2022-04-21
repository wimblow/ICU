from icu import __version__
from icu.database.db_connect import Connexion

connect = Connexion() 


def test_version():
    assert __version__ == '0.1.0'

def test_select():
    assert connect.select_statut() == [(1, 'with_mask'), (2, 'without_mask')]

def test_connect():
    assert connect.connect() == "Connexion établie"