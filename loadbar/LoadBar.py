import math


class LoadBar:
    """

    """

    def __init__(self, max=100, size=20, head='.', body='.', border_left='[', border_right=']', show_step=True,
                 show_percentage=True):
        """

        :param max: int: Max value of the load
        """
        self.max = max
        self.size = size
        self.head = head
        self.body = body
        self.border_left = border_left
        self.border_right = border_right
        self.show_step = show_step
        self.show_percentage = show_percentage

        self.i = 0  # State of the progress

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
        l = list()
        if self.show_step: l.append(self.get_step())
        if self.show_percentage: l.append(self.get_percentage())
        l.append(self._get_bar())
        s = ' '.join(l)
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

        todo_head = min(todo, 1)  # 1 or 0
        todo_blank = todo - todo_head
        return f'{self.border_left}{self.body * done}{self.head * todo_head}{" " * todo_blank}{self.border_right}'

    def get_step(self):
        if not self.show_step:
            return ''
        digit_nb = int(1 + math.ceil(math.log10(self.max)))
        return '{0:{1}}'.format(self.i, digit_nb) + f'/{self.max}'

    def get_percentage(self):
        if not self.show_percentage:
            return ''
        percentage = self.i * 100 / self.max
        percentage_string = f'{percentage:3.0f}%'
        if self.show_step:
            percentage_string = f'({percentage_string})'
        return percentage_string

