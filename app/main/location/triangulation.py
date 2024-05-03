import math
from typing import List, Tuple

from models import GsmCell


# https://ieeexplore.ieee.org/abstract/document/7456592
# Has multiple flaws:
# 1. Does not account for the fact that all the math is happening on spheroid
# 2. Does not account for the fact that signal strength may not correlate with real position
#    (1 tower may be blocked by an iron sheet, while others are not)
def triangulate(gsmtowers: List[GsmCell]) -> Tuple[float, float]:
    locations: List[Tuple[float, float]] = [(t.location.latitude, t.location.longitude) for t in gsmtowers]
    strength: List[float] = [t.signal_strength for t in gsmtowers]
    min_strength: float = min(strength)
    strength_shifted: List[float] = [(r - min_strength) for r in strength]

    locations_weighted: List[Tuple[float, float]] = [(i * s, j * s) for (i, j), s in zip(locations, strength_shifted)]
    final_location: Tuple[float, float] = (
        math.fsum([i for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
        math.fsum([j for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
    )
    return final_location
