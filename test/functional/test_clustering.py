import math

import pytest

from poker_ai.clustering.card_combos import CardCombos


def _get_num_combos(n: int, r: int):
    """Return number of combinations.

    Parameters
    ----------
    n : int
        Number to choose from
    r : int
        Number to choose
    """
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


@pytest.mark.parametrize("low_card_rank", [11, 12])
def test_clustering_1(low_card_rank: int):
    """Test the number of cards created."""
    high_card_rank = 14
    card_combos = CardCombos(
        low_card_rank=low_card_rank,
        high_card_rank=high_card_rank,
        disk_cache=False
    )
    n_cards = len(card_combos._cards)
    n_hole_cards = _get_num_combos(n_cards, 2)
    assert len(card_combos.starting_hands) == n_hole_cards
    # Number of hole card, and separately public card, combinations.
    assert len(card_combos.flop) == _get_num_combos(n_cards - 2, 3) * n_hole_cards
    assert len(card_combos.turn) == _get_num_combos(n_cards - 2, 4) * n_hole_cards
    assert len(card_combos.river) == _get_num_combos(n_cards - 2, 5) * n_hole_cards