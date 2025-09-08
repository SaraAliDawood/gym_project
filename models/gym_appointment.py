from odoo import models, fields , api
from odoo.exceptions import ValidationError
from datetime import datetime

# Model: Appointment

WEEK_DAYS = [
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
]

class GymAppointment(models.Model):
    _name = "gym.appointment"
    _description = "Gym Appointment"
    # _rec_name = "name"
    _rec_name = "trainer_id"
    # Trainer info
    trainer_id = fields.Many2one(
        "gym.trainer", 
        string="Trainer",   
    )
   
    trainer_cost_inside = fields.Float(
       string="Trainer Cost Out Working Hours",
       related="trainer_id.trainer_cost_inside"
    )
    trainer_cost_outside = fields.Float(
       string="Trainer Cost Within Working Hours",
       related="trainer_id.trainer_cost_outside"
    )
    session_cost = fields.Float(
       string="Session Cost",
       related="trainer_id.session_cost"
    )
    subscription_id = fields.Many2one(
    "gym.subscription",
    string="Subscription"
)

    # name = fields.Char(
    #     string="Appointment",
    #     compute="_compute_name",
    #     store=True
    # )
    # trainer_nid = fields.Char(
    #     string="Trainer National ID", 
    #     related="trainer_id.national_id", 
    #     store=True, 
    #     readonly=True
    # )
    # trainer_phone = fields.Char(
    #     string="Trainer Phone", 
    #     related="trainer_id.phone", 
    #     store=True, 
    #     readonly=True
    # )
    # trainer_image = fields.Image(
    #     string="Trainer Photo", 
    #     related="trainer_id.image_500", 
    #     store=True, 
    #     readonly=True
    # )

 
    weekday = fields.Selection(WEEK_DAYS, string="Weekday", required=True)
    start_time = fields.Datetime("Start Time", required=True)
    end_time = fields.Datetime("End Time", required=True)

    # name = fields.Char(
    #     string="Appointment",
    #     compute="_compute_name",
    #     store=True
    # )
    @api.constrains("start_time", "end_time")
    def _check_time_range(self):
        for rec in self:
            if rec.end_time <= rec.start_time:
                raise ValidationError("End Time must be greater than Start Time.")
    # @api.depends("weekday", "start_time", "end_time")
    # def _compute_name(self):
    #     for rec in self:
    #         rec.name = f"{rec.weekday} ({rec.start_time} - {rec.end_time})" if rec.weekday else ""