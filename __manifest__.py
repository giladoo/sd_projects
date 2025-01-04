# -*- coding: utf-8 -*-
{
    'name': 'SD Projects',
    'version': '17.0.1.0.0',
    'description': '',
    'category': 'Services',
    'summary': """ Projects, Clients and Contractors """,
    'author': 'Arash Homayounfar',
    'company': 'Giladoo',
    'maintainer': 'Giladoo',
    'website': "https://www.giladoo.com/projects",
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['base', 'web', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/hr_employee_views.xml',

    ],
    'assets':{
        'web.assets_backend':[
          # 'sd_hr/static/src/components/**/*',
        ],
    },

    'license': 'LGPL-3',
}
