from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError

class StudentReport(models.AbstractModel):
    _name = 'report.school_admin.student_doc'
    _description = 'Student Report'


    @api.model
    def _get_report_values(self, docids, data=None):
        # Render report
        ids = docids or data.get('ids') 
        model_name = 'student'
        docs = self.env[model_name].browse(ids)
        return {
            'doc_ids': ids,
            'doc_model': model_name,
            'docs': docs,
            'company': self.env.user.company_id,
            'self': self,
            'data': dict(
                data,
            ),
        }