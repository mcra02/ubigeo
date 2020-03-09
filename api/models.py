from django.db import models

# Create your models here.

class Departamento(models.Model):

    id = models.AutoField(
        primary_key=True,
        db_column='in_id_departamento'
    )

    name = models.CharField(
        db_column='vc_nombre',
        max_length=100,
        null=False,
        blank=False
    )

    description = models.CharField(
        db_column='vc_description',
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'departamento'

class Provincia(models.Model):

    id = models.AutoField(
        primary_key=True,
        db_column='in_id_provincia'
    )
    
    name = models.CharField(
        db_column='vc_nombre',
        max_length=100,
        null=False,
        blank=False
    )

    description = models.CharField(
        db_column='vc_description',
        max_length=500,
        null=True,
        blank=True
    )

    departamento = models.ForeignKey(
        Departamento,
        models.DO_NOTHING,
        null=False,
        blank=False,
        db_column='in_id_departamento'
    )

    class Meta:
        db_table = 'provincia'

class Distrito(models.Model):

    id = models.AutoField(
        primary_key=True,
        db_column='in_id_distrito'
    )
    
    name = models.CharField(
        db_column='vc_nombre',
        max_length=100,
        null=False,
        blank=False
    )

    description = models.CharField(
        db_column='vc_description',
        max_length=500,
        null=True,
        blank=True
    )

    provincia = models.ForeignKey(
        Provincia,
        models.DO_NOTHING,
        null=False,
        blank=False,
        db_column='in_id_provincia'
    )

    class Meta:
        db_table = 'distrito'

