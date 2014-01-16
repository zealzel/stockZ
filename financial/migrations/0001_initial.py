# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prices'
        db.create_table(u'financial_prices', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('total_stock', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_price', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('p_begin', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('p_max', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('p_min', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('p_end', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('p_diff', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'financial', ['Prices'])


    def backwards(self, orm):
        # Deleting model 'Prices'
        db.delete_table(u'financial_prices')


    models = {
        u'financial.prices': {
            'Meta': {'object_name': 'Prices'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_begin': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'p_diff': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'p_end': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'p_max': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'p_min': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'total_price': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'total_stock': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['financial']