#!/usr/bin/env python
import unittest

TEST_MODULES = [
    'test.http_test',
]

def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    import tornado.testing
    tornado.testing.main()
