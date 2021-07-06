# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError


class Signatures(models.Model):
    _name = 'signature'
    _description = 'Signatures'


    name = fields.Char('Name')

class Semester(models.Model):
    _name = 'school.semester'
    _descirption = 'Semesters'
    _rec_name = 'semester'

    semester = fields.Integer('Semester',required=True)
    group_ids = fields.One2many('school.group','semester_id',string='Grade',required=True)


class Group(models.Model):
    _name = 'school.group'
    _descirption = 'Group'
    _rec_name = 'group'

    group = fields.Char('Group',required=True)
    semester_id = fields.Many2one('school.semester',string='Semester')