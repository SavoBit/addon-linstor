# -*- coding: utf-8 -*-
"""
OpenNebula Driver for Linstor
Copyright 2018 LINBIT USA LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import xml.etree.ElementTree as ET


class Image(object):

    """Docstring for vm. """

    def __init__(self, xml):
        self.xmlstr = xml  # type: str
        self._root = ET.fromstring(xml)

    def __str__(self):
        return self.xmlstr

    @property
    def ID(self):
        """Returns name"""
        try:
            return self._root.find("ID").text
        except AttributeError:
            return ""

    @property
    def size(self):
        """Returns name"""
        try:
            return self._root.find("SIZE").text
        except AttributeError:
            return ""

    @property
    def source(self):
        """Returns source"""
        try:
            return self._root.find("SOURCE").text
        except AttributeError:
            return '""'

    @property
    def target_snap(self):
        """Returns target_snap"""
        try:
            return self._root.find("TARGET_SNAPSHOT").text
        except AttributeError:
            return '""'

    @property
    def datastore_ID(self):
        """Returns name"""
        try:
            return self._root.find("DATASTORE_ID").text
        except AttributeError:
            return ""

    @property
    def FS_type(self):
        """Returns FS_type"""
        try:
            return self._root.find("FSTYPE").text
        except AttributeError:
            return ""

    @property
    def path(self):
        """Returns path"""
        try:
            return self._root.find("PATH").text
        except AttributeError:
            return ""

    @property
    def cloning_ID(self):
        """Returns cloning_ID"""
        try:
            return self._root.find("CLONING_ID").text
        except AttributeError:
            return ""

    @property
    def md5(self):
        """Returns md5"""
        try:
            return self._root.find("TEMPLATE").find("MD5").text
        except AttributeError:
            return '""'

    @property
    def sha1(self):
        """Returns sha1"""
        try:
            return self._root.find("TEMPLATE").find("SHA1").text
        except AttributeError:
            return '""'

    @property
    def no_decompress(self):
        """Returns no_decompress"""
        try:
            return self._root.find("TEMPLATE").find("NO_DECOMPRESS").text
        except AttributeError:
            return '""'

    @property
    def limit_transfer_bw(self):
        """Returns limit_transfer_bw"""
        try:
            return self._root.find("TEMPLATE").find("LIMIT_TRANSFER_BW").text
        except AttributeError:
            return '""'
