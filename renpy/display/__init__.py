# Copyright 2004-2024 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import division, absolute_import, with_statement, print_function, unicode_literals
from renpy.compat import PY2, basestring, bchr, bord, chr, open, pystr, range, round, str, tobytes, unicode # *

from typing import Optional, Any


import renpy
renpy.update_path()

import renpy.log

# The draw object through which all drawing is routed. This object
# contains all of the distinction between the software and GL
# renderers.
draw = None # type: Any|None

# The interface object.
interface = None # type: Optional[renpy.display.core.Interface]

# Should we disable imagedissolve-type transitions?
less_imagedissolve = False

# Are we on a touchscreen?
touch = False

# The pygame.display.Info object, which we want to survive a reload.
info = None

# True if the platform can go fullscreen. (Right now, this is true for
# all platforms.)
can_fullscreen = True

def get_info():
    global info

    if info is None:
        import pygame_sdl2 as pygame
        pygame.display.init()
        info = pygame.display.Info()

    return info

# Logs we use.
log = renpy.log.open("log", developer=False, append=False)
ic_log = renpy.log.open("image_cache", developer=True, append=False)
to_log = renpy.log.open("text_overflow", developer=True, append=True)


# Generated by scripts/relative_imports.py, do not edit below this line.
if 1 == 0:
    from . import accelerator
    from . import anim
    from . import behavior
    from . import controller
    from . import core
    from . import displayable
    from . import dragdrop
    from . import emulator
    from . import error
    from . import focus
    from . import gesture
    from . import im
    from . import image
    from . import imagelike
    from . import imagemap
    from . import joystick
    from . import layout
    from . import matrix
    from . import minigame
    from . import model
    from . import module
    from . import motion
    from . import movetransition
    from . import particle
    from . import pgrender
    from . import predict
    from . import presplash
    from . import quaternion
    from . import render
    from . import scale
    from . import scenelists
    from . import screen
    from . import swdraw
    from . import transform
    from . import transition
    from . import tts
    from . import types
    from . import video
    from . import viewport
