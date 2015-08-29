#!/usr/bin/python2

##TODO: implement progress-bar
## implement playlist
## drag and drop

##Deepak Verma

from multiprocessing import Process
import wx
import pyglet
import easygui
ID_OPEN= 101
ID_EXIT= 110
path=""




class arkro(wx.Frame):

    def play_music(self):
        music = pyglet.media.load(path)
        music.play()
        pyglet.app.run()
        return True

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame aka window',size=(180,100))
        panel = wx.Panel(self)
        self.CreateStatusBar()
        #Create Play and Stop Buttons
        buttonStop = wx.Button(panel,label="Stop",pos=(60,10),size=(60,40))
        buttonPlay = wx.Button(panel,label="Play",pos=(00,10),size=(60,40))
        buttonOpen = wx.Button(panel,label="Open",pos=(120,10),size=(60,40))
        #Bind the buttons to their respective event handlers
        self.Bind(wx.EVT_BUTTON, self.playbutton, buttonPlay)
        self.Bind(wx.EVT_BUTTON, self.onStop, buttonStop)
        self.Bind(wx.EVT_BUTTON, self.onOpen, buttonOpen)
        self.Bind(wx.EVT_CLOSE,self.closewindow)
        #Set up the menu
        filemenu = wx.Menu()
        filemenu.Append(ID_OPEN,"&Open","Open a mp3 file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT,"E&xit","Terminate the app")
        #Creating the MenuBar
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File")
        self.SetMenuBar(menubar)
        self.Show(True)
        #Setting the menu event handlers
        wx.EVT_MENU(self,ID_OPEN,self.onOpen)
        wx.EVT_MENU(self,ID_EXIT,self.onExit)
        self.the_player = Process(target=self.play_music)

    def onOpen(self,event):
        global path
        path=easygui.fileopenbox(filetypes="*.mp3")
        self.the_player = Process(target=self.play_music)
        self.the_player.start()
        print path

    def playbutton(self,event):
        if self.the_player.is_alive():
            self.the_player.terminate()

        print "Starting new process"
        self.the_player = Process(target=self.play_music)
        self.the_player.start()

        return True

    def onStop(self,event):
        print "Stopping..........."
        if self.the_player.is_alive():
            self.the_player.terminate()

    def onPause(self,event):
        "implement pause feature"

    def onExit(self,event):
        self.the_player.terminate()
        self.Close(True)

    def closewindow(self,event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = arkro(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
