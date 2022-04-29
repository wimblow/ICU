import mysql.connector
from datetime import datetime as dt

class Connexion:

    @classmethod
    def connect(cls):
        cls.bdd = mysql.connector.connect(
            user="user", 
            password="root", 
            host="127.0.0.1",
            port="3308",
            database="facial_reco"
        )
        cls.cursor = cls.bdd.cursor()
        return "Connexion établie"

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.bdd.close()
    
    @classmethod
    def select_statut(cls):
        data = []
        cls.connect()
        cls.cursor.execute("SELECT * FROM statut")
        rep = cls.cursor.fetchall()
        for row in rep:
            data.append(row)
        cls.close()
        return data

    @classmethod
    def select_mask_period(cls, value, time):
        delta_time = round(dt.now().timestamp()) - time
        data = []
        data_value_count = {}
        cls.connect()
        if value == "*":
            cls.cursor.execute(
                f"SELECT label_statut \
                FROM statut \
                JOIN record \
                ON statut.id_statut = record.id_statut \
                WHERE record.timestamp_value >= {delta_time}")
        else:
            cls.cursor.execute(
                f"SELECT label_statut \
                FROM statut \
                JOIN record \
                ON statut.id_statut = record.id_statut \
                WHERE statut.label_statut = '{value}' AND record.timestamp_value >= {delta_time}")

        rep = cls.cursor.fetchall()
        for row in rep:
            data.append(row[0])
        for i in set(data):
            data_value_count[i] = data.count(i)
        cls.close()
        return data_value_count
    
    @classmethod
    def insert_data(cls, date, time, timestamp, statut):
        cls.connect()
        cls.cursor.execute(
            f"INSERT INTO record \
            VALUES (NULL,'{date}','{time}','{timestamp}','{statut}')")
        cls.bdd.commit()
        cls.close()

    @classmethod
    def select_dataviz(cls, start_time, end_time):

        cls.connect()
        cls.cursor.execute(
            f"SELECT label_statut \
            FROM statut \
            JOIN record \
            ON statut.id_statut = record.id_statut \
            WHERE record.timestamp_value >= {start_time} \
            AND record.timestamp_value <= {end_time}"
        )
  
        rep = cls.cursor.fetchall()

        cls.close()
        return rep

    @classmethod
    def select_dataviz2(cls, start_time, end_time):

        cls.connect()
        cls.cursor.execute(
            f"SELECT * \
            FROM record \
            JOIN statut \
            ON statut.id_statut = record.id_statut \
            WHERE record.timestamp_value >= {start_time} \
            AND record.timestamp_value <= {end_time}"
        )
  
        rep = cls.cursor.fetchall()

        cls.close()
        return rep



# if __name__ == "__main__":
#     output = Connexion.select_dataviz2(start_time="2022-04-26", end_time="2022-04-27")
#     print(output)