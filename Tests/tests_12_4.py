import logging
import rt_with_exceptions


class RunnerTest:

    def test_walk(self):
        try:
            t1 = rt_with_exceptions.Runner('Вася',-5)
            for i in range(0, 10):
                t1.walk()
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')
        return

    def test_run(self):
        try:
            t1 = rt_with_exceptions.Runner(2)
            for i in range(0, 10):
                t1.run()
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
        return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s-%(levelname)s-%(funcName)s:-%(lineno)d-%(message)s')

    RunnerTest.test_walk(None)
    RunnerTest.test_run(None)



