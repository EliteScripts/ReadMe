import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GdkPixbuf
import os
import subprocess

# Vérification si le dossier "Documents/Scripts" existe, sinon le créer
if not os.path.exists(os.path.expanduser("~/Documents/Scripts")):
    os.makedirs(os.path.expanduser("~/Documents/Scripts"))

# Création de la fenêtre principale
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Scripts Manager for Phosh", default_width=720, default_height=1440)
        self.set_position(Gtk.WindowPosition.CENTER)
        
	        # Création d'un bouton dans la barre de titre
        self.set_decorated(True)
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Scripts Manager for Phosh")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        # Création d'un TreeView pour afficher les scripts
        self.store = Gtk.ListStore(str, bool)
        self.treeview = Gtk.TreeView(model=self.store)
        self.treeview.set_headers_visible(False)
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_toggle_cell)
        column_toggle = Gtk.TreeViewColumn("", renderer_toggle, active=1)
        self.treeview.append_column(column_toggle)
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("", renderer_text, text=0)
        self.treeview.append_column(column_text)
        self.fill_store()
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(self.treeview)
        self.add(scrolled_window)
        
        # Création d'un bouton pour exécuter les scripts sélectionnés
        icon = Gio.ThemedIcon(name="system-run-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.button = Gtk.Button()
        self.button.add(image)
        self.button.connect("clicked", self.on_button_clicked)
        headerbar.pack_end(self.button)

        self.show_all()

    # Fonction pour remplir le ListStore avec les noms des fichiers dans le dossier "Documents/Scripts"
    def fill_store(self):
        path = os.path.expanduser("~/Documents/Scripts")
        for file in os.listdir(path):
            if file.endswith(".sh"):
                self.store.append([file, False])

    # Fonction appelée lorsqu'une case à cocher est activée/désactivée
    def on_toggle_cell(self, widget, path):
        self.store[path][1] = not self.store[path][1]

    # Fonction appelée lorsqu'on clique sur le bouton "Exécuter les scripts"
    def on_button_clicked(self, widget):
        for row in self.store:
            if row[1]:
                path = os.path.expanduser("~/Documents/Scripts/" + row[0])
                subprocess.Popen(["/bin/sh", path])

# Lancement de la fenêtre
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
