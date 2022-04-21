from datetime import datetime as dt
from datetime import date
import random
import time as ti
# import matplotlib.pyplot as plt
import numpy as np

from icu.database.db_connect import Connexion

conn = Connexion()


class Simul:

    @classmethod
    def auto_simul(cls, duration:int, sleep:int):
        """
        This method is used to automatically simulate person detection.

        Parameters
        ----------
        durationw : int
            The duration of the simulation in seconds.
        sleep : int
            The time between each detection in seconds.
        
        Returns
        -------
        None.
        """
        for i in range(duration):
            print(i)
            _date = date.today()
            _time = dt.now().strftime("%H:%M:%S")
            _timestamp = round(dt.now().timestamp())
            rdm_val = random.randint(0,1000)
            if rdm_val == 246:
                _statut = 2
            else:
                _statut = 1
            Connexion.insert_data(_date, _time, _timestamp, _statut)
            ti.sleep(random.randint(1,sleep))




    # @classmethod
    # def live_plot(cls, x_vec, y1_data, line1, identifier="", pause_time=15):

    #     if line1==[]:

    #         plt.ion()
    #         fig = plt.figure(figsize=(12,6))
    #         ax = fig.add_subplot(111)

    #         line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)

    #         plt.xlabel('Time')
    #         plt.ylabel('Value')
    #         plt.title('Real-time data')
    #         plt.grid(True)
    #         plt.show()

    #     line1.set_data(x_vec, y1_data)
    #     plt.pause(pause_time)

    #     return line1


