from sizing import position_size

def test_full_size_at_target_vol():
    assert position_size(1.0, 0.02) == 1000

def test_halves_when_vol_doubles():
    assert position_size(1.0, 0.04) == 500

def test_short_and_no_levering_up():
    assert position_size(-0.5, 0.01) == -500

def test_signal_is_capped():
    assert position_size(3.0, 0.02) == 1000

def test_zero_vol_means_flat():
    assert position_size(1.0, 0.0) == 0