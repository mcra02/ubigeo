from django.db import models

# Create your models here.

class Departamento(models.Model):

    id = models.AutoField(
        primary_key=True,
        db_column='in_id_region'
    )

    name = models.CharField(
        db_column='vc_nombre',
        max_length=100,
        null=False,
        blank=False
    )

    descripcion = models.CharField(
        db_column='vc_descripcion',
        max_length=500,
        null=True,
        blank=True
    )

    ubigeo = models.CharField(
        db_column='vc_ubigeo',
        max_length=10,
        null=True,
        blank=True
    )

    status = models.BooleanField(
        db_column='bo_estado',
        default=True,
    )

    user_created = models.CharField(
        db_column='vc_id_usuario_creacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    user_modified = models.CharField(
        db_column='vc_id_usuario_modificacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        'date created at',
        auto_now_add=True,
        null=False,
        blank=False,
        db_column='ts_fecha_creacion',
        help_text='Date time on which the object was created.'
    )
    date_modified = models.DateTimeField(
        'date modified at',
        auto_now=True,
        null=True,
        blank=True,
        db_column='ts_fecha_modificacion',
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        db_table = 'gn_region'

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

    descripcion = models.CharField(
        db_column='vc_descripcion',
        max_length=500,
        null=True,
        blank=True
    )

    departamento = models.ForeignKey(
        Departamento,
        models.DO_NOTHING,
        null=False,
        blank=False,
        db_column='in_id_region'
    )

    ubigeo = models.CharField(
        db_column='vc_ubigeo',
        max_length=10,
        null=True,
        blank=True
    )

    status = models.BooleanField(
        db_column='bo_estado',
        default=True,
    )

    user_created = models.CharField(
        db_column='vc_id_usuario_creacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    user_modified = models.CharField(
        db_column='vc_id_usuario_modificacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        'date created at',
        auto_now_add=True,
        null=False,
        blank=False,
        db_column='ts_fecha_creacion',
        help_text='Date time on which the object was created.'
    )
    date_modified = models.DateTimeField(
        'date modified at',
        auto_now=True,
        null=True,
        blank=True,
        db_column='ts_fecha_modificacion',
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        db_table = 'gn_provincia'

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

    descripcion = models.CharField(
        db_column='vc_descripcion',
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

    ubigeo = models.CharField(
        db_column='vc_ubigeo',
        max_length=10,
        null=True,
        blank=True
    )

    status = models.BooleanField(
        db_column='bo_estado',
        default=True,
    )

    user_created = models.CharField(
        db_column='vc_id_usuario_creacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    user_modified = models.CharField(
        db_column='vc_id_usuario_modificacion',
        max_length=10,
        default='ROOT',
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        'date created at',
        auto_now_add=True,
        null=False,
        blank=False,
        db_column='ts_fecha_creacion',
        help_text='Date time on which the object was created.'
    )
    date_modified = models.DateTimeField(
        'date modified at',
        auto_now=True,
        null=True,
        blank=True,
        db_column='ts_fecha_modificacion',
        help_text='Date time on which the object was last modified.'
    )
    class Meta:
        db_table = 'gn_distrito'

