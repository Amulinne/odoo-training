# -*- coding: utf-8 -*-
{
    'name': "lab_suvarskiy",
    'summary': "Лабораторная работа: расширение модели crm.lead",
    'description': "Учебный модуль, добавляющий поля в форму инициативы CRM",
    'author': "Суварский Давид Евгеньевич, группа КТ-31-23",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'crm', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}