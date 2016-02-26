from pfrock.core.register import PfrockPluginRegister
from pfrock_static_plugin.index import PfrockStaticPlugin

__version__ = '0.2.1.dev6'

PfrockPluginRegister.register(PfrockStaticPlugin)
