import unittest
from tests_12_3 import RunnerTest, TournamentTest

rts = unittest.TestSuite()

rts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
rts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rts)
