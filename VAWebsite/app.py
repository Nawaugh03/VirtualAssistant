def calculate_xp(level, base_xp=100, growth_factor=1.5):
    """
    Calculate the XP required to reach a specific level using an exponential formula.
    
    :param level: The target level (integer).
    :param base_xp: The XP required to reach level 2 (default is 100).
    :param growth_factor: The multiplier for each level (default is 1.5).
    :return: XP required to reach the specified level.
    """
    if level < 1:
        return 0  # No XP required for levels below 1

    # Calculate XP required for the given level
    xp_required = base_xp * (growth_factor ** (level - 1))
    return xp_required

# Example Usage
for i in range(1, 11):  # Calculate XP for levels 1 to 10
    xp = calculate_xp(i)
    print(f"Level {i}: {xp:.2f} XP required")