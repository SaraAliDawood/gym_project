# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class GymProjectTrainer(models.Model):
    _name = "gym.trainer"
    _description = "Gym Trainer"
    _order = "name"

    name = fields.Char("Trainer Name", required=True, tracking=True)
    phone = fields.Char("Phone", tracking=True)
    national_id = fields.Char("National ID", required=True, tracking=True)
    image_500 = fields.Image("Photo", max_width=500, max_height=500)

    is_active = fields.Boolean("Is Active?", default=True)

  
    appointment_ids = fields.One2many(
        "gym.appointment",
        "trainer_id",
        string="Appointments"
    )
    number_of_appointments = fields.Integer(
        "Number of Appointments",
        compute="_compute_number_of_appointments",
    )
    status = fields.Selection(
        [
            ("available", "Available"),
            ("busy", "Busy"),
            ("on_leave", "On Leave"),
        ],
        string="Status",
        default="available",
    )

    
    # ------------------------- Constraints -------------------------
  
    @api.constrains('national_id')
    def _check_national_id(self):
        for trainer in self:
            if trainer.national_id:
                if len(trainer.national_id) != 14:
                    raise ValidationError("National ID must be exactly 14 digits")
                if not trainer.national_id.isdigit():
                    raise ValidationError("National ID must contain only digits")
                existing = self.search([
                    ('national_id', '=', trainer.national_id),
                    ('id', '!=', trainer.id)
                ])
                if existing:
                    raise ValidationError("National ID must be unique")
    def action_open_wizard(self):
        return {
            'name': "Trainer Report",
            'type': 'ir.actions.act_window',
            'res_model': 'trainer.report.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_trainer_id': self.id,
            }
        }
    @api.depends("appointment_ids")
    def _compute_number_of_appointments(self):
     for trainer in self:
        if trainer.appointment_ids:
            trainer.number_of_appointments = self.env['gym.appointment'].search_count([
                ('trainer_id', '=', trainer.id)
            ])
        else:
            trainer.number_of_appointments = 0
    
    def action_appointment_numbers(self):
        return {
            'name': "Appointments",
            'type': 'ir.actions.act_window',
            'res_model': 'gym.appointment',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('trainer_id', '=', self.id)]
        }     