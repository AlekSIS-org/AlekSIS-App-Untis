import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("BiscuIT-App-Untis").version
except Exception:
    __version__ = "unknown"

default_app_config = "biscuit.apps.untis.apps.UntisConfig"
