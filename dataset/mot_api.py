from icecream import ic

from .mots_fr import MOTS

banned = set()


def get_mot_by_seq(seq: str) -> str:
    ic(f"try to get words for {seq}")
    seq = seq.lower()
    mot = next((mot for mot in MOTS if seq in mot and mot not in banned), None)
    if mot is None:
        raise ValueError(f"mot with `{seq}` not found")
    return mot
