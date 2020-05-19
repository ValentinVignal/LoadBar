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
        self.update(step=0)

    def update(self, to_add=None, step=None, end=''):
        """

        :param to_add:
        :return:
        """
        if step is None:
            self.i += 1 if to_add is None else to_add
        else:
            self.i = step
        s = ''
        s += self._get_bar()
        self._print(s, end=end)

    def end(self):
        self.update(step=self.max, end='\n')

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

    def _get_bar(self):
        done = int(min(self.i, self.max) * self.size // self.max)
        todo = self.size - done

        todo_head = min(todo, 1)        # 1 or 0
        todo_blank = todo - todo_head
        return f'{self.border_left}{self.body * done}{self.head * todo_head}{" " * todo_blank}{self.border_right}'

