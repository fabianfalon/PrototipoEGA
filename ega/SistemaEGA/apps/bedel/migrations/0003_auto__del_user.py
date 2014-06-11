# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'bedel_user')

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'bedel_user_user_permissions'))

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'bedel_user_groups'))


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'bedel_user', (
            ('ciudad_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('domicilio_actual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('perfil', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, unique=True)),
            ('cod_alumno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tipo_usuario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('apellido_nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('documentacion_completa', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bedel', ['User'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'bedel_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'bedel.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'bedel_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'bedel.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])


    models = {
        
    }

    complete_apps = ['bedel']