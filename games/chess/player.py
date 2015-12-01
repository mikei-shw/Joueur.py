# Generated by Creer at 04:13PM on December 01, 2015 UTC, git hash: '1b69e788060071d644dd7b8745dca107577844e1'
# This is a simple class to represent the Player object in the game. You can extend it by adding utility functions here in this file.

from games.chess.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """ The class representing the Player in the Chess game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """ initializes a Player with basic logic as provided by the Creer code generator
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._client_type = ""
        self._color = None
        self._file_direction = 0
        self._in_check = False
        self._lost = False
        self._made_move = False
        self._name = "Anonymous"
        self._other_player = None
        self._pieces = []
        self._reason_lost = ""
        self._reason_won = ""
        self._time_remaining = 0
        self._won = False



    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        """
        return self._client_type


    @property
    def color(self):
        """The color (side) of this player. Either 'White' or 'Black', with the 'White' player having the first move.
        """
        return self._color


    @property
    def file_direction(self):
        """The direction your checkers must go along the file (y) axis until they reach the other side.
        """
        return self._file_direction


    @property
    def in_check(self):
        """true if this player is currently in check, and must move out of check.
        """
        return self._in_check


    @property
    def lost(self):
        """if the player lost the game or not
        """
        return self._lost


    @property
    def made_move(self):
        """If the Player has made thier move for the turn. true means they can no longer move a piece this turn.
        """
        return self._made_move


    @property
    def name(self):
        """The name of the player
        """
        return self._name


    @property
    def other_player(self):
        """this player's opponent in the game.
        """
        return self._other_player


    @property
    def pieces(self):
        """All the unpcaptured chess pieces owned by this player.
        """
        return self._pieces


    @property
    def reason_lost(self):
        """the reason why the player lost the game
        """
        return self._reason_lost


    @property
    def reason_won(self):
        """the reason why the player won the game
        """
        return self._reason_won


    @property
    def time_remaining(self):
        """The amount of time (in ns) remaining for this AI to send commands.
        """
        return self._time_remaining


    @property
    def won(self):
        """if the player won the game or not
        """
        return self._won



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>