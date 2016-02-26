from pfrock.core.register import PfrockPluginRegister
from pfrock_static_plugin.index import PfrockStaticPlugin

__version__ = '0.2.1.dev5'

PfrockPluginRegister.register(PfrockStaticPlugin)
