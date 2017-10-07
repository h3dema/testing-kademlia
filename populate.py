import argparse
import sys

from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server

population = {1: 'Detra',
              2: 'Janeth',
              3: 'Yasmine',
              4: 'Shanita',
              5: 'Jenice',
              6: 'Micaela',
              7: 'Shantae',
              8: 'Lanny',
              9: 'Karena',
              10: 'Titus',
              11: 'Domenica',
              12: 'Erich',
              13: 'Alexandra',
              14: 'Sunny',
              15: 'Macy',
              16: 'Faustino',
              17: 'Reid',
              18: 'Haley',
              19: 'Kerstin',
              20: 'Phil',
              21: 'Artie',
              22: 'Mario',
              23: 'Darrick',
              24: 'Michaela',
              25: 'Annabelle',
              26: 'Sindy',
              27: 'Grace',
              28: 'Eusebio',
              29: 'Lacy',
              30: 'Dotty',
              31: 'Antonio',
              32: 'Tegan',
              33: 'Jamie',
              34: 'Deonna',
              35: 'Assunta',
              36: 'Willow',
              37: 'Santos',
              38: 'Rudolf',
              39: 'Robt',
              40: 'Odell',
              41: 'Latasha',
              42: 'Cristina',
              43: 'Karyn',
              44: 'Joe',
              45: 'Zella',
              46: 'Azalee',
              47: 'Nicholas',
              48: 'Carmelia',
              49: 'Tawna',
              50: 'Mayra',
              }
log.startLogging(sys.stdout)


def done(result):
    print "Key result:", result
    reactor.stop()


def bootstrapDone(found, server):
    for k in population:
        server.set(k, population[k])
    reactor.stop()


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('server', type=str, default="172.17.0.1", help='the ip address of a server')
args = parser.parse_args()

server = Server()
server.listen(8468)
server.bootstrap([(args.server, 8468)]).addCallback(bootstrapDone, server)

reactor.run()
