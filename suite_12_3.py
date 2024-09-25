import unittest
import tests_12_3

testS = unittest.TestSuite()
testS.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest)))
testS.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testS)