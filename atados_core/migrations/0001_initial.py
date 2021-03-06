# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Availability'
        db.create_table(u'atados_core_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weekday', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('period', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'atados_core', ['Availability'])

        # Adding model 'Cause'
        db.create_table(u'atados_core_cause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'atados_core', ['Cause'])

        # Adding model 'Skill'
        db.create_table(u'atados_core_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'atados_core', ['Skill'])

        # Adding model 'State'
        db.create_table(u'atados_core_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'atados_core', ['State'])

        # Adding model 'City'
        db.create_table(u'atados_core_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_core.State'])),
        ))
        db.send_create_signal(u'atados_core', ['City'])

        # Adding model 'Suburb'
        db.create_table(u'atados_core_suburb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_core.City'])),
        ))
        db.send_create_signal(u'atados_core', ['Suburb'])

        # Adding model 'Address'
        db.create_table(u'atados_core_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('addressline', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('addressnumber', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['atados_core.State'], null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['atados_core.City'], null=True, blank=True)),
            ('suburb', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['atados_core.Suburb'], null=True, blank=True)),
        ))
        db.send_create_signal(u'atados_core', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Availability'
        db.delete_table(u'atados_core_availability')

        # Deleting model 'Cause'
        db.delete_table(u'atados_core_cause')

        # Deleting model 'Skill'
        db.delete_table(u'atados_core_skill')

        # Deleting model 'State'
        db.delete_table(u'atados_core_state')

        # Deleting model 'City'
        db.delete_table(u'atados_core_city')

        # Deleting model 'Suburb'
        db.delete_table(u'atados_core_suburb')

        # Deleting model 'Address'
        db.delete_table(u'atados_core_address')


    models = {
        u'atados_core.address': {
            'Meta': {'object_name': 'Address'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressnumber': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.State']", 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.Suburb']", 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'atados_core.availability': {
            'Meta': {'object_name': 'Availability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'weekday': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'atados_core.cause': {
            'Meta': {'object_name': 'Cause'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'atados_core.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_core.State']"})
        },
        u'atados_core.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'atados_core.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'atados_core.suburb': {
            'Meta': {'object_name': 'Suburb'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_core.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['atados_core']