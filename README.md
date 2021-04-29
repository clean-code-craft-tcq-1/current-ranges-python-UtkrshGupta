# Test Driven Ranges

This exercise extends the [Battery Monitoring] use-case.

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input

Consider a set of periodic current samples from a charging session to be:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be:

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Start test-driven development:

1. Establish quality parameters for your project: What is the maximum complexity you would allow? How much duplication would you consider unacceptable? What is the coverage you'll aim for?
Adapt/adopt/extend the `yml` files from one of your workflow folders.

1. Write the smallest possible failing test.

1. Write the minimum amount of code that'll make it pass.

1. Write the next failing test.

Implement one failing test and at least one passing test:

- This time I have slightly changed and set the maximum CCN to be 5 just for a controlled run enviroment and also my logic can run felxibly. For other checks I haven't changed anything in, I considered them a fair check and did copy paste only.
- Smallest possible **failing** test is to test that the input should not be passed as empty -test_to_check_input_is_empty
- Smallest possible function for **Passing test** - get_current_range_frequency
- Another **failing** test is to test if input has any Nan or None - test_to_check_output_yields_invalid_if_input_has_nan, test_to_check_output_yields_invalid_if_input_has_None
- Smallest possible function for **Passing test** is to check for nan and None values before any reading or transformations - get_current_range_frequency
- Another **failing** test is to test if input has any non integer data ( in my example i have taken string data ) - test_to_check_impact_if_cuurent_values_are_passed_as_string
- Smallest possible code for **Passing test** is to add one statement check before producing results- 
if not all(isinstance(x, int) for x in data) - this particular line can check any mismatch of datatype in elements