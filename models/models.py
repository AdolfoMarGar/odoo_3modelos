
from odoo import models, fields, api


class restaurante(models.Model):
    _name = 'odoo_3modelos.res'
    _description = 'Define las caracteristicas de un restaurante'

    name = fields.Char('Direccion', required=True)
    mesas = fields.Integer(string='N. de mesas',required=True)

    empleados_ids = fields.One2many('odoo_3modelos.emp','res_id',string='Empleados')
    productos_ids = fields.One2many('odoo_3modelos.pro','res_id',string='Productos')
    


class empleado(models.Model):
    _name = 'odoo_3modelos.emp'
    _description = 'Define las caracteristicas de un empleado'
    _order = 'fecha'
    
    dni = fields.Char(string='DNI',required=True, size=9)
    nom = fields.Char(string= 'Nombre')
    ape = fields.Char(string= 'Apellidos')
    fecha = fields.Date(string='Fecha de incorporación')
    anios = fields.Integer(string='Años', default=18)
    tipo = fields.Selection(string='Tipo trabajo', selection=[('c','Cocinero'),('g','Gerente'),('b','base')],default = 'b')

    res_id = fields.Many2one('odoo_3modelos.res',string='Restaurante')


class producto(models.Model):
    _name = 'odoo_3modelos.pro'
    _description = 'Define los caracteristicas de los productos'

    nom = fields.Char(string= 'Nombre',required=True)
    coste = fields.Float('Coste',(3,2), default=0.0)

    res_id = fields.Many2one('odoo_3modelos.res',string='Restaurante')
