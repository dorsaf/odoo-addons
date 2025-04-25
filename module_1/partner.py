from odoo import models, fields

class Partner(models.Model):
    _name = 'module_1.partner'
    _description = 'Partner'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    is_company = fields.Boolean(string='Is a Company', default=False)