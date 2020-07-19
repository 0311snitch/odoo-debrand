{
    'name': "Odoo Debranding",
    'version': "13.0.1.2.2",
    'summary': """Odoo Backend and Front end Debranding""",
    'description': """Debrand Odoo,Debranding, odoo13""",
    'author': "Kirill Sudnikovich",
    'website': "https://sntch.dev/",
    'category': 'Tools',
    'depends': ['base_setup'],
    'data': [
        'views/views.xml',
        'views/res_config_views.xml',
        'views/ir_module_views.xml'
    ],
    'qweb': ["static/src/xml/base.xml"],
    'license': "AGPL-3",
    'installable': True,
    'application': False
}
