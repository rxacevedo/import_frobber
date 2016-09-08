"""Frob module - frobs things"""


import importlib


def main():
    # Omg modules
    foo_mod = importlib.import_module('foo')
    bar_mod = importlib.import_module('bar')
    baz_mod = importlib.import_module('.baz', package='bar')

    # Omg classes
    foo = foo_mod.Foo()
    bar = bar_mod.Bar()
    baz = baz_mod.Baz()

    # Omg methods
    foo.foo()
    bar.bar()
    baz.baz()


if __name__ == '__main__':
    main()
