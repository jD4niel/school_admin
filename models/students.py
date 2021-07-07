# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError


class Students(models.Model):
    _name = 'student'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Students'
    _order = 'number desc'
    _rec_name = 'number'

    
    name = fields.Char('Name', required=True)
    number = fields.Char('Number plates')
    address = fields.Text('Address')
    birthdate = fields.Datetime('Birthdate')
    tutor_id = fields.Many2one('res.users',string='Tutor', required=True)
    semester_id = fields.Many2one('school.semester',string='Semester', required=True)
    group_id = fields.Many2one('school.group',string='Group', required=True)
    signature_ids = fields.Many2many('signature','students_signatures_ids','student_id','signature_id',string='Signatures')
    grades_ids = fields.One2many('school.grades','student_id',string='School Grades')
    image = fields.Binary('Image')


    @api.onchange('grades_ids')
    def _onchange_grades_ids(self):
        args = {}
        args['domain'] = {'grades_ids': [('signature_id.id','not in',self.grades_ids.mapped('signature_id.id'))]}
        print("\n args :  %s \n"%args)
        return args

    @api.model
    def create(self, vals):
        res = super(Students, self).create(vals)
        res.number = self.env['ir.sequence'].next_by_code('student') if res else False
        return res


class SchoolGrades(models.Model):
    _name = 'school.grades'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'School Grades'
    _rec_name = 'signature_id'


    grade = fields.Integer('Grade',required=True)
    signature_id = fields.Many2one('signature',string='Signature',required=True)
    teacher_id = fields.Many2one('res.users',string='Teacher')
    notes = fields.Text('Notes')
    student_id = fields.Many2one('student',string='Student')

