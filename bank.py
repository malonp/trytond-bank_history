##############################################################################
#
#    GNU Condo: The Free Management Condominium System
#    Copyright (C) 2016- M. Alonso <port02.server@gmail.com>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from trytond.pool import PoolMeta


__all__ = ['Bank', 'BankAccount', 'BankAccountNumber', 'BankAccountParty']


class Bank(metaclass=PoolMeta):
    __name__ = 'bank'

    @classmethod
    def __setup__(cls):
        super(Bank, cls).__setup__()
        cls._history = True


class BankAccount(metaclass=PoolMeta):
    __name__ = 'bank.account'

    @classmethod
    def __setup__(cls):
        super(BankAccount, cls).__setup__()
        cls._history = True


class BankAccountNumber(metaclass=PoolMeta):
    __name__ = 'bank.account.number'

    @classmethod
    def __setup__(cls):
        super(BankAccountNumber, cls).__setup__()
        cls._history = True


class BankAccountParty(metaclass=PoolMeta):
    __name__ = 'bank.account-party.party'

    @classmethod
    def __setup__(cls):
        super(BankAccountParty, cls).__setup__()
        cls._history = True
