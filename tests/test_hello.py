from hello import greet


def test_default_greeting():
    assert greet() == "Hello, world!"


def test_named_greeting():
    assert greet("Ada") == "Hello, Ada!"


def test_blank_name_falls_back():
    assert greet("   ") == "Hello, world!"
