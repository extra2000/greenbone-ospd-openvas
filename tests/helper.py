# -*- coding: utf-8 -*-
# Copyright (C) 2014-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from unittest.mock import Mock


def assert_called_once(mock: Mock):
    if hasattr(mock, 'assert_called_once'):
        return mock.assert_called_once()

    if not mock.call_count == 1:
        # pylint: disable=protected-access
        msg = (
            f"Expected '{mock._mock_name or 'mock'}' to have "
            f"been called once. Called {mock.call_count} "
            f"times.{mock._calls_repr()}"
        )
        raise AssertionError(msg)


def assert_called(mock: Mock):
    """assert that the mock was called at least once"""
    if mock.call_count == 0:
        # pylint: disable=protected-access
        msg = f"Expected '{mock._mock_name or 'mock'}' to have been called."
        raise AssertionError(msg)
