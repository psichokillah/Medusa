# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import, unicode_literals

from pprint import pformat

from six import iteritems


class SeriesImageQueryResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SeriesImageQueryResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'key_type': 'text_type',
            'sub_key': 'text_type',
            'file_name': 'text_type',
            'language_id': 'int',
            'resolution': 'text_type',
            'ratings_info': 'int',
            'thumbnail': 'text_type'
        }

        self.attribute_map = {
            'id': 'id',
            'key_type': 'keyType',
            'sub_key': 'subKey',
            'file_name': 'fileName',
            'language_id': 'languageId',
            'resolution': 'resolution',
            'ratings_info': 'ratingsInfo',
            'thumbnail': 'thumbnail'
        }

        self._id = None
        self._key_type = None
        self._sub_key = None
        self._file_name = None
        self._language_id = None
        self._resolution = None
        self._ratings_info = None
        self._thumbnail = None

    @property
    def id(self):
        """
        Gets the id of this SeriesImageQueryResult.


        :return: The id of this SeriesImageQueryResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SeriesImageQueryResult.


        :param id: The id of this SeriesImageQueryResult.
        :type: int
        """
        self._id = id

    @property
    def key_type(self):
        """
        Gets the key_type of this SeriesImageQueryResult.


        :return: The key_type of this SeriesImageQueryResult.
        :rtype: text_type
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this SeriesImageQueryResult.


        :param key_type: The key_type of this SeriesImageQueryResult.
        :type: text_type
        """
        self._key_type = key_type

    @property
    def sub_key(self):
        """
        Gets the sub_key of this SeriesImageQueryResult.


        :return: The sub_key of this SeriesImageQueryResult.
        :rtype: text_type
        """
        return self._sub_key

    @sub_key.setter
    def sub_key(self, sub_key):
        """
        Sets the sub_key of this SeriesImageQueryResult.


        :param sub_key: The sub_key of this SeriesImageQueryResult.
        :type: text_type
        """
        self._sub_key = sub_key

    @property
    def file_name(self):
        """
        Gets the file_name of this SeriesImageQueryResult.


        :return: The file_name of this SeriesImageQueryResult.
        :rtype: text_type
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this SeriesImageQueryResult.


        :param file_name: The file_name of this SeriesImageQueryResult.
        :type: text_type
        """
        self._file_name = file_name

    @property
    def language_id(self):
        """
        Gets the language_id of this SeriesImageQueryResult.


        :return: The language_id of this SeriesImageQueryResult.
        :rtype: int
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """
        Sets the language_id of this SeriesImageQueryResult.


        :param language_id: The language_id of this SeriesImageQueryResult.
        :type: int
        """
        self._language_id = language_id

    @property
    def resolution(self):
        """
        Gets the resolution of this SeriesImageQueryResult.


        :return: The resolution of this SeriesImageQueryResult.
        :rtype: text_type
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this SeriesImageQueryResult.


        :param resolution: The resolution of this SeriesImageQueryResult.
        :type: text_type
        """
        self._resolution = resolution

    @property
    def ratings_info(self):
        """
        Gets the ratings_info of this SeriesImageQueryResult.
        Average rating for the given record.

        :return: The ratings_info of this SeriesImageQueryResult.
        :rtype: int
        """
        return self._ratings_info

    @ratings_info.setter
    def ratings_info(self, ratings_info):
        """
        Sets the ratings_info of this SeriesImageQueryResult.
        Average rating for the given record.

        :param ratings_info: The ratings_info of this SeriesImageQueryResult.
        :type: int
        """
        self._ratings_info = ratings_info

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this SeriesImageQueryResult.


        :return: The thumbnail of this SeriesImageQueryResult.
        :rtype: text_type
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this SeriesImageQueryResult.


        :param thumbnail: The thumbnail of this SeriesImageQueryResult.
        :type: text_type
        """
        self._thumbnail = thumbnail

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
