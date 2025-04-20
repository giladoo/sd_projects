# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import uuid
from icecream import ic

class SdProjectsProjects(models.Model):
    _name = 'sd_projects.projects'
    _description = 'Projects'
    _inherit = ['mail.thread']


    name = fields.Char(required=True, translate=True, tracking=True)
    project_no = fields.Char(tracking=True)
    client = fields.Many2one('res.partner',tracking=True)
    start_date = fields.Date(tracking=True)
    uu_id = fields.Char(default= lambda self: uuid.uuid4().hex)
    sequence = fields.Integer(default=100)


    def update_uuid(self):
        active_ids = self.env.context.get('active_ids')
        records = self.browse(active_ids)
        for rec in records:
            rec.uu_id = uuid.uuid4().hex
