#!/usr/bin/python3
"""OpenGL capabilities viewer."""

from kivy.app import App
from kivy.lang import Builder
from kivy.graphics.opengl import *
from kivy.uix.boxlayout import BoxLayout


#Constants
#==============================================================================
__author__ = "Eric Snyder"
__copyright__ = "Copyright (c) 2021 by Eric Snyder"
__license__ = "MIT"
__version__ = "1.0.0"

KVLANG = """
<MainScreen>:
    orientation: "vertical"
    ext_list: ExtList

    Label:
        text: "Extensions:"
        size_hint_y: .1

    TextInput:
        id: ExtList
        text: ""
        readonly: True
"""


#Classes
#==============================================================================
class MainScreen(BoxLayout):
    """The main screen for this app."""
    def __init__(self, **kwargs):
        """Setup this screen."""
        super(MainScreen, self).__init__(**kwargs)
        self.ext_list.text = glGetString(GL_EXTENSIONS).replace(b" ", b"\n")


class KvCaps(App):
    """A basic app class."""
    def build(self):
        """Build the UI for this app."""
        Builder.load_string(KVLANG)
        return MainScreen()


#Entry Point
#==============================================================================
KvCaps().run()
