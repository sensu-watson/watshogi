import unittest
from board import *

class BoardTest(unittest.TestCase):
    def test_calc_best_move(self):
        myboard = Board()
        myboard.set_startpos()

        ret_str, ret_int = myboard.calc_best_move()
        
        self.assertIsInstance(ret_str, str)
        self.assertIsInstance(ret_int, int)
        
    def test_evaluation_value(self):
        myboard = Board()
        myboard.set_startpos()

        ret = myboard.evaluation_value()
        exc_g = -10000
        exc_l = 10000

        self.assertGreater(ret, exc_g)
        self.assertLess(ret, exc_l)
        
    def test_puttable_piece(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            'PPP3PPP/9/9/9/9/9/9/9/9',
            startbelongings = 'PLNSGR'
            )
        geo = '3c'

        ret = myboard.puttable_piece(geo)
        exc = ['L*', 'N*', 'S*', 'G*', 'R*']

        self.assertCountEqual(ret, exc)

    def test_movable_place_promote_r_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4r4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_promote_r(geo)
        exc = ['5e', '5d', '5c', '5b', '5a',
               '4f', '3f', '2f', '1f',
               '6f', '7f', '8f', '9f',
               '5g', '5h', '5i',
               '4e', '4g', '6e', '6g']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_promote_b_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4b4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_promote_b(geo)
        exc = ['4e', '3d', '2c', '1b',
               '6e', '7d', '8c', '9b',
               '4g', '3h', '2i',
               '6g', '7h', '8i',
               '5e', '5g', '4f', '6f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_k_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4k4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_k(geo)
        exc = ['4d', '5d', '6d',
               '4e', '6e',
               '4f', '5f', '6f']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_r_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4r4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_r(geo)
        exc = ['5e', '5d', '5c', '5b', '5a',
               '4f', '3f', '2f', '1f',
               '6f', '7f', '8f', '9f',
               '5g', '5h', '5i']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_b_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4b4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_b(geo)
        exc = ['4e', '3d', '2c', '1b',
               '6e', '7d', '8c', '9b',
               '4g', '3h', '2i',
               '6g', '7h', '8i']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_g_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4g4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_g(geo)
        exc = ['5d', '6e', '4e', '4f', '5f', '6f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_s_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4s4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_s(geo)
        exc = ['4d', '6d', '4f', '5f', '6f']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_n_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4n4/9/9/9/9/9/9/9/9'
            )
        geo = '5a'

        ret = myboard.movable_place_N(geo)
        exc = ['4c', '6c']

    def test_movable_place_l_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4l4/9/9/9/9/9/9/9/9'
            )
        geo = '5a'

        ret = myboard.movable_place_l(geo)
        exc = ['5b', '5c', '5d', '5e', '5f', '5g', '5h', '5i']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_p_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4p4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_p(geo)
        exc = ['5f']
        
        self.assertCountEqual(ret, exc)
    
    def test_movable_place_promote_R_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4R4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_promote_R(geo)
        exc = ['5e', '5d', '5c', '5b', '5a',
               '4f', '3f', '2f', '1f',
               '6f', '7f', '8f', '9f',
               '5g', '5h', '5i',
               '4e', '4g', '6e', '6g']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_promote_B_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4B4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_promote_B(geo)
        exc = ['4e', '3d', '2c', '1b',
               '6e', '7d', '8c', '9b',
               '4g', '3h', '2i',
               '6g', '7h', '8i',
               '5e', '5g', '4f', '6f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_K_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4K4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_K(geo)
        exc = ['4d', '5d', '6d',
               '4e', '6e',
               '4f', '5f', '6f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_R_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4R4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_R(geo)
        exc = ['5e', '5d', '5c', '5b', '5a',
               '4f', '3f', '2f', '1f',
               '6f', '7f', '8f', '9f',
               '5g', '5h', '5i']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_B_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/4B4/9/9/9'
            )
        geo = '5f'

        ret = myboard.movable_place_B(geo)
        exc = ['4e', '3d', '2c', '1b',
               '6e', '7d', '8c', '9b',
               '4g', '3h', '2i',
               '6g', '7h', '8i']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_G_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4G4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_G(geo)
        exc = ['4d', '5d', '6d', '4e', '6e', '5f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_S_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/4S4/9/9/9/9'
            )
        geo = '5e'

        ret = myboard.movable_place_S(geo)
        exc = ['4d', '5d', '6d', '4f', '6f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_N_1(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/9/9/9/4N4'
            )
        geo = '5i'

        ret = myboard.movable_place_N(geo)
        exc = ['4g', '6g']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_N_2(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '9/9/9/9/9/9/3P1p3/9/4N4'
            )
        geo = '5i'

        ret = myboard.movable_place_N(geo)
        exc = ['4g']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_L_1(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '9i'

        ret = myboard.movable_place_L(geo)
        exc = ['9h']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_L_2(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4k4/9/4p4/9/9/9/4P4/9/4K3L'
            )
        geo = '1i'

        ret = myboard.movable_place_L(geo)
        exc = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_L_3(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4k4/9/4p3p/9/9/9/4P4/9/4K3L'
            )
        geo = '1i'

        ret = myboard.movable_place_L(geo)
        exc = ['1c', '1d', '1e', '1f', '1g', '1h']
        
        self.assertCountEqual(ret, exc)

    def test_movable_place_P_1(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7g'

        ret = myboard.movable_place_P(geo)
        exc = ['7f']
        
        self.assertCountEqual(ret, exc)
        
    def test_movable_place_P_2(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4k4/9/4p4/4l4/9/4L4/4P4/9/4K4'
            )
        geo = '5g'

        ret = myboard.movable_place_P(geo)
        exc = []

        self.assertCountEqual(ret, exc)

    def test_is_exist_piece_1(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7f'

        ret = myboard.is_exist_piece(geo)
        exc = False

        self.assertEqual(ret, exc)

    def test_is_exist_piece_2(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7g'

        ret = myboard.is_exist_piece(geo)
        exc = True

        self.assertEqual(ret, exc)

    def test_is_exist_turnplayer_piece_1(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7f'

        ret = myboard.is_exist_turnplayer_piece(geo)
        exc = False

        self.assertEqual(ret, exc)

    def test_is_exist_turnplayer_piece_2(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7g'

        ret = myboard.is_exist_turnplayer_piece(geo)
        exc = True

        self.assertEqual(ret, exc)

    def test_is_exist_turnplayer_piece_3(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '3c'

        ret = myboard.is_exist_turnplayer_piece(geo)
        exc = False

        self.assertEqual(ret, exc)

    def test_generate_next_move(self):
        myboard = Board()
        myboard.set_startpos(
            startpos =
            '4k4/9/4p4/9/9/9/4P4/9/4K4',
            starttempo = '0'
            )

        exc = ['5g5f', '5i6i', '5i6h', '5i5h', '5i4i', '5i4h']

        ret = myboard.generate_next_move()
        self.assertCountEqual(ret, exc)

    def test_board_reverse_geo_1(self):
        myboard = Board()
        myboard.set_startpos()
        i = 5
        j = 2
        
        exc = '7f'
        ret = myboard.board_reverse_geo(i, j)
        self.assertEqual(ret, exc)
        

    def test_generate_state(self):
        myboard = Board()
        myboard.set_startpos()

        moves = ['7g7f', '3c3d', '8h2b+']
        exc = {'board':
               [['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
                [' ', 'r', ' ', ' ', ' ', ' ', ' ', 'B+', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' '],
                ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
                ],
               'sente_hand':{
                   'R': 0,
                   'B': 1,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'gote_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'turn_player':'gote',
               'tempo':3}

        ret = myboard.generate_state(moves)
        self.assertEqual(ret, exc)
        

    def test_toggle_player_1(self):
        myboard = Board()
        myboard.set_startpos()
        exc = 'gote'
        ret = myboard.toggle_player()
        self.assertEqual(ret, exc)

    def test_toggle_player_2(self):
        myboard = Board()
        myboard.set_startpos()
        exc = 'sente'
        _ = myboard.toggle_player()
        ret = myboard.toggle_player()
        self.assertEqual(ret, exc)

    def test_board_geo_1(self):
        myboard = Board()
        myboard.set_startpos()
        geo = '7f'
        
        exc_i = 5
        exc_j = 2
        ret_i, ret_j = myboard.board_geo(geo)
        self.assertEqual(ret_i, exc_i)
        self.assertEqual(ret_j, exc_j)

    def test_move_peace_1(self):
        myboard = Board()
        myboard.set_startpos()

        move = '7g7f'
        exc = {'board':
               [['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
                [' ', 'r', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', 'B', ' ', ' ', ' ', ' ', ' ', 'R', ' '],
                ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
                ],
               'sente_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'gote_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'turn_player':'gote',
               'tempo':1}

        ret = myboard.move_peace(move)
        self.assertEqual(ret, exc)

    def test_move_peace_2(self):
        myboard = Board()
        ret = myboard.set_startpos(
            startpos =
            'lnsgkgsnl/1r5b1/pppppp1pp/6p2/9/2P6/PP1PPPPPP/1B5R1/LNSGKGSNL',
            starttempo = '2'
            )

        move = '8h2b+'
        exc = {'board':
               [['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
                [' ', 'r', ' ', ' ', ' ', ' ', ' ', 'B+', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', ' ', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', ' ', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' '],
                ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
                ],
               'sente_hand':{
                   'R': 0,
                   'B': 1,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'gote_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'turn_player':'gote',
               'tempo':3}

        ret = myboard.move_peace(move)
        self.assertEqual(ret, exc)

    def test_set_startpos_1(self):
        myboard = Board()
        startpos = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL'
        startplayer = 'b'
        startbelongings = '-'
        starttempo = '0'
        
        exc = {'board':
               [['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
                [' ', 'r', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', 'B', ' ', ' ', ' ', ' ', ' ', 'R', ' '],
                ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
                ],
               'sente_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'gote_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'turn_player':'sente',
               'tempo':0,
               'engine_turn':'sente'}
        
        ret = myboard.set_startpos(
            startpos, startplayer, startbelongings, starttempo)
        self.assertEqual(ret, exc)
        
    def test_set_startpos_2(self):
        myboard = Board()
        startpos = 'lnsgkgsnl/9/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL'
        startplayer = 'w'
        startbelongings = 'r2b'
        starttempo = '1'
        
        exc = {'board':
               [['l', 'n', 's', 'g', 'k', 'g', 's', 'n', 'l'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                [' ', 'B', ' ', ' ', ' ', ' ', ' ', 'R', ' '],
                ['L', 'N', 'S', 'G', 'K', 'G', 'S', 'N', 'L']
                ],
               'sente_hand':{
                   'R': 0,
                   'B': 0,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'gote_hand':{
                   'R': 1,
                   'B': 2,
                   'G': 0,
                   'S': 0,
                   'N': 0,
                   'L': 0,
                   'P': 0,
                   },
               'turn_player':'gote',
               'tempo':1,
               'engine_turn':'sente'}
        
        ret = myboard.set_startpos(
            startpos = startpos, startplayer = startplayer,
            startbelongings = startbelongings, starttempo = starttempo)
        self.assertEqual(ret, exc)

if __name__ == '__main__':
    unittest.main()
