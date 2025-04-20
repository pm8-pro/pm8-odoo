# Copyright 2025 PM8 - Fabian Semal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Project Task Quick Create",

    'summary': """
    Quick task creation in list view
    """,

    'description': """
        This module allows for inline task creation in list view.
        Then the Edit button opens the task form for further encoding
    """,

    'license': 'LGPL-3',
    'author': "PM8",
    'website': "https://www.pm8.pro",
    'category': 'Project',
    'version': '16.0.1.0.0',
    'depends': ['project'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
}
