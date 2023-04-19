from toxicTrig import toxicTrig 

def test_get_words() -> None:
    tt = toxicTrig()
    assert isinstance(tt.NOI, list)
    assert isinstance(tt.OI, list)
    assert isinstance(tt.ONI, list)