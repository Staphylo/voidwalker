# (void)walker unit test backend
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

from ...framework.interface import BooleanParameter
from ...framework.interface import Command
from ...framework.interface import CommandFactory
from ...framework.interface import DataCommand
from ...framework.interface import EnumParameter
from ...framework.interface import Parameter
from ...framework.interface import ParameterFactory

from .target import TestInferior
from .target import TestThread


class TestCommandFactory(CommandFactory, object):
    def create(self, command_type, inferior_repository, platform_factory,
               inferior_factory, thread_factory, config, terminal):
        if issubclass(command_type, DataCommand):
            class TestDataCommand(command_type):
                __doc__ = command_type.__doc__

                def __init__(self):
                    command_type.__init__(self)

                def invoke(self, argument, _):
                    inferior = TestInferior()
                    thread = TestThread(inferior.id(), 0)
                    command_type.execute(self, terminal, thread, argument)

            return TestDataCommand()

        if issubclass(command_type, Command):
            class TestCommand(command_type):
                __doc__ = command_type.__doc__

                def __init__(self):
                    command_type.__init__(self)

                def invoke(self, argument, _):
                    command_type.execute(self, terminal, argument)

            return TestCommand()

        else:
            raise TypeError('Command type %s unknown!' %
                            str(command_type))


class TestParameterFactory(ParameterFactory, object):
    def create(self, parameter_type):
        if issubclass(parameter_type, EnumParameter):
            class TestParameterEnum(parameter_type):
                def __init__(self):
                    parameter_type.__init__(self)
                    self.value = parameter_type.default_value(self)

            return TestParameterEnum()

        elif issubclass(parameter_type, BooleanParameter):
            class TestParameterBoolean(parameter_type):
                def __init__(self):
                    parameter_type.__init__(self)
                    self.value = parameter_type.default_value(self)

            return TestParameterBoolean()

        elif issubclass(parameter_type, Parameter):
            class TestParameter(parameter_type):
                def __init__(self):
                    parameter_type.__init__(self)

            return TestParameter()

        else:
            raise TypeError('Parameter type %s unknown!' %
                            str(type(parameter_type)))
