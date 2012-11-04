# (void)walker unit tests
# Copyright (C) 2012 David Holm <dholmster@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

import tests.interface
import tests.platform
import tests.target
import tests.types
import tests.ui


def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTests(loader.loadTestsFromModule(tests.interface))
    test_suite.addTests(loader.loadTestsFromModule(tests.platform))
    test_suite.addTests(loader.loadTestsFromModule(tests.target))
    test_suite.addTests(loader.loadTestsFromModule(tests.types))
    test_suite.addTests(loader.loadTestsFromModule(tests.ui))
    return test_suite
