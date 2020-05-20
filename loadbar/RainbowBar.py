import os

from .LoadBar import LoadBar


class ColorShell:
    reset = 0
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37


class RainbowBar(LoadBar):
    rainbow_colors = [
        ColorShell.red,
        ColorShell.yellow,
        ColorShell.green,
        ColorShell.cyan,
        ColorShell.blue,
        ColorShell.magenta
    ]

    def __init__(self, *args, **kwargs):
        super(RainbowBar, self).__init__(*args, **kwargs)

    def start(self, *args, **kwargs):
        os.system('')
        super(RainbowBar, self).start(*args, **kwargs)

    def _to_rainbow(self, string):
        rainbowed_string = ''
        nb_colors = len(RainbowBar.rainbow_colors)
        for i, s in enumerate(string):
            rainbowed_string += f'\033[{RainbowBar.rainbow_colors[i % nb_colors]}m{s}'
        rainbowed_string += '\033[0m'
        return rainbowed_string

    def _print(self, to_print, *args, **kwargs):
        to_print = self._to_rainbow(to_print)
        super(RainbowBar, self)._print(*args, to_print=to_print, **kwargs)
