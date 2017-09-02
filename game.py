from board import *

class GameRoop:
    def __init__(self):
        self.current_board = Board()

    def roop(self):
        isroop = True
        while isroop:
            command_list = input().split()
            isroop = self.response(command_list)

    def response(self, command_list):
        if command_list[0] == 'position':
            if command_list[1] == 'startpos':
                moves = []
                for i in range(3, len(command_list)):
                    moves.append(command_list[i])
                if len(moves) % 2 == 0:
                    self.current_board.set_startpos()
                else:
                    self.current_board.set_startpos(engine_turn = 'gote')
                self.current_board.generate_state(moves)
        if command_list[0] == 'go':
            best_move, _ = self.current_board.calc_best_move()
            print('bestmove ' + best_move)
            #print('bestmove resign')
        if command_list[0] == 'gameover':
            return False
        return True
        
if __name__ == '__main__':
    pass

    
