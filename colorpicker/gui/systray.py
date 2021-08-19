import os.path as osp

import wx
from wx.adv import TaskBarIcon, EVT_TASKBAR_LEFT_DOWN, EVT_TASKBAR_RIGHT_DOWN

fp = osp.dirname(osp.realpath(__file__))


class CustomTaskBarIcon(TaskBarIcon):
    """"""

    def __init__(self, frame):
        TaskBarIcon.__init__(self)
        self.frame = frame
        icon_fp = osp.join(fp, '..', 'core', 'assets', 'icon.png')
        img = wx.Image(icon_fp, wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)

        self.SetIcon(self.icon, "Colorpicker")
        self.Bind(EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
        self.Bind(EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)

    def OnTaskBarRightClick(self, evt):
        """"""
        self.frame.Hide()

    def OnTaskBarLeftClick(self, evt):
        """
        """
        self.frame.Show()
        self.frame.Restore()
        self.frame.Raise()
