import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        t1 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.walk()
        self.assertEqual(t1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        t1 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.run()
        self.assertEqual(t1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        t1 = runner.Runner("Konstantin")
        t2 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.run()
            t2.walk()
        self.assertNotEqual(t1.distance, t2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усейн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        arv = list(cls.all_results.values())
        for i in range(len(arv)):
            print(arv[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race1(self):
        ar = {}
        race = runner_and_tournament.Tournament(90,
                                                self.runner1,
                                                self.runner3).start()
        for i in range(1, len(race) + 1):
            ar[i] = str(race[i])
        n = len(TournamentTest.all_results)
        TournamentTest.all_results[n] = ar
        self.assertTrue('Ник' == race[len(race)], 'Последним стал не Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race2(self):
        ar = {}
        race = runner_and_tournament.Tournament(90,
                                                self.runner2,
                                                self.runner3).start()
        for i in range(1, len(race) + 1):
            ar[i] = str(race[i])
        n = len(TournamentTest.all_results)
        TournamentTest.all_results[n] = ar
        self.assertTrue('Ник' == race[len(race)], 'Последним стал не Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race3(self):
        ar = {}
        race = runner_and_tournament.Tournament(90,
                                                self.runner1,
                                                self.runner2,
                                                self.runner3).start()
        for i in range(1, len(race) + 1):
            ar[i] = str(race[i])
        n = len(TournamentTest.all_results)
        TournamentTest.all_results[n] = ar
        self.assertTrue('Ник' == race[len(race)], 'Последним стал не Ник')
