{
    'name': "Sale Credit",

    'description': """
Long description of module's purpose
    """,

    'author': "Mohamed Atef",

    'category': 'Sale Stock',
    'version': '19.0.0.1',

    'depends': ['base','sale_stock','stock','account','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/credit_release_wizard.xml',
        'data/ir_cron_data.xml',
        'views/sale_credit_view.xml',
        'views/templates.xml',
    
        
    ],

}

