import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t1 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.walk()
        self.assertEqual(t1.distance, 50)

    def test_run(self):
        t1 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.run()
        self.assertEqual(t1.distance, 100)

    def test_challenge(self):
        t1 = runner.Runner("Konstantin")
        t2 = runner.Runner("Konstantin")
        for i in range(0, 10):
            t1.run()
            t2.walk()
        self.assertNotEqual(t1.distance, t2.distance)


if __name__ == '__main__':
    unittest.main()
