# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrera'
        db.create_table(u'alumno_carrera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_carrera', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('duracion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'alumno', ['Carrera'])

        # Adding model 'Alumno'
        db.create_table(u'alumno_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_alumno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumno.Carrera'])),
            ('nombre_apellido', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('ciudad_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('domicilio_actial', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('usuario', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tipo_usuario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('documentacion_completa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'alumno', ['Alumno'])


    def backwards(self, orm):
        # Deleting model 'Carrera'
        db.delete_table(u'alumno_carrera')

        # Deleting model 'Alumno'
        db.delete_table(u'alumno_alumno')


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
            'tipo_usuario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'alumno.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'cod_carrera': ('django.db.models.fields.IntegerField', [], {}),
            'duracion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['alumno']