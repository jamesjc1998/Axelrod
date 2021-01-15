from typing import Optional

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class UTFT(Player):
    """
  Adapted from the 'Adaptive Pavlov 2006' strategy. 
  UTFT classifies the opponent as 'Neutral' or 'Defector' on a rolling basis. 
  If former, then TFT played.
  If latter, then defect to encourage opponent to cooperate more often, or to minimise losses.
    """

    name = "UTFT"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self) -> None:
        super().__init__()
        self.opponent_class = None  # type: Optional[str]

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        # TFT for six rounds
        if len(self.history) < 6:
            return D if opponent.history[-1:] == [D] else C
        else:
        # Classify opponent
            if (opponent.history[-6:]).count('D') > 2:
                self.opponent_class = "Defector"
            else:
                self.opponent_class = "Neutral"

        # Play according to classification
        if self.opponent_class == "Defector":
            return D
        else:
            return D if opponent.history[-1:] == [D] else C
              
