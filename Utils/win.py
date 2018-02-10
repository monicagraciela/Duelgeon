#!/usr/bin/env python3

from panda3d.core import WindowProperties, LVector3


def hide_cursor():
    """set the Cursor invisible"""
    props = WindowProperties()
    props.setCursorHidden(True)
    base.win.requestProperties(props)


def show_cursor():
    """set the Cursor visible again"""
    props = WindowProperties()
    props.setCursorHidden(False)
    base.win.requestProperties(props)


def change_resolution(w, h):
    props = WindowProperties()
    props.setSize(w, h)
    base.win.requestProperties(props)


def toggle_fullscreen(_size={'w': 0, 'h': 0}):
    windowed = not base.win.isFullscreen()
    props = WindowProperties(base.win.getProperties())

    if windowed:
        _size['w'] = props.getXSize()
        _size['h'] = props.getYSize()
        props.setSize(base.pipe.getDisplayWidth(), base.pipe.getDisplayHeight())
    else:
        props.setSize(_size['w'], _size['h'])

    props.setFullscreen(windowed)
    base.win.requestProperties(props)
