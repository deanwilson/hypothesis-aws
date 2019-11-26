# hypothesis-aws
A hypothesis extension that provides AWS related strategies


## Running locally

    git clone https://github.com/deanwilson/hypothesis-aws.git
    cd hypothesis-aws

    # install the package locally
    pip install -e .

    # run the region tests to see hypothesis in action
    pytest example/show-regions.py --hypothesis-show-statistics -s

    example/show-regions.py Trying example: test_display_region(region='ap-central-1')
    Trying example: test_display_region(region='sa-central-4')
    Trying example: test_display_region(region='ap-gov-central-1')
    Trying example: test_display_region(region='ap-northwest-1')
    Trying example: test_display_region(region='sa-gov-central-4')
    Trying example: test_display_region(region='me-northwest-4')
    Trying example: test_display_region(region='sa-gov-southeast-4')
    Trying example: test_display_region(region='me-gov-west-8')
    Trying example: test_display_region(region='eu-east-3')
    Trying example: test_display_region(region='me-gov-northwest-7')
    .
    =========================================== Hypothesis Statistics ============================================

    example/show-regions.py::test_display_region:
    
      - 10 passing examples, 0 failing examples, 0 invalid examples
      - Typical runtimes: 0-2 ms
      - Fraction of time spent in data generation: ~ 65%
      - Stopped because settings.max_examples=10

## Strategies

 * Real Regions
 * Fake Regions

### Real regions

The real region strategy provides the currently existing AWS regions, one at a
time. You can see it in action by running:

    pytest example/show-real-regions.py --hypothesis-show-statistics -s

    ... snip ...
    Trying example: test_display_region(region='ap-northeast-1')
    Trying example: test_display_region(region='us-gov-west-1')
    Trying example: test_display_region(region='me-south-1')
    Trying example: test_display_region(region='eu-west-3')
    ... snip ...

### Fake regions

This strategy creates probably fictious (it will eventually also return the real
regions) AWS region names. It uses the rules all the current regions conform to -

 * 2 letters describing 
 * hyphen
 * optional `gov`-
 * cardinal direction
 * hyphen
 * single digit - 1-9

    pytest example/show-regions.py --hypothesis-show-statistics -s

    example/show-regions.py Trying example: test_display_region(region='ap-central-1')
    Trying example: test_display_region(region='sa-central-4')
    Trying example: test_display_region(region='ap-gov-central-1')
    Trying example: test_display_region(region='ap-northwest-1')
    Trying example: test_display_region(region='sa-gov-central-4')
    Trying example: test_display_region(region='me-northwest-4')
    Trying example: test_display_region(region='sa-gov-southeast-4')

### Author

 * [Dean Wilson](https://www.unixdaemon.net)
