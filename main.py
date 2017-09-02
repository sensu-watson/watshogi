from game import *


class SoftwareInformation:
    software_name = 'Watshogi'
    software_author = 'Masaru Watanabe'
    
    def response_softwarename(self):
        print('id name ' + self.software_name)

    def response_softwareauthor(self):
        print('id name ' + self.software_author)

class MainRoop:
    def __init__(self):
        self.swInfo = SoftwareInformation()
        self.game = GameRoop()

    def roop(self):
        isroop = True
        while isroop:
            command_list = input().split()
            isroop = self.response(command_list)

    def response(self, command_list):
        def response_usiok():
            self.swInfo.response_softwarename()
            self.swInfo.response_softwareauthor()
            print('usiok')
        def response_readyok():
            print('readyok')
            
        if command_list[0] == 'usi':
            response_usiok()
        if command_list[0] == 'isready':
            response_readyok()
        if command_list[0] == 'usinewgame':
            self.game.roop()
        if command_list[0] == 'quit':
            return False
        return True


        
if __name__ == '__main__':
    mainRoop = MainRoop()
    mainRoop.roop()

    
