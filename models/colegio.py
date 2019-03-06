from odoo import models,fields, api

class colegio(models.Model):
    _name = 'escuelas.colegio'
    name = fields.Char(string="name", required=True, help="Nombre del colegio")
    direccion = fields.Char(string="direccion", required=True, help="Direccion del colegio")
    tipo = fields.Selection([
        ('Educacion Infantil', 'Educacion Infantil'),
        ('Secundaria', 'Secundaria'), 
        ('Universidad', 'Universidad')], string='tipo')
    estudiante_ids = fields.One2many("escuelas.estudiante", "colegio_id", string="estudiante")
    profesor_ids = fields.One2many("escuelas.profesor", "colegio_id", string="profesor")