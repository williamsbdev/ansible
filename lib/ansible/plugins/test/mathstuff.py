# (c) 2016, Ansible, Inc
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

__metaclass__ = type

def issubset(a, b):
    return set(a) <= set(b)

def issuperset(a, b):
    return set(a) >= set(b)

class TestModule(object):
    ''' Ansible math jinja2 tests '''

    def tests(self):
        return {
            # set theory
            'issubset': issubset,
            'issuperset': issuperset,
        }