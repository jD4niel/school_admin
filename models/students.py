# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError

class Students(models.Model):
    _name = 'student'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Students'
    _order = 'number desc'
    _rec_name = 'number'

    groups = [('a', 'A'),\
             ('b', 'B'),\
             ('c', 'C'),\
             ('d', 'D'),\
             ('e', 'E'),\
             ('f', 'F'),\
             ('g', 'G')]
    
    name = fields.Char('Name', required=True)
    number = fields.Integer('Number plates', required=True)
    birthdate = fields.Datetime('Birthdate', required=True)
    tutor_id = fields.Many2one('res.users',string='Tutor')
    grade = fields.Selection([('1', '1'),('2', '2'),('3', '3')],'Grade')
    group = fields.Selection(groups,'Group')
    signature_ids = fields.Many2many('signature','students_signatures_ids','student_id','signature_id',string='Signatures')
    grades_ids = fields.Many2many('school.grades','student_school_grades_rel','student_id','school_grade_id',string='School Grades')
    image = fields.Binary('Image')


class SchoolGrades(models.Model):
    _name = 'school.grades'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'School Grades'
    _rec_name = 'name'


    name = fields.Char('Name', required=True)
    grade = fields.Integer('Grade',required=True)
    signature_id = fields.Many2one('signature',string='Signature',required=True)
    teacher_id = fields.Many2one('res.users',string='Teacher')
    notes = fields.Text('Notes')
