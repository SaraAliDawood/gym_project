from odoo import models, fields


class GymSubscription(models.Model):
    _name = "gym.subscription"
    _description = "Gym Subscription"
    _rec_name = "trainee_id"

    # -------------------------
    # Trainer info
    # -------------------------
    trainer_id = fields.Many2one(
        "gym.trainer",
        string="Trainer"
    )

    trainer_national_id = fields.Char(
        string="Trainer National ID",
        related="trainer_id.national_id",
        store=True,
        readonly=True
    )
    trainer_phone = fields.Char(
        string="Trainer Phone",
        related="trainer_id.phone",
        store=True,
        readonly=True
    )

    # -------------------------
    # Trainee info
    # -------------------------
    trainee_id = fields.Many2one(
        "gym.trainee",
        string="Trainee",
        required=True
    )

    trainee_national_id = fields.Char(
        string="Trainee National ID",
        related="trainee_id.national_id",
        store=True,
        readonly=True
    )
    trainee_phone = fields.Char(
        string="Trainee Phone",
        related="trainee_id.phone",
        store=True,
        readonly=True
    )

    # -------------------------
    # Trainer appointments
    # -------------------------
    appointment_ids = fields.One2many(
        "gym.appointment",
        "subscription_id",
        string="Appointments"
    )

    service_id = fields.Many2one(
        "product.template",
        string="Service",
        required=True,
        domain=[("detailed_type", "=", "service"), ("is_subscription", "=", True)]
    )

    price = fields.Float(
        string="Price",
        related="service_id.list_price",
        store=True,
        readonly=True
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("running", "Running"),
            ("pause", "Paused"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft"
    )

    # -------------------------
    # Actions
    # -------------------------
    def action_draft(self):
        self.state = "draft"

    def action_running(self):
        self.state = "running"

    def action_pause(self):
        self.state = "pause"

    def action_cancel(self):
        self.state = "cancel"

    def action_done(self):
        self.state = "done"

    # -------------------------
    # Print All Subscriptions
    # -------------------------
    # def print_all_subscriptions(self):
    #     """Generate a PDF report for all subscriptions."""
    #     all_subs = self.env["gym.subscription"].search([])
    #     return self.env.ref("gym_project.action_gym_subscription_all").report_action(all_subs)
