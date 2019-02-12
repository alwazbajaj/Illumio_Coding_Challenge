import csv
class firewall:

    def __init__(self, rulesfile):
        self._rules = open(rulesfile)
        self._a = csv.reader(self._rules)

    def accept_packet(self,direction,protocol,port,ip_address):

        pt = [direction,protocol,port,ip_address]
        count = False
        for row in self._a:
            t = row[0].split()
            for i in range(4):
                if (str(pt[i])==str(t[i])):
                    count = True
                else:
                    count = False
                    break
            if (count == True):
                return count









