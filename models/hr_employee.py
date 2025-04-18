# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from icecream import ic

class SdProjectsHrEmployee(models.Model):
    _inherit = 'hr.employee'

    project_name = fields.Many2one('sd_projects.projects')
    project = fields.Many2one('sd_projects.employees')
    project_n = fields.Many2one("sd_projects.projects", compute="_project_n", store=True)
    # document_ids = fields.One2many('sd_hr_documents.attachments',
    #                                'employee_id',
    #                                string="documents")
    projects_count = fields.Integer(compute='_compute_projects_count',
                                    string='Projects',
                                    help='Count of projects.')
    @api.onchange('project')
    def _project_n(self):
        for rec in self:
            rec.project_n = rec.project.project

    def _compute_projects_count(self):
        for rec in self:
            rec.projects_count = self.env['sd_projects.employees'].search_count([('employee', '=', rec.id)])

    def action_projects_view(self):
        self.ensure_one()
        ic(self)
        context = dict(self.env.context)
        context['default_employee'] = self.id
        context['search_view_ref'] = 'sd_projects.employee_projects_search_one'
        domain = [('employee', '=', self.id)]
        # return {}
        return {
            'name': _('Projects'),
            'domain': domain,
            'res_model': 'sd_projects.employees',
            'type': 'ir.actions.act_window',
            # 'view_id': False,
            'view_id': self.env.ref('sd_projects.employee_projects_list_one').id,

            'view_mode': 'tree',
            'context': context,
        }
