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

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order'

    pos_ar_id = fields.Many2one(
        'pos.ar',
        related='session_id.config_id.pos_ar_id',
        string='Point of sale',
        readonly=False
    )

    @api.multi
    def action_pos_order_invoice(self):
        super(PosOrder, self).action_pos_order_invoice()

        for order in self:
            if order.invoice_id:
                inv = order.invoice_id
                if inv.pos_ar_id:
                    inv.update({
                        'denomination_id': inv.get_invoice_denomination().id,
                        'pos_ar_id': order.pos_ar_id.id
                    })
