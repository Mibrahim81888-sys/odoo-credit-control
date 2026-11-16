# from odoo import http


# class SaleStock(http.Controller):
#     @http.route('/sale_stock/sale_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_stock/sale_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_stock.listing', {
#             'root': '/sale_stock/sale_stock',
#             'objects': http.request.env['sale_stock.sale_stock'].search([]),
#         })

#     @http.route('/sale_stock/sale_stock/objects/<model("sale_stock.sale_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_stock.object', {
#             'object': obj
#         })

