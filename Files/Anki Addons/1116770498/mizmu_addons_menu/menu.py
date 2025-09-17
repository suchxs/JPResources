"""
updated and upgraded by mizmu addons (c) 2023
Github (https://github.com/hafatsat-anki/Beautify-Anki_2.0)
patreon (https://www.patreon.com/mizmuaddons)
buymeacoffee (https://www.buymeacoffee.com/jhhomshl)
ankiweb (https://ankiweb.net/shared/info/1116770498)
new icons: google fonts
"""

from pathlib import Path

from aqt import gui_hooks, mw, qconnect
from aqt.utils import openLink, showInfo
from aqt import QMenu, QIcon
current_directory = str(Path(__file__).parent.resolve())

def get_anki_version():
    try:
        # 2.1.50+ because of bdd5b27715bb11e4169becee661af2cb3d91a443, https://github.com/ankitects/anki/pull/1451
        from anki.utils import point_version
    except:
        try:
            # introduced with 66714260a3c91c9d955affdc86f10910d330b9dd in 2020-01-19, should be in 2.1.20+
            from anki.utils import pointVersion
        except:
            # <= 2.1.19
            from anki import version as anki_version
            return int(anki_version.split(".")[-1])
        else:
            return pointVersion()
    else:
        return point_version()

anki_21_version = get_anki_version()

# taken from https://github.com/AnKingMed/Study-Timer/commit/c3d89949c6523fd4f51121e2dc2ff0fffab5f202
def getMenu(parent, menuName):
    menubar = parent.form.menubar
    for a in menubar.actions():
        if menuName == a.text():
            return a.parent(), True
    else:
        return menubar.addMenu(menuName), False


def onSetupMenus(*args):
    def add_action(menu: QMenu, text: str, icon, func: callable):
        a = menu.addAction(text)
        if (icon is not None):
            a.setIcon(QIcon(f"{current_directory}/icons/{icon}"))
        qconnect(a.triggered, func)

    mizmu_menu, Already_exists = getMenu(mw, "&mizmu Addons")

    if not Already_exists:

        add_action(mizmu_menu, "my addons", "favicon.ico", lambda: openLink("https://ankiweb.net/shared/byauthor/760817185"))
        add_action(mizmu_menu, "github", "github-mark.png", lambda: openLink("https://github.com/hafatsat-anki"))
        add_action(mizmu_menu, "patreon", "patreon.png", lambda: openLink("https://www.patreon.com/mizmuaddons"))
        add_action(mizmu_menu, "buymeacoffee", "buymeacoffee.png", lambda: openLink("https://www.buymeacoffee.com/jhhomshl"))
        mizmu_menu.addSeparator()

    addon_menu = mizmu_menu.addMenu("Beautify_Anki 2.0")
    add_action(addon_menu, "Rate this addon", "Thumb_Up.png", lambda: openLink("https://ankiweb.net/shared/info/1116770498"))
    add_action(addon_menu, "Additional settings will appear as development continues...", None, lambda: showInfo("will appear soon.."))

gui_hooks.main_window_did_init.append(onSetupMenus)
