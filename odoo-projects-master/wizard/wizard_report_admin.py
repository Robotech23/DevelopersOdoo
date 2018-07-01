# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WizardReportCompras(models.TransientModel):
    #Modelo representado en el Wizard
    _name = "impuestos.wizard.compras"
    _description = "Wizar Libro de Compras"

    #Movimientos Destino
    periodo_compras_inicio = fields.Selection([('1','Todos los asientos Validados'),
        ('2', 'Todos los asientos')], string='Movimientos Destino', required=True)

    #Muestra cuentas
    periodo_compras_fin = fields.Selection([('1','Todos'), ('2','Con movimientos'), ('3' , 'Con saldo distinto a Cero')], string='Mostrar cuentas', required=True)

    #Fecha inicio
    excel_true_or_false1 = fields.Date('Fecha de Inicio',required=True)

    #ordenar por
    ordenarpor = fields.Selection([('1','Fecha'), ('2', 'Diario y Empresa')], string='Ordenar por', required=True)

    #incluir salario inicial
    saldo_inicial = fields.Boolean('incluir saldo inicial', required=True)

    #Fecha Fin
    fecha_fin = fields.Date('Fecha Finalizacion', required=True)



    @api.multi
    def action_report(self):
        #Método que llama la lógica para imprimir el reporte PDF del Libro de Compras
        excel = self.read(['excel_true_or_false1'])
        #Verificar si se quiere imprimir el reporte en formato EXCEL
        if excel == True:
            self.print_xls_report()
        else:
            data = {}
            res = self.read(['periodo_compras_inicio', 'periodo_compras_fin'])
            data['form'] = res[0]
            return self.env['report'].get_action([], 'impuestos1.test_template', data=data)

    @api.multi
    def print_xls_report(self):
        #Método que llama la lógica para imprimir el reporte EXCEL del Libro de Compras
        data = self.read('periodo_compras_inicio', 'periodo_compras_fin')[0]
        return {'type': 'ir.actions.report.xml',
                'report_name': 'impuestos1.test_template.xlsx',
                'datas': data
                }

    @api.multi
    def action_report_ventas(self):
        #Método que llama la lógica para imprimir el reporte PDF del Libro de Ventas
        data = {}
        res = self.read(['periodo_compras_inicio', 'periodo_compras_fin'])
        data['form'] = res[0]
        return self.env['report'].get_action([], 'impuestos1.test_template', data=data)

    @api.multi
    def print_xls_report_ventas(self, cr, uid, ids, context=None):
        #Método que llama la lógica para imprimir el reporte EXCEL del Libro de Ventas
        data = self.read(cr, uid, ids)[0]
        return {'type': 'ir.actions.report.xml',
                'report_name': 'impuestos1.test_template.xlsx',
                'datas': data
                }