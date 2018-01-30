from encode_repeating import encode_repeating


# Basic Tests
def test_encode_repeating_with_repeating_characters():
    test_string = "aaabbbbbcccc"

    assert encode_repeating(test_string) == "a3b5c4"


def test_encode_repeating_with_single_characters():
    test_string = "xxxyttttgeee"

    assert encode_repeating(test_string) == "x3yt4ge3"


def test_encode_repeating_with_single_and_double_characters():
    test_string = "ddbbfffgjjjj"

    assert encode_repeating(test_string) == "ddbbf3gj4"


# Edge Cases
def test_encode_repeating_returns_unmodified_with_empty_string():
    test_string = ""

    assert encode_repeating(test_string) == ""


def test_encode_repeating_returns_unmodified_with_None():
    test_string = None

    assert encode_repeating(test_string) is None


def test_encode_repeating_with_no_consecutive_repeating_characters():
    test_string = "aeiou"

    assert encode_repeating(test_string) == "aeiou"


def test_encode_repeating_with_repeating_spaces():
    test_string = "hi    there"

    assert encode_repeating(test_string) == "hi 4there"
