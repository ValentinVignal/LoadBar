class LoadBar:
    """

    """

    def __init__(self, max=100, size=20, head='.', body='.', border_left='[', border_right=']'):
        """

        :param max: int: Max value of the load
        """
        self.max = max
        self.size = size
        self.head = head
        self.body = body
        self.border_left = border_left
        self.border_right = border_right

        self.i = 0      # State of the progress

    def start(self):
        """

        :return:
        """
        self.update(to_add=0)

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
            f'{self.border_left}{self.body * done_body}{self.head * done_head}{" " * todo}{self.border_right}'
        )

    def end(self):
        self._print(f'{self.border_left}{self.body * self.size}{self.border_right}', end='\n')

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
