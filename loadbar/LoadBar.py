import math
import time
import datetime


class LoadBar:
    """

    """

    def __init__(self, max=100, size=20, head='.', body='.', border_left='[', border_right=']', show_step=True,
                 show_percentage=True, show_eta=True, title=None, show_total_time=True, show_time=False):
        """

        :param max: int: Max value of the load
        """
        self.loading = False
        self.max = max
        self.size = size
        self.head = head
        self.body = body
        self.border_left = border_left
        self.border_right = border_right
        self.show_step = show_step
        self.show_percentage = show_percentage
        # ----- ETA -----
        self.show_eta = show_eta
        self.eta = None
        self.eta_last_i_t = None
        self.start_time = None
        self.stop_time = None
        self.show_time = show_time
        self.show_total_time = show_total_time or show_eta or show_time
        # ----- End ETA -----
        self.title = title


        self._i = 0  # State of the progress

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, i):
        if self.use_time:
            # Do some work to see how long it is gonna last
            if self.eta_last_i_t is not None:
                if self.eta_last_i_t[0] > i:
                    # Don't want to go backward
                    self.eta = None
                    self.eta_last_i_t = None
                elif self.eta_last_i_t[0] < i:
                    # Do nothing if this is the same
                    t = time.time()
                    eta = (t - self.eta_last_i_t[1]) * self.max / (i - self.eta_last_i_t[0])
                    self.eta = eta if self.eta is None else 0.5 * eta + 0.5 * self.eta
                    self.eta_last_i_t = (i, t)
            else:
                # First iteration, I have to set up for the next one
                self.eta_last_i_t = (i, time.time())

        self._i = i

    @property
    def use_time(self):
        return self.show_eta or self.show_total_time

    def start(self, end=''):
        """

        :return:
        """
        self.loading = True
        if self.use_time:
            self.start_time = time.time()
        self.update(step=0, end=end)

    def update(self, step=None, to_add=None, end='', start='\r'):
        """

        :param start:
        :param end:
        :param step:
        :param to_add:
        :return:
        """
        if step is None:
            to_add = 1 if to_add is None else to_add
            self.i = self.i + to_add
        else:
            self.i = step
        l = list()
        if self.title is not None: l.append(self.title)
        if self.show_step: l.append(self._get_step())
        if self.show_percentage: l.append(self._get_percentage())
        l.append(self._get_bar())
        if self.show_time or (self.show_total_time and not self.loading): l.append(self._get_time())
        if self.show_eta and self.loading: l.append(self._get_eta())
        s = ' '.join(l)
        self._print(s, end=end, start=start)

    def end(self):
        self.loading = False
        if self.use_time:
            self.stop_time = time.time()
        self.update(step=self.max, end='\n')

    def _print(self, to_print, end='', flush=True, start='\r'):
        """
        Rewrite print function with default args
        :param to_print:
        :param end:
        :param flush:
        :param start
        :return:
        """
        # \r used to put the cursor at the beginning of the line
        print(f'{start}{to_print}', end=end, flush=flush)

    def _get_bar(self):
        done = int(min(self.i, self.max) * self.size // self.max)
        todo = self.size - done

        todo_head = min(todo, 1)  # 1 or 0
        todo_blank = todo - todo_head
        return f'{self.border_left}{self.body * done}{self.head * todo_head}{" " * todo_blank}{self.border_right}'

    def _get_step(self):
        if not self.show_step:
            return ''
        digit_nb = int(1 + math.floor(math.log10(self.max)))
        return '{0:{1}}'.format(self.i, digit_nb) + f'/{self.max}'

    def _get_percentage(self):
        if not self.show_percentage:
            return ''
        percentage = self.i * 100 / self.max
        percentage_string = f'{percentage:3.0f}%'
        if self.show_step:
            percentage_string = f'({percentage_string})'
        return percentage_string

    def _get_time(self):
        if self.loading:
            if not self.show_time:
                return ''
            else:
                current_time = time.time() - self.start_time
                current_time = datetime.timedelta(seconds=int(current_time))
                return f'Time {current_time}'
        else:
            if not self.show_total_time:
                return ''
            if self.start_time is not None and self.stop_time is not None:
                total_time = int(self.stop_time - self.start_time)
                total_time = datetime.timedelta(seconds=total_time)
                return f'Time {total_time}'

    def _get_eta(self):
        eta = '-:--:--'     # if self.eta is None
        if self.loading:
            if not self.show_eta:
                return ''
            if self.eta is not None:
                eta = self.eta * (self.max - self.i) / self.max
                eta = datetime.timedelta(seconds=int(eta))
            return f'ETA {eta}'
        else:
            return ''

