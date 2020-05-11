class LoadBar:
    """

    """
    def __init__(self, max=100):
        """

        :param max: int: Max value of the load
        """
        self.i = 0
        self.max = max

        self.loading = False

    def start(self):
        """

        :return:
        """
        if not self.loading:
            print('[')
            self.loading = True

    def update(self, to_add=1):
        """

        :param to_add:
        :return:
        """
        self.i += to_add
        print('.' * to_add, end='', flush=True)
        if self.i == self.max:
            self.end()

    def end(self):
        if self.loading:
            print(']')
            self.loading = False




