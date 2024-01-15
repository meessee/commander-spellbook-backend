# Generated by Django 5.0.1 on 2024-01-14 14:19

import imp
import django.contrib.postgres.indexes
from django.db import migrations, models
from spellbook.models import Variant as NewVariant
from spellbook.serializers import VariantSerializer
try:
    imp.find_module('psycopg2')
    psycopg2 = True
except ImportError:
    psycopg2 = False
if psycopg2:
    from django.contrib.postgres.operations import BtreeGinExtension
    extra_operations = [BtreeGinExtension()]
else:
    extra_operations = []


def preserialize_variants(apps, schema_editor):
    Variant = apps.get_model('spellbook', 'Variant')
    Feature = apps.get_model('spellbook', 'Feature')
    variants = list[Variant](Variant.objects
        .filter(status__in=NewVariant.public_statuses())
        .prefetch_related(
            'cardinvariant_set__card',
            'templateinvariant_set__template',
            'cardinvariant_set',
            'templateinvariant_set',
            models.Prefetch('produces', queryset=Feature.objects.filter(utility=False)),
            'of',
            'includes'
        )
    )
    for variant in variants:
        variant.serialized = VariantSerializer(variant).data  # type: ignore
    Variant.objects.bulk_update(variants, fields=['serialized'], batch_size=5000)


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0008_alter_card_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='serialized',
            field=models.JSONField(blank=True, editable=False, null=True),
        ),
        migrations.RunPython(
            preserialize_variants,
            reverse_code=migrations.RunPython.noop,
        ),
        *extra_operations,
        migrations.AddIndex(
            model_name='card',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'name_unaccented', 'name_unaccented_simplified', 'name_unaccented_simplified_with_spaces'], name='spellbook_c_name_037e1e_gin'),
        ),
        migrations.AddIndex(
            model_name='card',
            index=django.contrib.postgres.indexes.GinIndex(fields=['type_line'], name='spellbook_c_type_li_155b2b_gin'),
        ),
        migrations.AddIndex(
            model_name='card',
            index=django.contrib.postgres.indexes.GinIndex(fields=['oracle_text'], name='spellbook_c_oracle__78c83a_gin'),
        ),
        migrations.AddIndex(
            model_name='card',
            index=django.contrib.postgres.indexes.GinIndex(fields=['keywords'], name='spellbook_c_keyword_c42092_gin'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='spellbook_f_name_fedfaa_gin'),
        ),
        migrations.AddIndex(
            model_name='variant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['other_prerequisites'], name='spellbook_v_other_p_4121cc_gin'),
        ),
        migrations.AddIndex(
            model_name='variant',
            index=django.contrib.postgres.indexes.GinIndex(fields=['description'], name='spellbook_v_descrip_26b373_gin'),
        ),
    ]
