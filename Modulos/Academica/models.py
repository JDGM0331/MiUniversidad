from django.db import models

# Create your models here.

class Carrera(models.Model): # Class that allows to create and implement the models
    codigo = models.CharField(max_length=3, primary_key=True) # text data
    nombre = models.CharField(max_length=50) 
    duracion = models.PositiveSmallIntegerField(default=5) # numerical data

    def __str__(self): # Name each object found
        txt = "{0} (Duración: {1} años(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField() # date data
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F') # enumeration data
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE) # foreign key from carrera
    vigencia = models.BooleanField(default=True) # boolean data

    def nombreCompleto(self): # Returns the full name in a given format
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia: 
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)

class Curso(models.Model): 
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)

class Matricula(models.Model): 
    id = models.AutoField(primary_key=True) # autoincrementing data
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F": 
            letraSexo = "a"
        else: 
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fecMat)
