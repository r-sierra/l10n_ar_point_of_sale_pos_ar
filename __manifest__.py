# -*- encoding: utf-8 -*-
##############################################################################
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

{
    'name': 'Terminal Punto de Venta - Talonario por defecto',
    'version': '12.0.0.3.0',
    'category': 'Sales/Point Of Sale',
    'summary': 'Talonario predeterminado para Terminal Punto de Venta',
    'description': 'Permite definir el Talonario a utilizar para cada TPV',
    'depends': [
        'point_of_sale',
        'l10n_ar_point_of_sale'
    ],
    'data': [
        'views/pos_config_view.xml',
    ],
    'installable': True,
    'author': 'Roberto Sierra',
    'website': 'https://github.com/r-sierra',
    'license': 'GPL-3',
}
