from j_sapphon import JaneSapphon, Candidate, Lane

def C(id, confidence, carbon=True, synth=True, prior=True, prov=True, support=2, aligns=True):
    return Candidate(id, confidence, carbon, synth, prior, prov, support, aligns)

def run():
    j = JaneSapphon()
    assert j.ingest(C("root.v0", .995)) == Lane.VERIFIED
    assert j.current.id == "root.v0"
    assert j.ingest(C("unknown", .75, support=1)) == Lane.QUARANTINE
    assert j.current.id == "root.v0"
    assert j.ingest(C("minority", .999, support=4, aligns=False)) == Lane.NON_ALIGNED
    assert j.current.id == "root.v0"
    assert j.ingest(C("no-carbon", .999, carbon=False, support=4)) == Lane.QUARANTINE
    assert j.ingest(C("root.v1", .999, support=3)) == Lane.VERIFIED
    assert (j.past.id, j.current.id) == ("root.v0", "root.v1")
    assert j.ingest(C("root.v2", .9999, support=5)) == Lane.VERIFIED
    assert (j.past.id, j.current.id) == ("root.v1", "root.v2")
    assert [x.id for x in j.archive] == ["root.v0"]
    print("0e / J.SAPPHON AIRLOCK PASS")

if __name__ == "__main__":
    run()
