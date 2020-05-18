from termcolor import colored
import os

from .LoadBar import LoadBar


class ColorBar(LoadBar):
    def __init__(self, *args, color=None, on_color=None, **kwargs):
        """

        :param args:
        :param color: The color of the bar
        :param on_color: The background color of the bar
        :param kwargs:
        """
        super(ColorBar, self).__init__(*args, **kwargs)

        self.color = color
        self.on_color = None if on_color is None else f'on_{on_color}'
    
    def start(self, *args, **kwargs):
        os.system('')
        super(ColorBar, self).start(*args, **kwargs)

    def _print(self, to_print, *args, **kwargs):
        to_print = colored(
            text=str(to_print),
            color=self.color,
            on_color=self.on_color
        )
        super(ColorBar, self)._print(*args, to_print=to_print, **kwargs)


