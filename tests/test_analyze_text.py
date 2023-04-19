from toxicTrig import toxicTrig 

def test_analyze_text() -> None:
    tt = toxicTrig()
    counts = tt.text_analysis(["This is a test sentence, we have some toxic trig words here: 2g1c, babeland, queers"], batch_size=1)
    assert isinstance(counts, dict)
    assert counts["harmless-minority"] == 1
    assert counts["offensive-minority-reference"] == 1
    assert counts["offensive-not-minority"] == 1
    # TODO: add more tests