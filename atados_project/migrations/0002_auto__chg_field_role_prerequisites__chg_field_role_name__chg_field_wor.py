# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Role.prerequisites'
        db.alter_column(u'atados_project_role', 'prerequisites', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True))

        # Changing field 'Role.name'
        db.alter_column(u'atados_project_role', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Work.project'
        db.alter_column(u'atados_project_work', 'project_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['atados_project.Project'], unique=True))
        # Adding unique constraint on 'Work', fields ['project']
        db.create_unique(u'atados_project_work', ['project_id'])


        # Changing field 'Work.address'
        db.alter_column(u'atados_project_work', 'address_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['atados_core.Address'], unique=True))
        # Adding unique constraint on 'Work', fields ['address']
        db.create_unique(u'atados_project_work', ['address_id'])

        # Adding field 'Project.closed'
        db.add_column(u'atados_project_project', 'closed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Donation.project'
        db.alter_column(u'atados_project_donation', 'project_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['atados_project.Project'], unique=True))
        # Adding unique constraint on 'Donation', fields ['project']
        db.create_unique(u'atados_project_donation', ['project_id'])


        # Changing field 'Donation.delivery'
        db.alter_column(u'atados_project_donation', 'delivery_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['atados_core.Address'], unique=True))
        # Adding unique constraint on 'Donation', fields ['delivery']
        db.create_unique(u'atados_project_donation', ['delivery_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Donation', fields ['delivery']
        db.delete_unique(u'atados_project_donation', ['delivery_id'])

        # Removing unique constraint on 'Donation', fields ['project']
        db.delete_unique(u'atados_project_donation', ['project_id'])

        # Removing unique constraint on 'Work', fields ['address']
        db.delete_unique(u'atados_project_work', ['address_id'])

        # Removing unique constraint on 'Work', fields ['project']
        db.delete_unique(u'atados_project_work', ['project_id'])


        # User chose to not deal with backwards NULL issues for 'Role.prerequisites'
        raise RuntimeError("Cannot reverse this migration. 'Role.prerequisites' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Role.name'
        raise RuntimeError("Cannot reverse this migration. 'Role.name' and its values cannot be restored.")

        # Changing field 'Work.project'
        db.alter_column(u'atados_project_work', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_project.Project']))

        # Changing field 'Work.address'
        db.alter_column(u'atados_project_work', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_core.Address']))
        # Deleting field 'Project.closed'
        db.delete_column(u'atados_project_project', 'closed')


        # Changing field 'Donation.project'
        db.alter_column(u'atados_project_donation', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_project.Project']))

        # Changing field 'Donation.delivery'
        db.alter_column(u'atados_project_donation', 'delivery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atados_core.Address']))

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
        },
        u'atados_nonprofit.nonprofit': {
            'Meta': {'object_name': 'Nonprofit'},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['atados_core.Address']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['atados_core.Cause']", 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'atados_project.apply': {
            'Meta': {'object_name': 'Apply'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_project.Project']"}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_volunteer.Volunteer']"})
        },
        u'atados_project.donation': {
            'Meta': {'object_name': 'Donation'},
            'collection_by_nonprofit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delivery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['atados_core.Address']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['atados_project.Project']", 'unique': 'True'})
        },
        u'atados_project.project': {
            'Meta': {'object_name': 'Project'},
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['atados_core.Cause']", 'symmetrical': 'False'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nonprofit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_nonprofit.Nonprofit']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'atados_project.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'vacancies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['atados_project.Work']"})
        },
        u'atados_project.work': {
            'Meta': {'object_name': 'Work'},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['atados_core.Address']", 'unique': 'True'}),
            'availabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['atados_core.Availability']", 'symmetrical': 'False'}),
            'can_be_done_remotely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['atados_project.Project']", 'unique': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['atados_core.Skill']", 'symmetrical': 'False'}),
            'weekly_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'atados_volunteer.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            'addressline': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressnumber': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['atados_core.Cause']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['atados_core.Skill']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.State']", 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['atados_core.Suburb']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'})
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['atados_project']