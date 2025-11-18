#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author: Paolo De Stefani
# Contact: paolo <at> paolodestefani <dot> it
# Copyright (C) 2026 Paolo De Stefani
# License: GPL v3

# This file is part of pySagra.
#
# pySagra is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pySagra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pySagra.  If not, see <http://www.gnu.org/licenses/>.

"""Database exceptions

"""

# Exceptions hierarchy
#
# PyAppDatabaseException
#   -> PyAppDBError
#      -> PyAppDBConnectionError
#      -> PyAppDBFunctionError
#   -> PyAppDBWarning
#   -> PyAppDBInfo


class PyAppDatabaseException(Exception):
    "Base exception class"


class PyAppDBConnectionError(PyAppDatabaseException):
    "Errors on connectiong to database server"


class PyAppDBError(PyAppDatabaseException):
    "Error on interacting with database server"

    def __init__(self, code=None, message=None):
        super().__init__(code, message)
        self.code = code
        self.message = message


class PyAppDBConcurrencyError(PyAppDBError):
    "Error on row modified before update/delete"

    def __init__(self):
        super().__init__(0, 'Row modified before update/delete')
