# Generated by Django 4.1 on 2022-10-01 22:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0002_alter_combo_cards_state_alter_combo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='identity',
            field=models.CharField(blank=True, help_text='Card mana identity', max_length=5, validators=[django.core.validators.RegexValidator(message='Can be any combination of zero or more letters in [W,U,B,R,G], in order.', regex='^W?U?B?R?G?$')], verbose_name='mana identity of card'),
        ),
        migrations.AddField(
            model_name='variant',
            name='identity',
            field=models.CharField(blank=True, editable=False, help_text='Mana identity', max_length=5, validators=[django.core.validators.RegexValidator(message='Can be any combination of zero or more letters in [W,U,B,R,G], in order.', regex='^W?U?B?R?G?$')], verbose_name='mana identity'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='description',
            field=models.TextField(blank=True, help_text='Long description, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:[0-9WUBRGCPXYZSTQEA½∞]|PW|CHAOS|TK|[1-9][0-9]{1,2}|H[WUBRG]|(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?)\\})*[^\\{]*$')]),
        ),
    ]
