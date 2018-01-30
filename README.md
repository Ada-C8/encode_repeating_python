# Encode Repeating in Python
In this assignment, you'll design and implement one of the string manipulation functions that is commonly asked during interviews.

## Exercise
* Design and implement a function that encodes a string by replacing consecutive repeating characters with a number representing the frequency. The replacement is done only if the string length will get reduced by the process. For example:
   - an input of "aaabbbbbcccc" will return "a3b5c4", since "a" is repeated 3 times, "b" is repeated 5 times and "c" is repeated 4 times.
   - an input of "xxxyttttgeee" will return "x3yt4ge3". "y" and "g" are not replaced by "y1" and "g1" since that will increase the length.
   - an input of "ddbbfffgjjjj" will return "ddbbf3gj4". "dd" and "bb" are not replaced since the length would remain the same with "d2" and "b2". "g" is not replaced with "g1" since that will increase the length.
* Share and explain the time and space complexities for your solution.
* At minimum, your implementation should pass the basic tests.

**Further reading**: Read further on [Run-length encoding (RLE)](https://en.wikipedia.org/wiki/Run-length_encoding), the simple form of loss-less data compression that this assignment is based on.

## Python Considerations
The Ruby version of this assignment involved manipulating a string in place. Unlike Ruby strings, Python strings are immutable, which means they can't be changed after they are initialized. Because strings cannot be modified in place, a new string must be created whenever a change must be made to a string.

**Note**: Do not use Python provided functionality for `reversed()` or `reverse()`. You may use `len()` and string slicing (`"string"[1:5]`) to implement this function.

## Running the Tests
Install `pytest`
```terminal
pip install pytest
```
To run all tests, navigate to the same directory as the test file and run:
```terminal
pytest test_encode_repeating.py
```
Alternatively, to exit instantly on first error or failed test, run:
```terminal
pytest -x test_encode_repeating.py
```

See [pytest documentation](http://pytest.org/latest/) for more information about `pytest`.
