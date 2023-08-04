# -*- coding: utf-8 -*-
{
    'name': "Uanalyst Contract",

    'summary': """
        Uanalyst Contract""",

    'description': """
        Uanalyst Contract
    """,
    'sequence': '-100',
    'author': "Mohamed Nagy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale_management', 'hr', 'account', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        # 'views/po_lines_details_wizard_views.xml',
        'views/po_views.xml',
        'views/po_lines_views.xml',
        'views/contract_views.xml',
        'views/lg_configuration_views.xml',
        'views/payment_terms_views.xml',
        'views/contacts_views.xml',
        'views/accepted_views.xml',
        'views/site_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
