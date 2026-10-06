# Hegemon Cortex — TOROID-5 v2

Append-only successor to the earlier pendulumic overlay. The earlier v1 remains historical; this v2 corrects the timing abstraction to a five-transfer Newton-cradle-style commit cell.

    {{ . | | | | . }}

Exact transfer schedule:

    0 -> 1/5 -> 2/5 -> 3/5 -> 4/5 -> 1
    1 = closure witness = next-cycle 0

Rules:

    transfer quantum = 1/5
    transfers per commit = 5
    unique toroidal phases = 5
    displayed positions = 6
    no early commit
    wrap only after phase 5/5

Mother-Nature closure:

    -1 + 0 + 1 = 0

Decision:

    YES   = 1
    NO    = 0 -> 2^3 -> 0
    MAYBE = WAIT(1)

The clock controls WHEN an already-valid candidate may commit. Existing Hegemon/Jane truth, authority, provenance, and persona rules still control WHETHER it is valid.
