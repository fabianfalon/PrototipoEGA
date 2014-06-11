# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table(u'alumno_alumno')

        # Deleting model 'Carrera'
        db.delete_table(u'alumno_carrera')

        # Adding model 'User'
        db.create_table(u'alumno_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=50)),
            ('cod_alumno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre_apellido', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('dni', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('ciudad_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('domicilio_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('password1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipo_usuario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('documentacion_completa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'alumno', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'alumno_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'alumno.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'alumno_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'alumno.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])


    def backwards(self, orm):
        # Adding model 'Alumno'
        db.create_table(u'alumno_alumno', (
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('ciudad_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('tipo_usuario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('domicilio_actial', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumno.Carrera'])),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('documentacion_completa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre_apellido', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('cod_alumno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'alumno', ['Alumno'])

        # Adding model 'Carrera'
        db.create_table(u'alumno_carrera', (
            ('duracion', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_carrera', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'alumno', ['Carrera'])

        # Deleting model 'User'
        db.delete_table(u'alumno_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'alumno_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'alumno_user_user_permissions'))


    models = {
        u'alumno.user': {
            'Meta': {'object_name': 'User'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ciudad_actual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'cod_alumno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'documentacion_completa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'domicilio_actual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'nombre_apellido': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_usuario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['alumno']