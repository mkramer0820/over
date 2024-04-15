import wx
import os
from functs import write_excel,test

wildcard = "All files (*.*)|*.*"


class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Over Under')
        self.currentDirectory = os.getcwd()

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        ie_box = wx.StaticBox(self.panel, -1, 'Please select the input file')
        ie_sizer = wx.StaticBoxSizer(ie_box, wx.VERTICAL)

        fl_box = wx.BoxSizer(wx.HORIZONTAL)
        self.fl_ctrl = wx.FilePickerCtrl(self.panel, message="Choose a file")
        fl_box.Add(self.fl_ctrl, 1, wx.ALL | wx.CENTER | wx.EXPAND, 5)
        ie_sizer.Add(fl_box, 1, wx.ALL | wx.CENTER | wx.EXPAND, 10)
        self.fl_ctrl.Bind(wx.EVT_FILEPICKER_CHANGED, self.on_open_file)        

        ie_box1 = wx.StaticBox(self.panel, -1, 'RUN')
        ie_sizer1 = wx.StaticBoxSizer(ie_box1, wx.VERTICAL)
        run_btn = wx.Button(self.panel, -1, "Run")
        run_btn.Bind(wx.EVT_BUTTON, self.on_run)

        vbox.Add(ie_sizer, 0, wx.ALL | wx.CENTER | wx.EXPAND, 5)
        vbox.Add(ie_sizer1, 0, wx.ALL | wx.CENTER | wx.EXPAND, 5)
        vbox.Add(run_btn, 0, wx.ALL | wx.CENTER | wx.EXPAND, 5)


        self.panel.SetSizer(vbox)
        self.Center()
        self.panel.Fit()
        self.Show()

        self.f = None
        
    

    def on_open_file(self, event):
        p = self.fl_ctrl.GetPath()
        self.f = p
        return self.f

    def on_run(self, event):
        print('running, on file opne')
        path = self.f
        f = open("log.txt", "a")
        f.write("on run, \n")
        f.close()
        write_excel(path)


        #write_excel(start_date+'-'+end_date+'.xlsx', self.f)
        


if __name__ == '__main__':
    app = wx.App()
    frame = MainWindow()
    app.MainLoop()