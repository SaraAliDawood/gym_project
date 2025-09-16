from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    trainer_percentage_inside = fields.Float(
        string="Trainer Percentage Inside Working Hours",
        default=40
    )
    trainer_percentage_outside = fields.Float(
        string="Trainer Percentage Outside Working Hours",
        default=60
    )

    
  


    is_subscription = fields.Boolean(string="Is Subscription?")
    can_be_freezed = fields.Boolean(string="Can Be Freezed?")
    is_locker = fields.Boolean(string="Is Locker?")
