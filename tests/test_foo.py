from foo import foo, bar

def test_foo():
    assert foo('dummy') == 'foo'

def test_bar():
    assert bar() == 'bar'