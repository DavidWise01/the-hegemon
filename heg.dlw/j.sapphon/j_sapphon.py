"""j.sapphon — Hegemon GEN-1 truth airlock."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List

class Lane(str, Enum):
    VERIFIED = "verified"
    QUARANTINE = "quarantine"
    NON_ALIGNED = "non_aligned"

@dataclass(frozen=True)
class Candidate:
    id: str
    confidence: float
    carbon_support: bool
    synthetic_support: bool
    prior_support: bool
    provenance_ok: bool = True
    independent_support: int = 1
    aligns: Optional[bool] = None

@dataclass(frozen=True)
class State:
    id: str
    confidence: float

@dataclass
class JaneSapphon:
    threshold: float = 0.99
    min_independent_support: int = 2
    past: Optional[State] = None
    current: Optional[State] = None
    archive: List[State] = field(default_factory=list)
    quarantine: List[Candidate] = field(default_factory=list)
    non_aligned: List[Candidate] = field(default_factory=list)

    def merit(self, c: Candidate) -> bool:
        quorum = c.carbon_support and c.synthetic_support and c.prior_support
        return quorum and c.provenance_ok and c.independent_support >= self.min_independent_support and c.confidence >= self.threshold

    def ingest(self, c: Candidate) -> Lane:
        if c.aligns is False:
            self.non_aligned.append(c)
            return Lane.NON_ALIGNED
        if not self.merit(c):
            self.quarantine.append(c)
            return Lane.QUARANTINE
        self._carry(State(c.id, c.confidence))
        return Lane.VERIFIED

    def _carry(self, state: State) -> None:
        if self.past is not None:
            self.archive.append(self.past)
        self.past = self.current
        self.current = state

    def hot(self):
        return self.past, self.current
