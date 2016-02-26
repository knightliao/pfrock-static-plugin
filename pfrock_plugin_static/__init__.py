from pfrock.core.register import PfrockPluginRegister
from pfrock_plugin_static.index import PfrockStaticPlugin

__version__ = '0.2.1.dev4'

PfrockPluginRegister.register(PfrockStaticPlugin)
