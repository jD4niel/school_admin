# -*- coding: utf-8 -*-
# Coded by jD4niel (Daniel Acosta) - jdanielcontreras0@gmail.com
{
    'name': "School Management",
    'summary': """
        School management for parents and teachers 
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "jD4niel",
    'website': "https://github.com/jD4niel",
    'category': 'Administration',
    'version': '0.1',
    'depends': ['base','web','portal','mail'],
    'data': [
        'data/signature_data.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/signatures_view.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}
