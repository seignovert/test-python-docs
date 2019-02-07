'''Tests foo module.'''

from foo import bar, foo

def test_foo_str():
    '''Test foo string output.'''
    assert foo('dummy') == 'foo'

def test_bar_str():
    '''Test bar string output.'''
    assert bar() == 'bar'
