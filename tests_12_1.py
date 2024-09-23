import unittest
import HumanRun


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = HumanRun.Runner(name='Хотьба')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = HumanRun.Runner(name='Бег')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run_1 = HumanRun.Runner(name='Бег')
        run_2 = HumanRun.Runner(name='Хотьба')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)

if __name__ == '__main__':
    unittest.main()