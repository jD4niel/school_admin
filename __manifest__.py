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
    'author': "Daniel Acosta (jD4niel)",
    'website': "https://github.com/jD4niel",
    'category': 'Administration',
    'version': '0.1',
    'depends': ['base','web','portal','mail'],
    'data': [
        'security/ir_groups.xml',
        'security/ir_rules.xml',
        'data/ir_sequence.xml',
        'data/signature_data.xml',
        'data/res.users.csv',
        'data/student.csv',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/signatures_view.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}
