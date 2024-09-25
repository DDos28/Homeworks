import unittest
import HumanRun as hr


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.Useyn = hr.Runner('Усэйн', 10)
        self.Andrey = hr.Runner('Андрей', 9)
        self.Nik = hr.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            print(value)

    def test_run_1(self):
       useyn_nik = hr.Tournament(90, self.Useyn, self.Nik)
       results = useyn_nik.start()
       sprint = ''
       for key, value in results.items():
           sprint += str(key) + ': ' + str(value) + ' '
       all_results['1'] = sprint

       self.assertTrue(results[2] == 'Ник', 'Неверное имя последнего бегуна в забеге 1')

    def test_run_2(self):
        andrey_nik = hr.Tournament(90, self.Andrey, self.Nik)
        results = andrey_nik.start()
        sprint = ''
        for key, value in results.items():
            sprint += str(key) + ': ' + str(value) + ' '
        all_results['2'] = sprint
        self.assertTrue(results[2] == 'Ник', 'Неверное имя последнего бегуна в забеге 2')

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
