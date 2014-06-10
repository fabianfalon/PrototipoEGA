# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Alumno.password'
        db.add_column(u'alumno_alumno', 'password',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Alumno.password'
        db.delete_column(u'alumno_alumno', 'password')


    models = {
        u'alumno.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumno.Carrera']"}),
            'ciudad_actual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'cod_alumno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'documentacion_completa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'domicilio_actial': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'nombre_apellido': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo_usuario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'alumno.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'cod_materia': ('django.db.models.fields.IntegerField', [], {}),
            'duracion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['alumno']