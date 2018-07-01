# -*- coding: utf-8 -*-
{
    'name': "impuestos1",

    'summary': """
        Imprime reportes PDF y EXCEL de las Facturas de Clientes (Libro de Ventas)
        y Facturas del Proveedor (Libro de Compras)
        """,

    'description': """
        Imprime Reportes PDF y ECXEL
    """,

    'author': "Juan Barrios",


    'category': 'Contabilidad',
    'version': '0.1',

    # Modulos necesarios para el correcto funcionamiento
    'depends': ['base', 'report', 'account'],

    # Vistas
    'data': [
        'views/views.xml',
        'report/report_view.xml',
        'report/test_template.xml'
    ],
}