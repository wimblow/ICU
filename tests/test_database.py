from icu.database.db_connect import Connexion

connect = Connexion() 

def test_connect():
    assert connect.connect() == "Connexion établie"

def test_select():
    assert connect.select_statut() == [(1, 'with_mask'), (2, 'without_mask')]
