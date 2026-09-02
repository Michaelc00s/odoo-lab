from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    ai_category = fields.Selection(
        [
            ("sales", "Sales"),
            ("support", "Support"),
            ("accounting", "Accounting"),
            ("other", "Other"),
        ],
        string="AI Category",
    )

    ai_confidence = fields.Float(
        string="AI Confidence",
    )

    ai_summary = fields.Text(
        string="AI Summary",
    )

    ai_processed = fields.Boolean(
        string="AI Processed",
        default=False,
    )
    ai_last_processed = fields.Datetime(
	    string="AI Last Processed",
    )
    ai_status_note = fields.Char(
    string="AI Status Note",
    )	

    def action_process_with_ai(self):
        for lead in self:
            lead.write({
                "ai_category": "sales",
                "ai_confidence": 0.95,
                "ai_summary": f"AI processed opportunity: {lead.name}",
                "ai_processed": True,
		"ai_last_processed": fields.Datetime.now(),
            })

        return True








