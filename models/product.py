from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Float fields
    trainer_cost_inside = fields.Float(string="Trainer Cost Inside Working Hours")
    trainer_cost_outside = fields.Float(string="Trainer Cost Outside Working Hours")

    trainer_percentage_inside = fields.Float(string="Trainer Percentage Inside Working Hours")
    trainer_percentage_outside = fields.Float(string="Trainer Percentage Outside Working Hours")

    # Boolean fields
    is_subscription = fields.Boolean(string="Is Subscription?")
    can_be_freezed = fields.Boolean(string="Can Be Freezed?")
    is_locker = fields.Boolean(string="Is Locker?")
