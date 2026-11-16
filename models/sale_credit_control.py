from odoo import models, fields, api

class SaleContactLimitInherit(models.Model):
    _inherit = 'res.partner'
    use_credit_limit = fields.Boolean(string='Enforce Credit Limit')
    credit_limit = fields.Float(string="Credit Limit")
    current_risk_amount = fields.Float(string="Current Risk Amount", compute="_compute_current_risk", store=True)

    @api.depends('invoice_ids.move_type',
                 'invoice_ids.state',
                 'invoice_ids.payment_state',
                 'invoice_ids.amount_residual',
                 'sale_order_ids.state',
                 'sale_order_ids.invoice_status',
                 'sale_order_ids.amount_total',
        )
    def _compute_current_risk(self):
        for partner in self:
            unpaid_invoices = partner.invoice_ids.filtered(
                lambda inv: inv.move_type in ['out_invoice','out_refund']
                and inv.state == 'posted'
                and inv.payment_state in ['not_paid','partial']
            )
            total_unpaid = sum(unpaid_invoices.mapped('amount_residual'))

            unvoiced_orders = partner.sale_order_ids.filtered(
                lambda order : order.state == 'sale'
                and order.invoice_status in ['to invoice','no']

            )
            total_unvoice = sum(unvoiced_orders.mapped('amount_total'))
            partner.current_risk_amount = total_unpaid + total_unvoice

