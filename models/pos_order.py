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

from odoo import fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order'

    pos_ar_id = fields.Many2one(
        'pos.ar',
        related='session_id.config_id.pos_ar_id',
        string='Point of sale',
        readonly=False
    )

    def _prepare_invoice(self):
        prepared_invoice = super(PosOrder, self)
        if self.pos_ar_id.id:
          prepared_invoice['pos_ar_id'] = self.pos_ar_id.id
        return prepared_invoice
