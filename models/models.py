# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from icecream import ic

class SdProjectsProjects(models.Model):
    _name = 'sd_projects.projects'
    _description = 'Projects'

    name = fields.Char(required=True, translate=True)
    project_no = fields.Char()
    client = fields.Many2one('res.partner')
    start_date = fields.Date()


class SdProjectsEmployees(models.Model):
    _name = 'sd_projects.employees'
    _description = 'Employee Projects'
    _rec_name = 'project'
    _order = 'project'


    employee = fields.Many2one('hr.employee', required=True)
    project = fields.Many2one('sd_projects.projects', required=True)
    plan = fields.Float(default=0)
    # main = fields.Boolean(default=False)

    @api.onchange('employee', 'project')
    def plan_calculator(self):
        if self.employee and self.project:
            employee_plans = self.search([('employee', '=', self.employee.id)])
            plan_sum = sum(list(rec.plan for rec in employee_plans))
            self.plan =  100 - plan_sum
        else:
            self.plan = 0

    @api.constrains('plan', 'project')
    def _check_price_range(self):
        for record in self:
            employee_plans = self.search([('employee', '=', record.employee.id), ('id', '!=', record.id)])
            plan_sum = sum(list(rec.plan for rec in employee_plans))
            projects = list(rec.project for rec in employee_plans)
            # ic(plan_sum, record.plan)



            if record.project in projects:
                raise ValidationError(f"The {record.project.name} had been assigned to {record.employee.name}.")
            if record.plan < 0 or record.plan > 100:
                raise ValidationError("plan must be between 0 and 100!")
            if plan_sum + record.plan > 100:
                raise ValidationError("Total cannot be more than 100!")
