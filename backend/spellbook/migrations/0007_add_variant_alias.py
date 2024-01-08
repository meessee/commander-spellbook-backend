# Generated by Django 5.0 on 2024-01-08 20:12

import django.core.validators
import django.db.models.deletion
import spellbook.models.variant_alias
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0006_variant_line_counts_and_nullable_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardincombo',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='cardincombo',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='cardincombo',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='cardincombo',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='cardinvariant',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='cardinvariant',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='cardinvariant',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='cardinvariant',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='cardusedinvariantsuggestion',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='cardusedinvariantsuggestion',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='cardusedinvariantsuggestion',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='cardusedinvariantsuggestion',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='description',
            field=models.TextField(blank=True, help_text='Long description of the combo, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='combo',
            name='other_prerequisites',
            field=models.TextField(blank=True, help_text='Other prerequisites for this combo.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(help_text='Short name for a produced effect', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Must start with a capital letter.', regex='^[A-Z]'), django.core.validators.RegexValidator(message='Must not end with punctuation.', regex='[A-Za-z0-9()\\{\\}]$'), django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='name of feature'),
        ),
        migrations.AlterField(
            model_name='featureproducedinvariantsuggestion',
            name='feature',
            field=models.CharField(help_text='Feature name', max_length=255, validators=[django.core.validators.RegexValidator(message='Must start with a capital letter.', regex='^[A-Z]'), django.core.validators.RegexValidator(message='Must not end with punctuation.', regex='[A-Za-z0-9()\\{\\}]$'), django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='feature name'),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(help_text='short description of the template in natural language', max_length=255, validators=[django.core.validators.RegexValidator(message='Must start with a capital letter.', regex='^[A-Z]'), django.core.validators.RegexValidator(message='Must not end with punctuation.', regex='[A-Za-z0-9()\\{\\}]$'), django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='template name'),
        ),
        migrations.AlterField(
            model_name='templateincombo',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='templateincombo',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='templateincombo',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='templateincombo',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='templateinvariant',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='templateinvariant',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='templateinvariant',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='templateinvariant',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='battlefield_card_state',
            field=models.CharField(blank=True, help_text='State of the card on the battlefield, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='battlefield starting card state'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='exile_card_state',
            field=models.CharField(blank=True, help_text='State of the card in exile, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='exile starting card state'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='graveyard_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the graveyard, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='graveyard starting card state'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='library_card_state',
            field=models.CharField(blank=True, help_text='State of the card in the library, if present.', max_length=200, validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='library starting card state'),
        ),
        migrations.AlterField(
            model_name='templaterequiredinvariantsuggestion',
            name='template',
            field=models.CharField(help_text='Template name', max_length=255, validators=[django.core.validators.RegexValidator(message='Must start with a capital letter.', regex='^[A-Z]'), django.core.validators.RegexValidator(message='Must not end with punctuation.', regex='[A-Za-z0-9()\\{\\}]$'), django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')], verbose_name='template name'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='description',
            field=models.TextField(blank=True, help_text='Long description, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='id',
            field=models.CharField(help_text='Unique ID for this variant', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='variant',
            name='other_prerequisites',
            field=models.TextField(blank=True, help_text='Other prerequisites for this variant.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='variantsuggestion',
            name='description',
            field=models.TextField(help_text='Long description, in steps', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='variantsuggestion',
            name='notes',
            field=models.TextField(blank=True, help_text='Notes written by editors', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.AlterField(
            model_name='variantsuggestion',
            name='other_prerequisites',
            field=models.TextField(blank=True, help_text='Other prerequisites for this variant.', validators=[django.core.validators.RegexValidator(message='Unpaired double square brackets are not allowed.', regex='^(?:[^\\[]*(?:\\[(?!\\[)|\\[{2}[^\\[]+\\]{2}|\\[{3,}))*[^\\[]*$'), django.core.validators.RegexValidator(message='Symbols must be in the {1}{W}{U}{B}{R}{G}{B/P}{A}{E}{T}{Q}... format.', regex='^(?:[^\\{]*\\{(?:(?:2\\/[WUBRG]|W\\/U|W\\/B|B\\/R|B\\/G|U\\/B|U\\/R|R\\/G|R\\/W|G\\/W|G\\/U)(?:\\/P)?|CHAOS|PW|TK|[WUBRG](?:\\/P)?|[1-9][0-9]{1,2}|H[WUBRG]|[0-9CPXYZSTQEA½∞])\\})*[^\\{]*$'), django.core.validators.RegexValidator(message='Only ordinary characters are allowed.', regex='^[\\x0A\\x0D\\x20-\\x7E\\x80\\x95\\x99\\xA1\\xA9\\xAE\\xB0\\xB1-\\xB3\\xBC-\\xFF]*$')]),
        ),
        migrations.CreateModel(
            name='VariantAlias',
            fields=[
                ('id', models.CharField(help_text='Unique id of this variant alias', max_length=128, primary_key=True, serialize=False, validators=[spellbook.models.variant_alias.no_variant_with_this_id])),
                ('description', models.TextField(blank=True, help_text='Description of this variant alias')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aliases', to='spellbook.variant')),
            ],
            options={
                'verbose_name': 'variant alias',
                'verbose_name_plural': 'variant aliases',
            },
        ),
    ]
