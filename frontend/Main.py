from PyQt5.QtWidgets import QWidget

from frontend.function.EventListFunction import EventListFunction
from frontend.function.OptionsWindowFunction import OptionsWindowFunction
from frontend.function.StyleFunction import StyleFunction


class Main(OptionsWindowFunction, EventListFunction, StyleFunction):

    def __init__(self):
        super().__init__()