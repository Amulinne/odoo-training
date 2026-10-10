# -*- coding: utf-8 -*-

from odoo import models, fields


class Meeting(models.Model):
    _name = 'snt.meeting'
    _description = 'Собрание'

    name = fields.Char(
        string='Наименование собрания',
        required=True
    )

    date = fields.Datetime(
        string='Дата и время собрания',
        required=True
    )

    question_ids = fields.One2many(
        comodel_name='snt.question',
        inverse_name='meeting_id',
        string='Вопросы'
    )

    member_ids = fields.Many2many(
        comodel_name='res.users',
        string='Список участников'
    )

    protocol_id = fields.Many2one(
        comodel_name='snt.protocol',
        string='Протокол'
    )


class Protocol(models.Model):
    _name = 'snt.protocol'
    _description = 'Протокол'

    name = fields.Char(
        string='Наименование протокола',
        required=True
    )

    date = fields.Datetime(
        string='Дата и время составления',
        required=True
    )

    text = fields.Html(
        string='Текст протокола'
    )

    chairman = fields.Many2one(
        comodel_name='res.users',
        string='Председатель'
    )

    secretary = fields.Many2one(
        comodel_name='res.users',
        string='Секретарь'
    )

    meeting_id = fields.Many2one(
        comodel_name='snt.meeting',
        string='Собрание'
    )


class Question(models.Model):
    _name = 'snt.question'
    _description = 'Вопрос'

    name = fields.Char(
        string='Текст вопроса'
    )

    yes = fields.Integer(
        string='Голосов "За"'
    )

    state = fields.Selection(
        [
            ('not_set', 'Решение не принято'),
            ('yes', 'Принято'),
        ],
        default='not_set',
        string='Статус решения'
    )

    meeting_id = fields.Many2one(
        comodel_name='snt.meeting',
        string='Собрание'
    )