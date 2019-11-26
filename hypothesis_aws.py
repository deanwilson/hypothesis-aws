from hypothesis.strategies import from_regex
import re


def fake_regions():
    """Generate fake regions that match the AWS region naming format"""

    # all of these are real codes
    region_codes = [
        "ap",
        "ca",
        "cn",
        "eu",
        "me",
        "sa",
        "us",
    ]

    cardinal_directions = [
        "central",
        "north",
        "northeast",
        "northwest",
        "south",
        "southeast",
        "southwest",
        "east",
        "west",
    ]

    # no current region has more than a single digit at the end
    region_number = list(range(1, 10))

    alternation_regions = "|".join(region_codes)
    alternation_directions = "|".join(cardinal_directions)
    alternation_number = "|".join(str(i) for i in region_number)

    # Build a horrible regex with lots of literal alternations
    pattern = re.compile(
        f"({alternation_regions})-(gov-)?({alternation_directions})-({alternation_number})"
    )

    return from_regex(pattern, fullmatch=True)
