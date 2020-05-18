class LoadBar:
    """

    """

    def __init__(self, max=100, size=20, head='.', body='.'):
        """

        :param max: int: Max value of the load
        """
        self.max = max
        self.size = size
        self.head = head
        self.body = body

        self.i = 0      # State of the progress

    def start(self):
        """

        :return:
        """
        self._print(f'[{" " * self.size}]')

    def update(self, to_add=1):
        """

        :param to_add:
        :return:
        """
        self.i += to_add

        done = int(min(self.i, self.max) * self.size // self.max)
        done_head = min(1, done)        # 0 or 1
        done_body = done - done_head
        todo = self.size - done
        self._print(
            f'[{self.body * done_body}{self.head * done_head}{" " * todo}]'
        )

    def end(self):
        self._print(f'[{self.body * self.size}]', end='\n')

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
