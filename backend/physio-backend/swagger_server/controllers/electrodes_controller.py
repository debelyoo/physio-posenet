import connexion
import six

from swagger_server import util


def add_electrode(file):  # noqa: E501
    """Add a new electrode to the library

     # noqa: E501

    :param file: Picture showing the electrode that needs to be added to the library
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def electrodes_get():  # noqa: E501
    """Get all electrodes in the library

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_image_by_electrode_id_and_index(electrodeId, index):  # noqa: E501
    """Find image for an electrode by index

    Returns a single image # noqa: E501

    :param electrodeId: ID of electrode to return
    :type electrodeId: str
    :param index: index of the image
    :type index: int

    :rtype: None
    """
    return 'do some magic!'


def validate_electrodes(electrodeId, file=None):  # noqa: E501
    """Validates electrodes position

    Validates the electrodes (sent in body) against the reference in server # noqa: E501

    :param electrodeId: ID of electrode to validate
    :type electrodeId: str
    :param file: image of the electrode to validate
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'
