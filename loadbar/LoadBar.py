import math

class LoadBar:
    """

    """

    def __init__(self, max=100, size=10):
        """

        :param max: int: Max value of the load
        """
        self.i = 0
        self.max = max
        self.size = size

    def start(self):
        """

        :return:
        """
        self._print('[')

    def update(self, to_add=1):
        """

        :param to_add:
        :return:
        """
        self.i += to_add

        done = int(min(self.i, self.max) * self.size // self.max)
        todo = self.size - done
        self._print(
            f'[{"." * done}{" " * todo}]'
        )

    def end(self):
        self._print(f'[{"." * self.size}]', end='\n')

    def _print(self, to_print, end='', flush=True):
        """
        Rewrite print function with default args
        :param to_print:
        :param end:
        :param flush:
        :return:
        """
        # \r used to put the cursor at the beginning of the line
        print(f'\r{to_print}', end=end, flush=flush)
