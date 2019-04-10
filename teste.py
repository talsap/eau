import wx
import wx.lib.mixins.listctrl as listmix
from wx.lib.agw import ultimatelistctrl as ULC

APPNAME='Sortable Ultimate List Ctrl'
APPVERSION='1.0'
MAIN_WIDTH=300
MAIN_HEIGHT=300

musicdata = {
0 : ("Bad English", "The Price Of Love"),
1 : ("DNA featuring Suzanne Vega", "Tom's Diner"),
2 : ("George Michael", "Praying For Time"),
3 : ("Gloria Estefan", "Here We Are"),
4 : ("Linda Ronstadt", "Don't Know Much"),
5 : ("Michael Bolton", "How Am I Supposed To Live Without You"),
6 : ("Paul Young", "Oh Girl"),
}

########################################################################
class TestUltimateListCtrlPanel(wx.Panel, listmix.ColumnSorterMixin):

    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS, size=(MAIN_WIDTH,MAIN_HEIGHT))

        self.index = 0

        self.list_ctrl = ULC.UltimateListCtrl(self, -1, agwStyle=ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)
        self.list_ctrl.InsertColumn(0, "Artist")
        self.list_ctrl.InsertColumn(1, "Title", wx.LIST_FORMAT_RIGHT)
        self.list_ctrl.InsertColumn(2, "Download")

        items = musicdata.items()
        index = 0
        for key, data in items:
            pos=self.list_ctrl.InsertStringItem(index, data[0])
            self.list_ctrl.SetStringItem(index, 1, data[1])
            #self.list_ctrl.SetStringItem(index, 2, data[2])
            button = wx.Button(self.list_ctrl, id=key, label="Download")
            self.list_ctrl.SetItemWindow(pos, col=2, wnd=button, expand=True)
            self.list_ctrl.SetItemData(index, key)
            index += 1

        # Now that the list exists we can init the other base class,
        # see wx/lib/mixins/listctrl.py
        self.itemDataMap = musicdata
        listmix.ColumnSorterMixin.__init__(self, 2)
        self.Bind(wx.EVT_LIST_BUTTON_CLICK, lambda event: self.OnColClick(event, key), self.list_ctrl)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)


    def GetListCtrl(self):
        return self.list_ctrl

    #----------------------------------------------------------------------
    def OnColClick(self, event, key):
        print(key)

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'%s v%s' % (APPNAME,APPVERSION),size=(MAIN_WIDTH,MAIN_HEIGHT),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        # Add a panel so it looks the correct on all platforms
        panel = TestUltimateListCtrlPanel(self)

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
