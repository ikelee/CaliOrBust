#Sept 13, 
#Ike Lee
#Development Cycle 1 of Fall 2017 Coop project 
#Nodes: Game designed to emulate cyber attack 

class Gameboard: 
    def __init__ (self):
        self.blockA = 0
        self.blockB = 0
        self.blockC = 0
        self.blockD = 0 
        self.blockE = 0
        self.blockF = 0
        self.blockG = 0
        self.blockH = 0
        self.blockI = 0

        self.blocklist = [self.blockA, self.blockB, self.blockC, self.blockD, self.blockD, self.blockF, self.blockG, self.blockH, self.blockI]

        '''
         _______       _______       _______
        |       |     |       |     |       |
        |   A   |  ab |   B   |  bc |   C   |
        |       |     |       |     |       |
         -------       -------       -------
           ad            be            cf
         _______       _______       _______
        |       |     |       |     |       |
        |   D   |  de |   E   |  ef |   F   |
        |       |     |       |     |       |
         -------       -------       -------
           dg            eh            fi
         _______       _______       _______
        |       |     |       |     |       |
        |   G   |  gh |   H   |  hi |   I   |
        |       |     |       |     |       |
         -------       -------       -------

        '''

    def block

    def board_output(self):
        print("      _______       _______       _______ ")
        print("     |       |     |       |     |       |")
        print("     |   %s   |  ab |   %s   |  bc |   %s   |" % (self.blocklist[0], self.blocklist[1], self.blocklist[2]))
        print("     |       |     |       |     |       |")
        print("      -------       -------       -------")
        print("        ad            be            cf")
        print("      _______       _______       _______")
        print("     |       |     |       |     |       |")
        print("     |   %s   |  de |   %s   |  ef |   %s   |" % (self.blocklist[3], self.blocklist[4], self.blocklist[5]))
        print("     |       |     |       |     |       |")
        print("      -------       -------       -------")
        print("        dg            eh            fi")
        print("      _______       _______       _______")
        print("     |       |     |       |     |       |")
        print("     |   %s   |  gh |   %s   |  hi |   %s   |" % (self.blocklist[6], self.blocklist[7], self.blocklist[8]))
        print("     |       |     |       |     |       |")
        print("      -------       -------       -------")

class player1: 
    def __init__(self, Gameboard):
        self.starting_point = Gameboard.blockA
        self.possessed_server = [Gameboard.blockA]
        self.course_of_attack = {"ab": 0, "ad" : 0}

    def gain_network(net_name): 
        self.possessed_server.append(self.net_name)


gameboard = Gameboard()
gameboard.board_output()


