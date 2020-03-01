import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def towdata_delete():  # noqa: E501
    """Deletes the current prediction data

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def towdata_get():  # noqa: E501
    """returns the prediction for the current dataset

    it will return the predicition for the fibonacci series from 1 to N, (the N should be configurable, but for next iterations. Window size should be configurable) # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def towdata_post(body):  # noqa: E501
    """uploads data to train and predict over

    The body should be in .csv format so the server can read it # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def towdata_put(body):  # noqa: E501
    """Uploads live data to the server for predicition

    The data should be in a csv format # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
