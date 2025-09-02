from odoo import models, fields

class TrainerReportWizard(models.TransientModel):
    _name = "trainer.report.wizard"
    _description = "Trainer Report Wizard"

    trainer_id = fields.Many2one("gym.trainer", string="Trainer", required=True)
    # from_date = fields.Many2one(
    #     "gym.appointment",
    #     string="From Appointment",
    #     domain="[('trainer_id', '=', trainer_id)]",
    #     required=True
    # )

    # to_date = fields.Many2one(
    #     "gym.appointment",
    #     string="To Appointment",
    #     domain="[('trainer_id', '=', trainer_id)]",
    #     required=True
    # )
    from_date = fields.Datetime("From Date", required=True)
    to_date = fields.Datetime("To Date", required=True)


    def action_print(self):

        from_date = self.from_date.start_time
        to_date = self.to_date.end_time

    
        return {'type': 'ir.actions.act_window_close'}
