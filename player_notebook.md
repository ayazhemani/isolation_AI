
# Isolation

This IPython notebook contains the skeletons of the player class and eval function classes that you need to fill out. In addition, we have included the `RandomPlayer` and `HumanPlayer` classes for you to test against.

## Submitting

When you are ready to submit, copy code from the following classes into the attached `player_submission.py`:

1. OpenMoveEvalFn
1. CustomEvalFn
1. CustomPlayer

Please do not copy any code that is not part of those classes. You may be tempted to simply export a python file from this notebook and use that as a submission; please **DO NOT** do that. We need to be certain that code unprotected by a *main* test (any tests that you might want to write) do not get accidentally executed

## Helper Player classes

We include 2 player types for you to test against locally:

- `RandomPlayer` - chooses a legal move randomly from among the available legal moves
- `HumanPlayer` - allows *YOU* to play against the AI

**DO NOT** submit.

You are however free to change these classes as you see fit. Know that any changes you make will be solely for the benefit of your own tests.


```python
from random import randint

class RandomPlayer():
    """Player that chooses a move randomly."""
    def move(self, game, legal_moves, time_left):
        if not legal_moves: return (-1,-1)
        return legal_moves[randint(0,len(legal_moves)-1)]
```


```python
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
```

## Evaluation Functions

These functions will inform the value judgements your AI will make when choosing moves. There are 2 classes:

- `OpenMoveEvalFn` - Scores the number of moves open for the active player. All baseline tests will use this function. Mandatory
- `CustomEvalFn` - You are encouraged to create your own evaluation function here.

**DO** submit code within the classes (and only that within the classes).

### Tips

1. You may write additional code within each class. However, we will only be invoking the `score()` function. You may not change the signature of this function.
1. When writing additional code to test, try to do so in separate cells. It allows for independent test execution and you can be sure that *all* the code within the EvalFn cells belong only to the EvalFn classes


```python
class OpenMoveEvalFn():
    """Evaluation function that outputs a 
    score equal to how many moves are open
    for the active player."""
    def score(self, game):
        # TODO: finish this function!
        return eval_func
```


```python
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""
    def score(self, game):
        # TODO: finish this function!
        return eval_func
```

### Tests

We've included some sample code to test the evaluation functions. Change as you see fit. **DO NOT** submit.


```python
"""Example test you can run
to make sure your basic evaluation
function works."""
from isolation import Board

if __name__ == "__main__":
    sample_board = Board(RandomPlayer(),RandomPlayer())
    # setting up the board as though we've been playing
    sample_board.move_count = 3
    sample_board.__active_player__ = 0 # player 1 = 0, player 2 = 1
    # 1st board = 7 moves
    sample_board.__board_state__ = [
                [0,2,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]
    ]
    sample_board.__last_player_move__ = {0: (2,2), 1: (0,1)}

    # player 1 should have 7 moves available,
    # so board gets a score of 7
    h = OpenMoveEvalFn()
    print('This board has a score of %s.'%(h.score(sample_board)))
```

## CustomPlayer

This is the meat of the assignment. A few notes about the class:

- You are not permitted to change the function signatures of any of the provided methods.
- You are permitted to change the default values within the function signatures provided. In fact, when you have your custom evaluation function, you are encouraged to change the default values for `__init__` to use the new eval function.
- You are free change the contents of each of the provided methods. When you are ready with `alphabeta()`, for example, you are encouraged to update `move()` to use that function instead.
- You are free to add more methods to the class.
- You may not create additional external functions and classes that are referenced from within this class.

**DO** submit the code within this class (and only the code within this class).


```python
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
        return best_move, best_val

    def alphabeta(self, game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        return best_move, best_val
```

### Tests

We've included some code to help you test your player as well as to give you an idea of how the players are invoked. Feel free to play around with the code and add more tests.

**DO NOT** submit.


```python
"""Example test to make sure
your minimax works, using the
#my_moves evaluation function."""
from isolation import Board

if __name__ == "__main__":
    # create dummy 3x3 board
    p1 = CustomPlayer(search_depth=3)
    p2 = CustomPlayer()
    b = Board(p1,p2,3,3)
    b.__board_state__ = [
        [0,2,0],
        [0,0,1],
        [0,0,0]
    ]
    b.__last_player_move__[p1] = (1,2)
    b.__last_player_move__[p2] = (0,1)
    # use minimax to determine optimal move 
    # sequence for player 1
    b.play_isolation()
    # your output should look like this:
    """
    ####################
      | 2 |   | 
      |   | 1 | 
      |   |   | 

    ####################
    ####################
    1 | 2 |   | 
      |   | - | 
      |   |   | 

    ####################
    ####################
    1 | - |   | 
      |   | - | 
      |   | 2 | 

    ####################
    ####################
    - | - |   | 
      |   | - | 
      | 1 | 2 | 

    ####################
    ####################
    - | - |   | 
    2 |   | - | 
      | 1 | - | 

    ####################
    ####################
    - | - | 1 | 
    2 |   | - | 
      | - | - | 

    ####################
    Illegal move at -1,-1.
    Player 1 wins.
    """
```


```python
"""Example test you can run
to make sure your AI does better
than random."""
from isolation import Board

if __name__ == "__main__":
    r = RandomPlayer()
    h = CustomPlayer()
    game = Board(h,r)
    game.play_isolation()
```
