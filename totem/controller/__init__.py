from ui import window
from .config import ConfigController
from .detector import DetectorController
from .loading import LoadingController
from .password import PasswordController

config = ConfigController(window)
config.load()

loading = LoadingController(window, config)

detector = DetectorController(window, config)
password = PasswordController(window, config)
