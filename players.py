#!/usr/bin/env python


from random import randint

class RandomPlayer():
    """Player that chooses a move randomly."""
    def move(self, game, legal_moves, time_left):
        print('\t'.join(['[%d] %s'%(i,str(move)) for i,move in enumerate(legal_moves)] ))
		
        if not legal_moves: return (-1,-1)
        return legal_moves[randint(0,len(legal_moves)-1)]

class HumanPlayer():
    """Player that chooses a move according to
    user's input."""
    def move(self, game, legal_moves, time_left):
        print('\t'.join(['[%d] %s'%(i,str(move)) for i,move in enumerate(legal_moves)] ))
        
        valid_choice = False
        while not valid_choice:
            try:
                index = int(raw_input('Select move index:'))
                valid_choice = 0 <= index < len(legal_moves)

                if not valid_choice:
                    print('Illegal move! Try again.')
            
            except ValueError:
                print('Invalid index! Try again.')
        return legal_moves[index]
		
# Submission Class 1
class OpenMoveEvalFn():
    """Evaluation function that outputs a
    score equal to how many moves are open
    for the active player."""
    def score(self, game):
        # TODO: finish this function!
        eval_func=len(self.get_legal_moves())
        return eval_func

# Submission Class 2
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""
    def score(self, game):
        # TODO: finish this function!
        eval_func=legal_moves
        return eval_func

# Submission Class 3
class CustomPlayer():
    # TODO: finish this class!
    """Player that chooses a move using
    your evaluation function and
    a depth-limited minimax algorithm
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 1000 milliseconds."""
    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, legal_moves, time_left):

        best_move, utility = self.minimax(game, depth=self.search_depth)
        # you will eventually replace minimax with alpha-beta
        return best_move

    def utility(self, game):

        if game.is_winner(self):
            return float("inf")

        if game.is_opponent_winner(self):
            return float("-inf")

        return self.eval_fn.score(game)

    def minimax(self, game, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        branches=[]
        legal_moves = game.get_legal_moves()
        for branch in legal_moves:
            branches.append(self.eval_fn(game.forecast_move(branch)))
        best_move = legal_moves[branches.index(max(branches))]
        return best_move, best_val

    def alphabeta(self, game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        return best_move, best_val
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
