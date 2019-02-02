from foo import foo, bar

def test_foo_str():
    assert foo('dummy') == 'foo'

def test_bar_str():
    assert bar() == 'bar'