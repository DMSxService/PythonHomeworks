import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усейн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        arv = list(cls.all_results.values())
        for i in range(len(arv)):
            print(arv[i])

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


if __name__ == '__main__':
    unittest.main()
