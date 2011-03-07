from gi.repository import Gtk

from gtweak.gsettings import GSettingsSetting
from gtweak.tweakmodel import Tweak, TweakGroup
from gtweak.widgets import TweakSwitch

class GSettingsSwitchTweak(Tweak):
    def __init__(self, schema_name, key_name):
        settings = GSettingsSetting(schema_name)
        Tweak.__init__(self, settings.get_summary(key_name), settings.get_description(key_name))
        self.widget = TweakSwitch(settings, key_name)

TWEAK_GROUPS = (
        TweakGroup(
            "Nautilus",
            GSettingsSwitchTweak("org.gnome.desktop.background", "show-desktop-icons"),
            GSettingsSwitchTweak("org.gnome.desktop.background", "draw-background")),
)
