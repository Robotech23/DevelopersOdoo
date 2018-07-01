from odoo import api, models
from odoo.tools import float_round
from odoo.http import request


class report_admin(models.AbstractModel):
    #Modelo Abstracto
    _name = 'report.impuestos1.test_template'

    @ api.model
    #Render Html, paso de datos al template
    def  render_html (self, docids, data = None): 
        report_obj  = self.env [ 'report' ] 
        report  =  report_obj._get_report_from_name('impuestos1.test_template') 
        docargs  =  { 
            'doc_ids': docids,
            'doc_model':  'report.impuestos1', 
            'docs' :  self, 
            'data' : data,
        } 
        return  report_obj.render('impuestos1.test_template', docargs )

