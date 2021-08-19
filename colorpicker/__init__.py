import wx

from colorpicker.gui.window import MainFrame

def create_window():
    """"""
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
