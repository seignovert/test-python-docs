'''Dummy foo module.'''

def foo(dummy):
    '''Foo function.

    Args:
        dummy (str): Dummy parameter

    Return:
        str: Foo string

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> foo('dummy')
        'foo'

    Note:
        Test note in docstring

    '''
    return 'foo'

def bar():
    '''Bar function.'''
    bar = 'bar'
    return f"{bar}"
