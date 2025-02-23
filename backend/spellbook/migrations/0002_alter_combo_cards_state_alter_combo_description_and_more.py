# Generated by Django 4.1 on 2022-09-30 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='cards_state',
            field=models.TextField(blank=True, default='', help_text='State of cards in their starting locations.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')], verbose_name='starting cards state'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='description',
            field=models.TextField(blank=True, help_text='Long description of the combo, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')]),
        ),
        migrations.AlterField(
            model_name='combo',
            name='mana_needed',
            field=models.CharField(blank=True, default='', help_text='Mana needed for this combo. Use the {1}{W}{U}{B}{R}{G}{B/P}... format.', max_length=200, validators=[django.core.validators.RegexValidator(message='Mana needed must be in the {1}{W}{U}{B}{R}{G}{B/P}... format.', regex='^(\\{(?:[0-9WUBRGCPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\} *)*$')]),
        ),
        migrations.AlterField(
            model_name='combo',
            name='other_prerequisites',
            field=models.TextField(blank=True, default='', help_text='Other prerequisites for this combo.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')]),
        ),
        migrations.AlterField(
            model_name='combo',
            name='zone_locations',
            field=models.TextField(blank=True, default='', help_text='Starting locations for cards.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')], verbose_name='starting locations'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='cards_state',
            field=models.TextField(blank=True, default='', help_text='State of cards in their starting locations.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')], verbose_name='starting cards state'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='description',
            field=models.TextField(blank=True, help_text='Long description of the variant, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='mana_needed',
            field=models.CharField(blank=True, default='', help_text='Mana needed for this combo. Use the {1}{W}{U}{B}{R}{G}{B/P}... format.', max_length=200, validators=[django.core.validators.RegexValidator(message='Mana needed must be in the {1}{W}{U}{B}{R}{G}{B/P}... format.', regex='^(\\{(?:[0-9WUBRGCPXYZS∞]|[1-9][0-9]{1,2}|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\} *)*$')]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='other_prerequisites',
            field=models.TextField(blank=True, default='', help_text='Other prerequisites for this variant.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='zone_locations',
            field=models.TextField(blank=True, default='', help_text='Starting locations for cards.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')], verbose_name='starting locations'),
        ),
    ]
