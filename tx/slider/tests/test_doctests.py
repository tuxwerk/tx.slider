#import unittest2 as unittest
import unittest
from Testing.ZopeTestCase import FunctionalDocFileSuite
from tx.slider.tests import BaseFunctionalTest


def test_suite():
    return unittest.TestSuite([
        FunctionalDocFileSuite(
            'browser.txt',
            package='tx.slider',
            test_class=BaseFunctionalTest
        )
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
