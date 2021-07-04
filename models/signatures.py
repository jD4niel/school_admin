# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError


class Signatures(models.Model):
    _name = 'signature'
    _description = 'Signatures'


    name = fields.Char('Name')
