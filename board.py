import copy
import threading


class Board:
    def __init__(self, board = None, sente_hand = None,
                 gote_hand = None, turn_player = None, tempo = None,
                 next_move = None, engine_turn = None, depth = 3):
        self.board = board
        self.sente_hand = sente_hand
        self.gote_hand = gote_hand
        self.turn_player = turn_player
        self.tempo = tempo
        self.next_move = next_move
        self.engine_turn = engine_turn
        self.depth = depth

    def calc_best_move(self):
        def calc_next(k):
            """nextboard = Board(board = copy.deepcopy(self.board),
                              sente_hand = copy.deepcopy(self.sente_hand),
                              gote_hand = copy.deepcopy(self.gote_hand),
                              turn_player = self.turn_player,
                              tempo = self.tempo,
                              engine_turn = self.engine_turn,
                              depth = self.depth - 1)"""
            nextboard = copy.deepcopy(self)
            nextboard.depth -= 1
            try:
                nextboard.move_peace(k)
            except KeyError:
                if self.engine_turn == self.turn_player:
                    self.next_move[k] = 9999
                    return 9999
                else:
                    self.next_move[k] = -9999
                    return -9999
            _, ret = nextboard.calc_best_move()
            self.next_move[k] = ret
            return ret
            
        if self.depth == 0:
            return None, self.evaluation_value()
        self.generate_next_move()
        next_turn_player = 'sente' if self.turn_player == 'gote' else 'gote'
        move = {}
        th = {}
        for k in self.next_move.keys():
            th[k] = threading.Thread(target=calc_next, name=k, args=(k,))
            th[k].start()
        for k in self.next_move.keys():
            th[k].join()
        
        
        #for k in self.next_move.keys():
        #    self.next_move[k] = calc_next(k)
        if self.engine_turn == self.turn_player:
            sort_next_move = sorted(self.next_move.items(), key=lambda x:x[1], reverse=True)
        else:
            sort_next_move = sorted(self.next_move.items(), key=lambda x:x[1])
        best_move = sort_next_move[0][0]
        return best_move, self.next_move[best_move]
        

    def evaluation_value(self):
        pointsum = 0
        for i in range(0,9):
            for j in range(0, 9):
                piece = self.board[i][j]
                if piece == ' ':
                    pass
                elif piece == 'P':
                    pointsum += 1
                elif piece == 'L':
                    pointsum += 3
                elif piece == 'N':
                    pointsum += 4
                elif piece == 'S':
                    pointsum += 5
                elif piece == 'G':
                    pointsum += 6
                elif piece == 'B':
                    pointsum += 8
                elif piece == 'R':
                    pointsum += 10
                elif piece == 'K':
                    pass
                elif piece == 'P+':
                    pointsum += 7
                elif piece == 'L+':
                    pointsum += 6
                elif piece == 'N+':
                    pointsum += 6
                elif piece == 'S+':
                    pointsum += 6
                elif piece == 'B+':
                    pointsum += 10
                elif piece == 'R+':
                    pointsum += 12
                elif piece == 'p':
                    pointsum -= 1
                elif piece == 'l':
                    pointsum -= 3
                elif piece == 'n':
                    pointsum -= 4
                elif piece == 's':
                    pointsum -= 5
                elif piece == 'g':
                    pointsum -= 6
                elif piece == 'b':
                    pointsum -= 8
                elif piece == 'r':
                    pointsum -= 10
                elif piece == 'k':
                    pass
                elif piece == 'p+':
                    pointsum -= 7
                elif piece == 'l+':
                    pointsum -= 6
                elif piece == 'n+':
                    pointsum -= 6
                elif piece == 's+':
                    pointsum -= 6
                elif piece == 'b+':
                    pointsum -= 10
                elif piece == 'r+':
                    pointsum -= 12
        pointsum += self.sente_hand['R'] * 10
        pointsum += self.sente_hand['B'] * 8
        pointsum += self.sente_hand['S'] * 5
        pointsum += self.sente_hand['N'] * 4
        pointsum += self.sente_hand['L'] * 3
        pointsum += self.sente_hand['P'] * 1
        pointsum -= self.gote_hand['R'] * 10
        pointsum -= self.gote_hand['B'] * 8
        pointsum -= self.gote_hand['S'] * 5
        pointsum -= self.gote_hand['N'] * 4
        pointsum -= self.gote_hand['L'] * 3
        pointsum -= self.gote_hand['P'] * 1

        if self.engine_turn == 'sente':
            self.can_move_sente()
        else:
            pointsum *= -1
            self.can_move_gote()
                
        self.generate_next_move()
        return pointsum * 100 + len(self.next_move)
        #return pointsum

    def puttable_piece(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist = []
        if self.is_exist_piece(i = i, j = j):
            return retlist
        if self.turn_player == 'sente':
            hand = self.sente_hand
        else:
            hand = self.gote_hand
        for k,v in hand.items():
            if v > 0:
                if i < 1 and k == 'P':
                    continue
                if i < 1 and k == 'L':
                    continue
                if i < 2 and k == 'N':
                    continue
                if k == 'P':
                    isnopawn = True
                    for l in range(9):
                        if self.board[l][j] == 'P' and self.turn_player == 'sente':
                            isnopawn = False
                        if self.board[l][j] == 'p' and self.turn_player == 'gote':
                            isnopawn = False
                    if isnopawn == False:
                        continue
                retlist.append(k + '*')
        return retlist

    def movable_place_P(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        if self.is_exist_turnplayer_piece(i = i-1, j = j):
            return []
        return [self.board_reverse_geo(i-1,j)]

    def movable_place_L(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(i-1, -1, -1):
            if self.is_exist_piece(i = k, j = j):
                if not self.is_exist_turnplayer_piece(i = k, j = j):
                    retlist.append(self.board_reverse_geo(k,j))
                return retlist
            else:
                retlist.append(self.board_reverse_geo(k,j))
        return retlist

    def movable_place_N(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        if not self.is_exist_turnplayer_piece(i = i-2, j = j-1):
            retlist.append(self.board_reverse_geo(i-2,j-1))
        if not self.is_exist_turnplayer_piece(i = i-2, j = j+1):
            retlist.append(self.board_reverse_geo(i-2,j+1))
        return retlist

    def movable_place_S(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i-1, j = k):
                retlist.append(self.board_reverse_geo(i-1,k))
        if not self.is_exist_turnplayer_piece(i = i+1, j = j-1):
            retlist.append(self.board_reverse_geo(i+1,j-1))
        if not self.is_exist_turnplayer_piece(i = i+1, j = j+1):
            retlist.append(self.board_reverse_geo(i+1,j+1))
        return retlist

    def movable_place_G(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i-1, j = k):
                retlist.append(self.board_reverse_geo(i-1,k))
        if not self.is_exist_turnplayer_piece(i = i, j = j-1):
            retlist.append(self.board_reverse_geo(i,j-1))
        if not self.is_exist_turnplayer_piece(i = i, j = j+1):
            retlist.append(self.board_reverse_geo(i,j+1))
        if not self.is_exist_turnplayer_piece(i = i+1, j = j):
            retlist.append(self.board_reverse_geo(i+1,j))
        return retlist

    def movable_place_B(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        leftup = True
        leftdown = True
        rightup = True
        rightdown = True
        for k in range(1, 9):
            if leftup:
                a = i-k
                b = j+k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    leftup = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if leftdown:
                a = i+k
                b = j+k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    leftdown = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if rightup:
                a = i-k
                b = j-k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    rightup = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if rightdown:
                a = i+k
                b = j-k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    rightdown = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
        return retlist
    
    def movable_place_R(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        up = True
        left = True
        right = True
        down = True
        for k in range(1, 9):
            if up:
                a = i-k
                b = j
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    up = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if left:
                a = i
                b = j+k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    left = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if right:
                a = i
                b = j-k
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    right = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
            if down:
                a = i+k
                b = j
                if not self.is_exist_piece(i = a, j = b):
                    retlist.append(self.board_reverse_geo(a, b))
                else:
                    down = False
                    if not self.is_exist_turnplayer_piece(i = a, j = b):
                        retlist.append(self.board_reverse_geo(a, b))
        return retlist

    def movable_place_K(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i-1, j = k):
                retlist.append(self.board_reverse_geo(i-1,k))
        if not self.is_exist_turnplayer_piece(i = i, j = j-1):
            retlist.append(self.board_reverse_geo(i,j-1))
        if not self.is_exist_turnplayer_piece(i = i, j = j+1):
            retlist.append(self.board_reverse_geo(i,j+1))
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i+1, j = k):
                retlist.append(self.board_reverse_geo(i+1,k))
        return retlist

    def movable_place_promote_B(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist = self.movable_place_B(i = i, j = j)
        kinglist = self.movable_place_K(i = i, j = j)
        retlist.extend(kinglist)
        return list(set(retlist))
    
    def movable_place_promote_R(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist = self.movable_place_R(i = i, j = j)
        kinglist = self.movable_place_K(i = i, j = j)
        retlist.extend(kinglist)
        return list(set(retlist))

    def movable_place_p(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        if self.is_exist_turnplayer_piece(i = i+1, j = j):
            return []
        return [self.board_reverse_geo(i+1,j)]

    def movable_place_l(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(i+1, 9):
            if self.is_exist_piece(i = k, j = j):
                if not self.is_exist_turnplayer_piece(i = k, j = j):
                    retlist.append(self.board_reverse_geo(k,j))
                return retlist
            else:
                retlist.append(self.board_reverse_geo(k,j))
        return retlist

    def movable_place_n(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        if not self.is_exist_turnplayer_piece(i = i+2, j = j-1):
            retlist.append(self.board_reverse_geo(i+2,j-1))
        if not self.is_exist_turnplayer_piece(i = i+2, j = j+1):
            retlist.append(self.board_reverse_geo(i+2,j+1))
        return retlist

    def movable_place_s(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i+1, j = k):
                retlist.append(self.board_reverse_geo(i+1,k))
        if not self.is_exist_turnplayer_piece(i = i-1, j = j-1):
            retlist.append(self.board_reverse_geo(i-1,j-1))
        if not self.is_exist_turnplayer_piece(i = i-1, j = j+1):
            retlist.append(self.board_reverse_geo(i-1,j+1))
        return retlist

    def movable_place_g(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        retlist=[]
        for k in range(j-1, j+2):
            if not self.is_exist_turnplayer_piece(i = i+1, j = k):
                retlist.append(self.board_reverse_geo(i+1,k))
        if not self.is_exist_turnplayer_piece(i = i, j = j-1):
            retlist.append(self.board_reverse_geo(i,j-1))
        if not self.is_exist_turnplayer_piece(i = i, j = j+1):
            retlist.append(self.board_reverse_geo(i,j+1))
        if not self.is_exist_turnplayer_piece(i = i-1, j = j):
            retlist.append(self.board_reverse_geo(i-1,j))
        return retlist

    def movable_place_b(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        return self.movable_place_B(i = i, j = j)
    
    def movable_place_r(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        return self.movable_place_R(i = i, j = j)

    def movable_place_k(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        return self.movable_place_K(i = i, j = j)

    def movable_place_promote_b(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        return self.movable_place_promote_B(i = i, j = j)

    def movable_place_promote_r(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        return self.movable_place_promote_R(i = i, j = j)
    
    def is_exist_turnplayer_piece(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        if i > 8 or i < 0 or j > 8 or j < 0:
            return True
        if self.turn_player == 'sente':
            return self.board[i][j][0].isupper()
        else:
            return self.board[i][j][0].islower()

    def is_exist_piece(self, geo = None, i = None, j = None):
        if geo:
            i, j = self.board_geo(geo)
        if i > 8 or i < 0 or j > 8 or j < 0:
            return True
        return self.board[i][j] != ' '

    def can_move_sente(self):
        retlist = []
        for i in range(0,9):
            for j in range(0, 9):
                geo = self.board_reverse_geo(i = i,j = j)
                if self.board[i][j] == ' ':
                    movlist = self.puttable_piece(i = i, j = j)
                    for x in movlist:
                        retlist.append(x + geo)
                elif self.board[i][j] == 'P':
                    movlist = self.movable_place_P(i = i, j = j)
                    for x in movlist:
                        if i != 1:
                            retlist.append(geo + x)
                        if i < 4:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'L':
                    movlist = self.movable_place_L(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        if a != 0:
                            retlist.append(geo + x)
                        if a < 3:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'N':
                    movlist = self.movable_place_N(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        if a > 1:
                            retlist.append(geo + x)
                        if a < 3:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'S':
                    movlist = self.movable_place_S(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a < 3 or i < 3:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'G':
                    movlist = self.movable_place_G(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'B':
                    movlist = self.movable_place_B(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a < 3 or i < 3:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'R':
                    movlist = self.movable_place_R(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a < 3 or i < 3:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'K':
                    movlist = self.movable_place_K(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'P+':
                    movlist = self.movable_place_G(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'L+':
                    movlist = self.movable_place_G(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'N+':
                    movlist = self.movable_place_G(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'S+':
                    movlist = self.movable_place_G(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'B+':
                    movlist = self.movable_place_promote_B(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'R+':
                    movlist = self.movable_place_promote_R(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
        retdic = {}
        for x in retlist:
            retdic[x] = 0
        self.next_move = retdic
        return retlist

    def can_move_gote(self):
        retlist = []
        for i in range(0,9):
            for j in range(0, 9):
                geo = self.board_reverse_geo(i = i,j = j)
                if self.board[i][j] == ' ':
                    movlist = self.puttable_piece(i = i, j = j)
                    for x in movlist:
                        retlist.append(x + geo)
                elif self.board[i][j] == 'p':
                    movlist = self.movable_place_p(i = i, j = j)
                    for x in movlist:
                        if i != 7:
                            retlist.append(geo + x)
                        if i > 4:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'l':
                    movlist = self.movable_place_l(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        if a != 8:
                            retlist.append(geo + x)
                        if a > 5:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'n':
                    movlist = self.movable_place_n(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        if a < 7:
                            retlist.append(geo + x)
                        if a > 5:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 's':
                    movlist = self.movable_place_s(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a > 5 or i > 5:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'g':
                    movlist = self.movable_place_g(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'b':
                    movlist = self.movable_place_b(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a > 5 or i > 5:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'r':
                    movlist = self.movable_place_r(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                        if a > 5 or i > 5:
                            retlist.append(geo + x + '+')
                elif self.board[i][j] == 'k':
                    movlist = self.movable_place_k(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'p+':
                    movlist = self.movable_place_g(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'l+':
                    movlist = self.movable_place_g(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'n+':
                    movlist = self.movable_place_g(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 's+':
                    movlist = self.movable_place_g(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'b+':
                    movlist = self.movable_place_promote_b(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
                elif self.board[i][j] == 'r+':
                    movlist = self.movable_place_promote_r(i = i, j = j)
                    for x in movlist:
                        a, b = self.board_geo(x)
                        retlist.append(geo + x)
        retdic = {}
        for x in retlist:
            retdic[x] = 0
        self.next_move = retdic
        return retlist

    def generate_next_move(self):
        if self.turn_player == 'sente':
            retlist = self.can_move_sente()
        else:
            retlist = self.can_move_gote()
        return retlist

    def generate_state(self, moves):
        for x in moves:
            self.move_peace(x)
        
        retdic = {}
        retdic['board'] = self.board
        retdic['sente_hand'] = self.sente_hand
        retdic['gote_hand'] = self.gote_hand
        retdic['turn_player'] = self.turn_player
        retdic['tempo'] = self.tempo
        return retdic

    def toggle_player(self):
        if self.turn_player == 'gote':
            self.turn_player = 'sente'
        else:
            self.turn_player = 'gote'
        return self.turn_player

    def board_geo(self, geo):
        geo_list = list(geo)
        i = 9 - int(geo_list[0])
        if geo_list[1] == 'a':
            j = 0
        if geo_list[1] == 'b':
            j = 1
        if geo_list[1] == 'c':
            j = 2
        if geo_list[1] == 'd':
            j = 3
        if geo_list[1] == 'e':
            j = 4
        if geo_list[1] == 'f':
            j = 5
        if geo_list[1] == 'g':
            j = 6
        if geo_list[1] == 'h':
            j = 7
        if geo_list[1] == 'i':
            j = 8
        return j, i

    def board_reverse_geo(self, i, j):
        vertical = str(9 - j)
        if i == 0:
            horizontal = 'a'
        if i == 1:
            horizontal = 'b'
        if i == 2:
            horizontal = 'c'
        if i == 3:
            horizontal = 'd'
        if i == 4:
            horizontal = 'e'
        if i == 5:
            horizontal = 'f'
        if i == 6:
            horizontal = 'g'
        if i == 7:
            horizontal = 'h'
        if i == 8:
            horizontal = 'i'
        return vertical + horizontal
        
    
    def move_peace(self, move):
        if move[0:1].isdigit():
            before_i, before_j = self.board_geo(move[0:2])
            move_peace = self.board[before_i][before_j]
            self.board[before_i][before_j] = ' '
        else:
            if self.turn_player == 'sente':
                move_peace = move[0:1]
                self.sente_hand[move[0:1]]-=1
            else:
                move_peace = move[0:1].lower()
                self.gote_hand[move[0:1]]-=1
                    
        after_i, after_j = self.board_geo(move[2:4])
        take_peace = self.board[after_i][after_j]
        if take_peace != ' ':
            if self.turn_player == 'sente':
                self.sente_hand[take_peace[0:1].upper()]+=1
            else:
                self.gote_hand[take_peace[0:1].upper()]+=1
        if len(move) == 5:
            self.board[after_i][after_j] = move_peace + '+'
        else:
            self.board[after_i][after_j] = move_peace
        self.toggle_player()
        self.tempo+=1
        
        retdic = {}
        retdic['board'] = self.board
        retdic['sente_hand'] = self.sente_hand
        retdic['gote_hand'] = self.gote_hand
        retdic['turn_player'] = self.turn_player
        retdic['tempo'] = self.tempo
        return retdic
        
    def set_startpos(
        self,
        startpos = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL',
        startplayer = 'b',
        startbelongings = '-',
        starttempo = '0',
        engine_turn = 'sente'):
        self.engine_turn = engine_turn
        
        startpos = startpos.replace('9', '         ')
        startpos = startpos.replace('8', '        ')
        startpos = startpos.replace('7', '       ')
        startpos = startpos.replace('6', '      ')
        startpos = startpos.replace('5', '     ')
        startpos = startpos.replace('4', '    ')
        startpos = startpos.replace('3', '   ')
        startpos = startpos.replace('2', '  ')
        startpos = startpos.replace('1', ' ')
        posstr_array = startpos.split('/')
        board = []
        for x in posstr_array:
            board.append(list(x))
        self.board = board

        if startplayer == 'b':
            turn_player = 'sente'
        else:
            turn_player = 'gote'
        self.turn_player = turn_player

        sente_hand = {'R': 0,'B': 0,'G': 0,'S': 0,'N': 0,'L': 0,'P': 0}
        gote_hand = {'R': 0,'B': 0,'G': 0,'S': 0,'N': 0,'L': 0,'P': 0}
        
        if startbelongings == '-':
            pass
        else:
            tempstr = startbelongings[::-1]
            isdigit = True
            input_position = []
            for i in range(len(tempstr)):
                if isdigit:
                    isdigit = False
                else:
                    if tempstr[i].isdigit():
                       isdigit = True
                    else:
                        input_position.append(i)
                        isdigit = False
            if not isdigit:
                input_position.append(len(tempstr))
            input_position = input_position[::-1]
            templist = list(tempstr)
            for x in input_position:
                templist.insert(x, '1')
            tempstr = ''.join(templist)
            startbelongings = tempstr[::-1]

            templist = list(startbelongings)
            for i in range(0, len(templist), 2):
                num = templist[i]
                peace = templist[i+1]
                if peace.isupper():
                    sente_hand[peace] = int(num)
                else:
                    gote_hand[peace.upper()] = int(num)
        self.sente_hand = sente_hand
        self.gote_hand = gote_hand

        tempo = int(starttempo)
        self.tempo = int(tempo)

        retdic = {}
        retdic['board'] = self.board
        retdic['sente_hand'] = self.sente_hand
        retdic['gote_hand'] = self.gote_hand
        retdic['turn_player'] = self.turn_player
        retdic['tempo'] = self.tempo
        retdic['engine_turn'] = self.engine_turn
        return retdic



if __name__ == '__main__':
    pass

    
