# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Hospital System as training",

    'author': "Khaled Atef",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/doctors_rule.xml',
        'data/data.xml',
        'wizards/add_appointment.xml',
        'views/menus.xml',
        'views/adding_patient_info_to_contact.xml',
        'views/patient_view.xml',
        'views/adding_is_doctor_to_users.xml',
        'views/doctor_view.xml',
        'views/appointment_sequence.xml',
        'views/appointments_view.xml',
        'views/prescription_view.xml',
        'views/medicines_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

