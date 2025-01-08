from django.db import models

# Relación 1 a 1: Cada banda tiene un perfil único con detalles adicionales.
# Tiene que ir primero este modelo por que se heredan los atributos entre tablas.
class PerfilBanda(models.Model):
    descripcion = models.TextField()
    anio_formacion = models.IntegerField()
    genero = models.CharField(max_length=100)

    def __str__(self):
        return f"Banda de género {self.genero}, formada en {self.anio_formacion}"

# Modelo para Banda.
class Banda(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    perfil = models.OneToOneField(PerfilBanda, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

# Relación 1 a Muchos: Una banda tiene varios álbumes.
class Album(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} de {self.banda.nombre}"

# Relación Muchos a Muchos: Los miembros pueden pertenecer a varias bandas, y las bandas tienen varios miembros.
# Modelo para Miembro.
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    instrumento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.instrumento})"

# Modelo para la relación entre Miembro y Banda. Siempre en las relaciones muchos a muchos se crea un modelo intermedio. (otra tabla)
class MiembroBanda(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    rol = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.miembro.nombre} en {self.banda.nombre}"
