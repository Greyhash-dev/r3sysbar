from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from mqtt import r3_mqtt
from functools import partial

r3 = r3_mqtt()

def add_entries(entries, menu, actions):
    for entry in entries:
        action = QAction(entry[0])
        menu.addAction(action)
        action.triggered.connect(entry[1])
        actions.append(action)

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon('r3.png')
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.activated.connect(r3.panic)
tray.setVisible(True)

# Level 1 Menu
menu = QMenu()
entries = [("Exit", app.quit)]

# Add Submenu #1 Light
light = menu.addMenu("Light")
# Add Submenu #1.1
basiclight = light.addMenu("Basic Lights")


actions = []
add_entries(entries, menu, actions)


# Light Menu
entries = [("All Basic Light ON", r3.all_basic_lights_on), ("All Basic Light OFF", r3.all_basic_lights_off)]
add_entries(entries, light, actions)

entries = [("Basic Light 1", partial(r3.switch_basic, 1)), ("Basic Light 2", partial(r3.switch_basic, 2)), ("Basic Light 3", partial(r3.switch_basic, 3)), ("Basic Light 4", partial(r3.switch_basic, 4)), ("Basic Light 5", partial(r3.switch_basic, 5)), ("Basic Light 6", partial(r3.switch_basic, 6))]
add_entries(entries, basiclight, actions)
tray.setContextMenu(menu)


app.exec()
