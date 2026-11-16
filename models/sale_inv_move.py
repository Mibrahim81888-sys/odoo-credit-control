from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleInvMoveInherit(models.Model):
    _inherit = 'stock.picking'
    is_credit_hold = fields.Boolean(string="Credit Hold")
    credit_release_reason=fields.Char(string="Reason", readonly=True)

    def button_validate(self):
            for picking in self: 
                if picking.is_credit_hold:
                    raise UserError("You cannot rely on exchange! This simple permission is the key to reaching the ordinary customer.")
            return super().button_validate()
    def _cron_release_credit_hold(self):
        help_pickings=self.search([
            ('is_credit_hold', '=', True),
            ('state', 'not in', ['done', 'cancel'])
        ])

        for picking in help_pickings :
            partner = picking.partner_id

            if not partner.use_credit_limit or partner.current_risk_amount <= partner.credit_limit:
                picking.is_credit_hold = False
                picking.message_post(
                    body="The credit block was automatically lifted by the system after the customer's debt fell below the allowed limit"
                )


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    def action_confirm(self):
        res = super().action_confirm()

        for order in self: 
           
            partner = order.partner_id
            if(
                partner.use_credit_limit
                and partner.current_risk_amount > partner.credit_limit
            ):
                pickings = order.picking_ids.filtered(
                    lambda p: p.state not in ["done","cancel"]
                )
                for picking in pickings:
                    picking.is_credit_hold = True
                    picking.message_post(
                        body="You have exceeded the permitted limit !!"
                    )
        return res

    


