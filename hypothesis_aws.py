from hypothesis.strategies import from_regex, sampled_from
import re


def regions():

    real_regions = [
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-north-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-south-1",
        "sa-east-1",
        "us-east-1",
        "us-east-2",
        "us-gov-east-1",
        "us-gov-west-1",
        "us-west-1",
        "us-west-2",
    ]

    return sampled_from(real_regions)

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
