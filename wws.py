class WWS(Player):
    """
    Half Lazy TFT

    A player starts by cooperating and then on only responds to opponent defects
    every other time, otherwise the player just cooperates.

    Code is slight moficiation of original TFT strategy.
    Can be classified as "nice".

    """

    # These are various properties for the strategy
    name = "Half Lazy TFT"
    classifier = {
        "memory_depth": 1,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        # First move
        if not self.history:
            return C
        # React to the opponent's every other move (if defection)
        if opponent.defections>1 and opponent.defections%2==0:
            return D
        return C
