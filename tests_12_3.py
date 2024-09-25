import unittest
import HumanRun as hr
import HumanRun1

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        run = HumanRun1.Runner(name='Хотьба')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run = HumanRun1.Runner(name='Бег')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        run_1 = HumanRun1.Runner(name='Бег')
        run_2 = HumanRun1.Runner(name='Хотьба')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.Useyn = hr.Runner('Усэйн', 10)
        self.Andrey = hr.Runner('Андрей', 9)
        self.Nik = hr.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_1(self):
       useyn_nik = hr.Tournament(90, self.Useyn, self.Nik)
       results = useyn_nik.start()
       sprint = ''
       for key, value in results.items():
           sprint += str(key) + ': ' + str(value) + ' '
       all_results['1'] = sprint

       self.assertTrue(results[2] == 'Ник', 'Неверное имя последнего бегуна в забеге 1')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_2(self):
        andrey_nik = hr.Tournament(90, self.Andrey, self.Nik)
        results = andrey_nik.start()
        sprint = ''
        for key, value in results.items():
            sprint += str(key) + ': ' + str(value) + ' '
        all_results['2'] = sprint
        self.assertTrue(results[2] == 'Ник', 'Неверное имя последнего бегуна в забеге 2')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_3(self):
        useyn_andrey_nik = hr.Tournament(90, self.Useyn, self.Andrey, self.Nik)
        results = useyn_andrey_nik.start()
        sprint = ''
        for key, value in results.items():
            sprint += str(key) + ': ' + str(value) + ' '
        all_results['3'] = sprint
        self.assertTrue(results[3] == 'Ник', 'Неверное имя последнего бегуна в забеге 3')

if __name__ == '__main__':
    unittest.main()
