

from odoo import models, fields, api, _

class CreditReleaseWizard (models.TransientModel):
    _name = 'credit.release.wizard'
    _description = 'Credit Release Wizard'

    reason_accept = fields.Text(required=True ,string = "Release Reason")

    def action_confirm_release(self):
        picking_id = self.env.context.get('active_id')

        if picking_id :
            picking = self.env['stock.picking'].browse(picking_id)

            picking.write ({
                'is_credit_hold' : False,
                'credit_release_reason' : self.reason_accept,
            })

            picking.message_post(
            body=f"The credit block was lifted by the manager. Reason: {self.reason_accept}"
            )