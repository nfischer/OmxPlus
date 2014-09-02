#!/usr/bin/python

from gi.repository import Gtk, Gdk
#import cairo
import time
import os

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Omx+")
        self.set_name('MyWindow')
        self.set_size_request(400, 400)
        icon_path = "eduke32.png"
        self.set_icon_from_file(icon_path)

        self.black_window = Gtk.Window(title="Black Window")
        self.black_window.set_name('BlackWindow')

        style_provider = Gtk.CssProvider()
        css = """
#BlackWindow {
    background-color: #000000;
}
"""
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        button2 = Gtk.Button("Full screen")
        button2.connect("clicked", self.on_fullscreen_clicked)
        box.add(button2)

        #button4 = Gtk.Button("Unfull screen")
        #button4.connect("clicked", self.on_unfullscreen_clicked)
        #box.add(button4)

    #def on_unfullscreen_clicked(self, widget):
    #    # Undoes fullscreen
    #    self.unfullscreen()
    #    #self.black_window.show_all()
    #    self.black_window.destroy()

    def on_fullscreen_clicked(self, widget):
        # Goes fullscreen
        self.black_window.fullscreen()
        #self.unfullscreen()

        # set cursor invisible
        cursor = Gdk.Cursor.new(Gdk.CursorType.BLANK_CURSOR)

        # Show window
        self.black_window.show_all()
        self.black_window.get_window().set_cursor(cursor)
        while Gtk.events_pending():
            Gtk.main_iteration()

        # Execute other commands
        time.sleep(5)

        # Cleanup
        self.black_window.destroy()
        #self.unfullscreen()

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            f_name = dialog.get_filename()
            print("File selected: " + f_name)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("AVI files")
        filter_text.add_pattern("*.avi")
        dialog.add_filter(filter_text)

        filter_mp4 = Gtk.FileFilter()
        filter_mp4.set_name("MP4 files")
        filter_text.add_pattern("*.mp4")
        dialog.add_filter(filter_mp4)

        filter_mkv = Gtk.FileFilter()
        filter_mkv.set_name("MKV files")
        filter_text.add_pattern("*.mkv")
        dialog.add_filter(filter_mkv)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)


win = FileChooserWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
