# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SdProjectsHrEmployee(models.Model):
    _inherit = 'hr.employee'

    project_name = fields.Many2one('sd_projects.projects')
