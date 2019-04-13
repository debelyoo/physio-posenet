import connexion
import six

from swagger_server import util
from flask import send_from_directory
from ..physio_utils import load_config

config = load_config("config.yml")
STATIC_FILE_DIR = config["staticFileDir"]

def front_get(path):  # noqa: E501
    """Get the home page

     # noqa: E501


    :rtype: None
    """
    return send_from_directory(STATIC_FILE_DIR, path)

