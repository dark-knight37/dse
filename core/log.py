import datetime
import time
from blackboard import Blackboard


class Loggable():
    def __init__(self, nname, qqueue, eenv):
        self.dlevel = Blackboard().get('debugLevel')
        self.name = nname
        self.queue = qqueue
        self.env = eenv

    def getName(self):
        return self.name

    def log(self, message, debuglevel):
        if (self.dlevel <= debuglevel):
            tosend = str(self.env.now) + ';' + self.name + ';' + message
            self.queue.put(tosend)


class Logger:
    def __init__(self, qqueue):
        self.queue = qqueue
        self.running = True

    def manage(self, message):
        if (message == 'HALT'):
            self.running = False
        else:
            self.log(message)

    def log(self, message):
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        #print('\t\t' + st + '\t\t' + message)
        print(message)

    def run(self):
        while (self.running == True):
            m = self.queue.get()
            self.manage(m)