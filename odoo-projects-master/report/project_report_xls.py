
class ClassABCD(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        current_date = strftime("%Y-%m-%d", gmtime())
        logged_users = self.env['res.users'].search([('id', '=', data['create_uid'][0])])
        sheet = workbook.add_worksheet()
        # add the rest of the report code here

ClassABCD('report.impuestos1.test_template.xlsx', 'report.impuestos1.test_template')