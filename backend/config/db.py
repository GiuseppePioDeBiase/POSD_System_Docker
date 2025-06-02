from pymongo import MongoClient


def conn_db():
    # Configurazione della connessione al database
    conn = MongoClient('mongodb', 27017)
    db = conn['POSD_System']  # Nome del database
    return db
