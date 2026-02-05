from rohonchain_strategy.arbitrage.constraints import one_hot_constraints


def test_one_hot():
    cs = one_hot_constraints('x', [0,1])
    assert len(cs) == 2
