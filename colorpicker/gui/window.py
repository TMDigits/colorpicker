import os.path as osp

import wx
from pynput import keyboard, mouse

from colorpicker.core._defs import BG_COLOR, FG_COLOR
from colorpicker.gui.systray import CustomTaskBarIcon
from colorpicker.gui.panel import ColorDisplay, ColorInfos
from colorpicker.core.mouse import Picker


fp = osp.dirname(osp.realpath(__file__))


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        wx.Frame.__init__(self, None, title="Colorpicker",
                          style=wx.DEFAULT_FRAME_STYLE
                          & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
                          & wx.NO_BORDER)
        self.SetIcon(wx.Icon(osp.join(fp, '..', 'core', 'assets', 'icon.ico')))

        # stylize the frame
        self.set_position()
        self.SetBackgroundColour(wx.Colour(*BG_COLOR))
        self.SetForegroundColour(wx.Colour(*FG_COLOR))

        # create the components
        self.panel = wx.Panel(self)
        self.panel_left = ColorDisplay(self.panel, self.draw_color)
        self.panel_right = ColorInfos(self.panel, self.clip_rgb, self.clip_hex)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.panel_left, 1, wx.EXPAND)
        sizer.Add(self.panel_right, 2, wx.EXPAND)
        self.panel.SetSizer(sizer)
        self.panel.SetSize((self.app_w, self.app_h))

        # add taskbar icon
        self.tbIcon = CustomTaskBarIcon(self)
        self.Bind(wx.EVT_ICONIZE, self.minimize_frame)
        self.Bind(wx.EVT_CLOSE, self.close_frame)

        # add input listeners
        self.picker = Picker()
        self.picked = (0, 0, 0)
        self.keys_listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+c': self.pop_tray,
            '<ctrl>+<alt>+p': self.toggle_picking
        })
        self.mouse_listener = None

        # start listeners
        self.keys_listener.start()
        self.toggle_picking()

        # show frame
        self.Show()
        self.Raise()

    def pop_tray(self):
        if self.IsShownOnScreen():
            self.Hide()
        else:
            self.maximize_frame()

    def set_position(self):
        scr_w, scr_h = wx.GetDisplaySize()
        self.app_w, self.app_h = (scr_w*0.175, scr_h*0.1)
        self.SetSize((self.app_w, self.app_h))
        self.SetPosition((scr_w*0.8, scr_h*0.85))

    def toggle_picking(self, *args, **kwargs):
        if self.mouse_listener is not None:
            self.mouse_listener.stop()
            self.mouse_listener = None
        else:
            self.mouse_listener = mouse.Listener(on_move=self.update_rgb)
            self.mouse_listener.start()

    def clip_rgb(self, *args, **kwargs):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(str(self.picked)))
            wx.TheClipboard.Close()

    def clip_hex(self, *args, **kwargs):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(
                wx.TextDataObject(self.rgb2hex(*self.picked)))
            wx.TheClipboard.Close()

    def rgb2hex(self, r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def update_rgb(self, *args, **kwargs):
        self.picked = self.picker.get_color()
        self.panel_right.rgb_disp.SetLabel(str(self.picked))
        self.panel_right.hex_disp.SetLabel(self.rgb2hex(*self.picked))
        self.panel_left.Refresh()

    def draw_color(self, *args, **kwargs):
        self.dc = wx.PaintDC(self.panel_left)
        self.dc.SetBrush(wx.Brush(wx.Colour(*self.picked)))
        self.dc.SetPen(wx.Pen("WHITE", 1))
        self.dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        self.dc.Clear()
        w, h = self.panel_left.GetSize()
        self.dc.DrawEllipse(0.05*w, 0.05*h, 0.9*w, 0.9*h)

    def close_frame(self, event):
        """
        Destroy the taskbar icon and the frame
        """
        self.keys_listener.stop()
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

    def minimize_frame(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        if self.IsIconized():
            self.Hide()

    def maximize_frame(self):
        """
        Show the frame
        """
        self.Show()
        self.Restore()
        self.Raise()
        self.SetFocus()
