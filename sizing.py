def position_size(signal: float, vol: float, target_vol: float = 0.02, cap: int = 1000) -> int:
    """Shares to hold for a signal in [-1, 1] at today's volatility.

    Full size (cap shares) when vol equals target_vol, smaller when vol is higher,
    never larger than cap when vol is lower; the signal is clipped to [-1, 1];
    zero or negative vol means stay flat. Truncate to an int.
    """
    raise NotImplementedError  # TODO: the feature you ship in this quiz