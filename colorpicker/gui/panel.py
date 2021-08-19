import os.path as osp

import wx
import wx.lib.platebtn as platebtn

from colorpicker.core._defs import BG_COLOR, FG_COLOR

fp = osp.dirname(osp.realpath(__file__))


class ColorDisplay(wx.Panel):

    def __init__(self, parent, update):
        super().__init__(parent)
        self.Bind(wx.EVT_PAINT, update)


class ColorInfos(wx.Panel):

    def __init__(self, parent, clip_rgb, clip_hex):
        super().__init__(parent)
        self.SetForegroundColour(wx.Colour(*FG_COLOR))

        self.row = wx.BoxSizer(wx.VERTICAL)
        self.rows = [wx.BoxSizer(wx.HORIZONTAL), wx.BoxSizer(wx.HORIZONTAL)]

        self.rgb_disp = wx.StaticText(self, label="", style=wx.ALIGN_LEFT)
        self.hex_disp = wx.StaticText(self, label="", style=wx.ALIGN_LEFT)

        icon_fp = osp.join(fp, '..', 'core', 'assets', 'clip.png')
        img = wx.Image(icon_fp, wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)

        self.clip_rgb_btn = platebtn.PlateButton(self, bmp=bmp)
        self.clip_hex_btn = platebtn.PlateButton(self, bmp=bmp)
        self.clip_rgb_btn.SetBackgroundColour(wx.Colour(*BG_COLOR))
        self.clip_hex_btn.SetBackgroundColour(wx.Colour(*BG_COLOR))
        self.Bind(wx.EVT_BUTTON, clip_rgb, self.clip_rgb_btn)
        self.Bind(wx.EVT_BUTTON, clip_hex, self.clip_hex_btn)

        self.rows[0].AddSpacer(10)
        self.rows[0].Add(self.clip_rgb_btn, 1, wx.ALIGN_CENTER)
        self.rows[0].AddSpacer(10)
        self.rows[0].Add(self.rgb_disp, 1, wx.ALIGN_CENTER)

        self.rows[1].AddSpacer(10)
        self.rows[1].Add(self.clip_hex_btn, 1, wx.ALIGN_CENTER)
        self.rows[1].AddSpacer(10)
        self.rows[1].Add(self.hex_disp, 1, wx.ALIGN_CENTER)

        self.row.Add(self.rows[0], 1, wx.ALIGN_LEFT)
        self.row.Add(self.rows[1], 1, wx.ALIGN_LEFT)

        self.SetSizer(self.row)
