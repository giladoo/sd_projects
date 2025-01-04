# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SdProjectsProjects(models.Model):
    _name = 'sd_projects.projects'
    _description = 'Projects'

    name = fields.Char(required=True, translate=True)
    project_no = fields.Char()
    client = fields.Many2one('res.partner')
    start_date = fields.Date()
