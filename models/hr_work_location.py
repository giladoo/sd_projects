
from odoo import models, fields, api, _

class SdProjectsHrWorkLocation(models.Model):
    _inherit = "hr.work.location"

    project_name = fields.Many2one('sd_projects.projects')