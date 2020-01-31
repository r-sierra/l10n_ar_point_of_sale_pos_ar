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
from odoo.exceptions import ValidationError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_ar_id = fields.Many2one('pos.ar', string='Point of sale')

    @api.onchange('module_account')
    def _onchange_module_account(self):
        super(PosConfig, self)._onchange_module_account()
        if not self.module_account:
            self.pos_ar_id = False

    @api.constrains('company_id', 'pos_ar_id')
    def _check_company_pos_ar(self):
        if self.pos_ar_id and self.pos_ar_id.company_id.id != self.company_id.id:
            raise ValidationError(_("The point of sale number and the point of sale must belong to the same company."))
