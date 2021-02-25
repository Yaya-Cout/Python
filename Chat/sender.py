import gi
import getpass
import requests
import os

gi.require_version("Gtk", "3.0")
import gi.repository.Gtk as Gtk


hostname = os.uname()[1]
hostname = "Mercenaire"
user = getpass.getuser()


def send(self, data=None):
    print(msg.get_text())
    print(notifies_combo.get_active())
    if notifies_combo.get_active() == -1:
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
        dialog.run()
    else:
        data = {
            "user": user,
            "sendhost": hostname + ".local",
            "notifyhost": notifies_adress[notifies_combo.get_active()],
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
            dialog.connect("destroy", dialog.exit())
            dialog.run()
            print("SPAM")
        else:
            print(resp.content)
            print("Send")

    # curl "http://Imbatable.local:18523/?user=neo&sendhost=Imbatable.local&notifieshost=Imbatable.local&msg=Coucou"


msg = Gtk.Entry()
msg2 = Gtk.TextView()
msg.set_text("Coucou")
msg.grab_focus()

win = Gtk.Window(title="Chat")
win.set_hexpand(True)
win.set_vexpand(True)
win.set_size_request(200, 100)

label = Gtk.Label(label="Message :")


msg.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "system-search-symbolic")

notifies_store = Gtk.ListStore(str)
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
for notifiy in notifies:
    notifies_store.append([notifiy])

notifies_combo = Gtk.ComboBox.new_with_model(notifies_store)
renderer_text = Gtk.CellRendererText()
notifies_combo.pack_start(renderer_text, True)
notifies_combo.add_attribute(renderer_text, "text", 0)

sendbutton = Gtk.Button(label="Envoyer")
sendbutton.connect("clicked", send)
contener = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)


contener.pack_start(notifies_combo, False, False, True)
contener.pack_start(label, True, True, 0)
contener.pack_start(msg, True, True, 0)
contener.pack_start(msg2, True, True, 0)
contener.pack_start(sendbutton, True, True, 0)
win.add(contener)

win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

print(msg.get_text())
