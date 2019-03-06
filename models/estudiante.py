from odoo import models,fields, api

class estudiante(models.Model):
    _name = 'escuelas.estudiante'
    name = fields.Char(string="name", required=True, help="Nombre del estudiante")
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del estudiante")
    profesor_id = fields.Many2one("escuelas.profesor", string="profesor")
    colegio_id = fields.Many2one("escuelas.colegio", string="colegio")


   
    
    