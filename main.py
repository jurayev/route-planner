import unittest
from tests import system_tests, unit_tests
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(" Test Log")


def unit_suite():
    logger.info("---------RUNNING UNIT TESTS--------------")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(unit_tests.UnitTests)
    return suite


def smoke_suite():
    logger.info("---------RUNNING SMOKE TESTS--------------")
    Test = system_tests.SystemTests
    suite = unittest.TestSuite()
    suite.addTest(Test('test_plan_short_path'))
    return suite


def system_suite():
    logger.info("---------RUNNING SYSTEM TESTS--------------")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(system_tests.SystemTests)
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unit_suite())
    runner.run(smoke_suite())
    runner.run(system_suite())

