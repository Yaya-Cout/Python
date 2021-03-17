"""Graphical interface for chat module."""
import getpass
import os

import gi
import requests

# import text

gi.require_version("Gtk", "3.0")
import gi.repository.Gtk as Gtk

HOSTNAME = os.uname()[1]
# HOSTNAME = "Mercenaire"
USER = getpass.getuser()
MSGICON = "system-search-symbolic"


class SearchDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(
            self,
            title="Search",
            transient_for=parent,
            modal=True,
        )
        self.add_buttons(
            Gtk.STOCK_FIND,
            Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
        )

        box = self.get_content_area()

        label = Gtk.Label(label="Insert text you want to search for:")
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()


def send(self, data=None):
    """Send message to server."""
    # print(notifies_combo.get_active())
    # notifiyid = notifies_combo.get_active()
    notifyid = 1
    if notifyid == -1:
        dialog = Gtk.MessageDialog(
            transient_for=win,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="Veuilez selectioner un destinataire",
        )
        dialog.format_secondary_text("Pas de destinataire séléctioné")
        dialog.run()
    elif msg.get_text() == "":
        dialog = Gtk.MessageDialog(
            transient_for=win,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="Veuilez entrer un message",
        )
        dialog.format_secondary_text("Le message est vide")
        dialog.connect("destroy", dialog.destroy())
        dialog.run()
    else:
        data = {
            "user": USER,
            "sendhost": HOSTNAME + ".local",
            "notifyhost": notifies_adress[notifyid],
            "msg": msg.get_text(),
        }
        # resp = requests.post("http://ipv6.yann.n1n1.xyz:18523", data=data)
        resp = requests.post("http://Imbatable.local:18523", data=data)
        if resp.content == "SPAM".encode("UTF-8"):
            dialog = Gtk.MessageDialog(
                transient_for=win,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text="SPAM détecté",
            )
            dialog.format_secondary_text("Un SPAM à été détecté")
            dialog.connect("destroy", dialog.destroy())
            dialog.run()
            print("SPAM")
        else:
            print(resp.content)
            print("Send")


msg = Gtk.Entry()
msg2 = Gtk.TextView()
msg.set_text("Coucou")
msg.grab_focus()

win = Gtk.Window(title="Chat")
win.set_icon_from_file("chat.gif")
win.set_hexpand(True)
win.set_vexpand(True)
win.set_size_request(200, 100)

label = Gtk.Label(label="Message :")

msg.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, MSGICON)

notifies = [
    "Mercenaire",
    "Imbatable",
    "Matrix",
]
notifies_adress = [
    "[2a01:e0a:169:7510:4b74:f188:e475:a254]",
    "[2a01:e0a:169:7510:68f9:2a4b:91f5:e387]",
    "Matrix.local",
]

notifies_store = Gtk.ListStore(str)
for notifiy in notifies:
    notifies_store.append([notifiy])

language_filter = notifies_store.filter_new()

notifies_combo = Gtk.TreeView(model=language_filter)
for i, column_title in enumerate(["Destinataire"]):
    renderer = Gtk.CellRendererText()
    column = Gtk.TreeViewColumn(column_title, renderer, text=i)
    notifies_combo.append_column(column)


def on_notifies_selection_changed(selection):
    model, treeiter = selection.get_selected()
    if treeiter is not None:
        print("You selected", model[treeiter][0])


select = notifies_combo.get_selection()
select.connect("changed", on_notifies_selection_changed)

notifies_win = Gtk.ScrolledWindow()
notifies_win.set_vexpand(True)
notifies_win.set_hexpand(True)
notifies_win.add(notifies_combo)

# notifies_combo = Gtk.ComboBox.new_with_model(notifies_store)
# renderer_text = Gtk.CellRendererText()
# notifies_combo.pack_start(renderer_text, True)
# notifies_combo.add_attribute(renderer_text, "text", 0)

sendbutton = Gtk.Button(label="Envoyer")
sendbutton.connect("clicked", send)
# contener = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
# contenerleft = Gtk.Box(homogeneous=Gtk.Orientation.HORIZONTAL, spacing=6)
# contenerigth = Gtk.Box(homogeneous=Gtk.Orientation.HORIZONTAL, spacing=6)
grid = Gtk.Grid()
grid.attach(notifies_win, 0, 0, 1, 7)
# grid.attach(scrollable_treelist, 0, 0, 2, 1)
grid.attach(label, 1, 0, 2, 1)
grid.attach_next_to(msg, label, Gtk.PositionType.BOTTOM, 1, 2)
grid.attach_next_to(msg2, msg, Gtk.PositionType.BOTTOM, 3, 2)
grid.attach_next_to(sendbutton, msg2, Gtk.PositionType.BOTTOM, 1, 2)
win.add(grid)

# Position (1;2), prend 3 de large et 1 de haut
# grid.attach(button, 1, 2, 3, 1)


# contener.pack_start(notifies_combo, False, False, True)
# contener.pack_start(label, True, True, 0)
# contener.pack_start(msg, True, True, 0)
# contener.pack_start(msg2, True, True, 0)
# contener.pack_start(sendbutton, True, True, 0)
# win.add(contener)

win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

print(msg.get_text())
