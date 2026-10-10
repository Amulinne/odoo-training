# -*- coding: utf-8 -*-

from odoo import models, fields


class DrivingLesson(models.Model):
    _name = 'driving.lesson'
    _description = 'Занятие по вождению'

    name = fields.Char(
        string='Наименование занятия',
        required=True
    )

    date = fields.Datetime(
        string='Дата и время занятия',
        required=True
    )

    exercise_ids = fields.One2many(
        comodel_name='driving.exercise',
        inverse_name='lesson_id',
        string='Упражнения занятия'
    )

    member_ids = fields.Many2many(
        comodel_name='res.users',
        string='Курсанты'
    )

    report_ids = fields.One2many(
        comodel_name='driving.report',
        inverse_name='lesson_id',
        string='Отчёт инструктора'
    )


class DrivingReport(models.Model):
    _name = 'driving.report'
    _description = 'Отчёт инструктора'

    name = fields.Char(
        string='Наименование отчёта',
        required=True
    )

    date = fields.Datetime(
        string='Дата составления',
        required=True
    )

    text = fields.Html(
        string='Текст отчёта'
    )

    instructor = fields.Many2one(
        comodel_name='res.users',
        string='Инструктор'
    )

    senior_instructor = fields.Many2one(
        comodel_name='res.users',
        string='Старший инструктор'
    )

    lesson_id = fields.Many2one(
        comodel_name='driving.lesson',
        string='Занятие',
        required=True,
        ondelete='cascade'
    )

    _sql_constraints = [
        (
            'unique_lesson_id',
            'unique(lesson_id)',
            'Для этого занятия уже создан отчёт.'
        ),
    ]


class DrivingExercise(models.Model):
    _name = 'driving.exercise'
    _description = 'Упражнение'

    name = fields.Char(
        string='Название упражнения'
    )

    score = fields.Integer(
        string='Оценка'
    )

    state = fields.Selection(
        [
            ('not_passed', 'Не сдано'),
            ('passed', 'Сдано'),
        ],
        default='not_passed',
        string='Статус'
    )

    lesson_id = fields.Many2one(
        comodel_name='driving.lesson',
        string='Занятие',
        required=True,
        ondelete='cascade'
    )
