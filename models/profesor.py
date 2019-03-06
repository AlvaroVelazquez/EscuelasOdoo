from odoo import models,fields, api

class profesor(models.Model):
    _name = 'escuelas.profesor'
    name = fields.Char(string="name", required=True, help="Nombre del profesor")
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del profesor")
    estudiante_ids = fields.One2many("escuelas.estudiante", "profesor_id", string="estudiante")
    colegio_id = fields.Many2one("escuelas.colegio", string="colegio")



