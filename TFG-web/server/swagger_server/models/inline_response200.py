# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nsteps: int=None, value: float=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param nsteps: The nsteps of this InlineResponse200.  # noqa: E501
        :type nsteps: int
        :param value: The value of this InlineResponse200.  # noqa: E501
        :type value: float
        """
        self.swagger_types = {
            'nsteps': int,
            'value': float
        }

        self.attribute_map = {
            'nsteps': 'nsteps',
            'value': 'value'
        }
        self._nsteps = nsteps
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nsteps(self) -> int:
        """Gets the nsteps of this InlineResponse200.


        :return: The nsteps of this InlineResponse200.
        :rtype: int
        """
        return self._nsteps

    @nsteps.setter
    def nsteps(self, nsteps: int):
        """Sets the nsteps of this InlineResponse200.


        :param nsteps: The nsteps of this InlineResponse200.
        :type nsteps: int
        """

        self._nsteps = nsteps

    @property
    def value(self) -> float:
        """Gets the value of this InlineResponse200.


        :return: The value of this InlineResponse200.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this InlineResponse200.


        :param value: The value of this InlineResponse200.
        :type value: float
        """

        self._value = value
