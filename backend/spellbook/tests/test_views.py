import json
from types import SimpleNamespace
from django.test import Client
from django.core.management import call_command
from spellbook.utils import launch_job_command
from spellbook.models import Card, Feature, Template, Combo, CardInCombo, TemplateInCombo, Variant, CardInVariant, TemplateInVariant
from .abstract_test import AbstractModelTests
from website.models import PROPERTY_KEYS


json_to_python_lambda = lambda d: SimpleNamespace(**d)


class CardViewsTests(AbstractModelTests):
    def card_assertions(self, card_result):
        c = Card.objects.get(id=card_result.id)
        self.assertEqual(card_result.id, c.id)
        self.assertEqual(card_result.name, c.name)
        self.assertEqual(card_result.oracle_id, str(c.oracle_id))
        self.assertEqual(card_result.identity, c.identity)
        self.assertEqual(card_result.legal, c.legal)
        self.assertEqual(card_result.spoiler, c.spoiler)
        self.assertEqual(len(card_result.features), c.features.count())
        feature_list = [f.id for f in c.features.all()]
        for f in card_result.features:
            self.assertIn(f.id, feature_list)

    def test_cards_list_view(self):
        c = Client()
        response = c.get('/cards', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        cards_count = Card.objects.count()
        self.assertEqual(len(result.results), cards_count)
        for i in range(cards_count):
            self.card_assertions(result.results[i])

    def test_cards_detail_view(self):
        c = Client()
        response = c.get('/cards/{}'.format(self.c1_id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(result.id, self.c1_id)
        self.card_assertions(result)


class FeatureViewsTests(AbstractModelTests):
    def feature_assertions(self, feature_result):
        f = Feature.objects.get(id=feature_result.id)
        self.assertEqual(feature_result.id, f.id)
        self.assertEqual(feature_result.name, f.name)
        self.assertEqual(feature_result.description, f.description)
        self.assertEqual(feature_result.utility, f.utility)

    def test_features_list_view(self):
        c = Client()
        response = c.get('/features', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        features_count = Feature.objects.count()
        self.assertEqual(len(result.results), features_count)
        for i in range(features_count):
            self.feature_assertions(result.results[i])

    def test_features_detail_view(self):
        c = Client()
        response = c.get('/features/{}'.format(self.f1_id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(result.id, self.f1_id)
        self.feature_assertions(result)


class TemplateViewsTests(AbstractModelTests):
    def template_assertions(self, template_result):
        t = Template.objects.get(id=template_result.id)
        self.assertEqual(template_result.id, t.id)
        self.assertEqual(template_result.name, t.name)
        self.assertEqual(template_result.scryfall_query, t.scryfall_query)
        self.assertEqual(template_result.scryfall_api, t.scryfall_api())

    def test_templates_list_view(self):
        c = Client()
        response = c.get('/templates', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        templates_count = Template.objects.count()
        self.assertEqual(len(result.results), templates_count)
        for i in range(templates_count):
            self.template_assertions(result.results[i])

    def test_templates_detail_view(self):
        c = Client()
        response = c.get('/templates/{}'.format(self.t1_id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(result.id, self.t1_id)
        self.template_assertions(result)


class ComboViewsTests(AbstractModelTests):
    def combo_assertions(self, combo_result):
        b = Combo.objects.get(id=combo_result.id)
        self.assertEqual(combo_result.id, b.id)
        self.assertEqual(combo_result.mana_needed, b.mana_needed)
        self.assertEqual(combo_result.other_prerequisites, b.other_prerequisites)
        self.assertEqual(combo_result.description, b.description)
        self.assertEqual(len(combo_result.requires), b.requires.count())
        produces_list = [p.id for p in b.produces.all()]
        for p in combo_result.produces:
            self.assertIn(p.id, produces_list)
            f = Feature.objects.get(id=p.id)
            self.assertEqual(p.name, f.name)
            self.assertEqual(p.description, f.description)
            self.assertEqual(p.utility, f.utility)
        needs_list = [n.id for n in b.needs.all()]
        for n in combo_result.needs:
            self.assertIn(n.id, needs_list)
            f = Feature.objects.get(id=n.id)
            self.assertEqual(n.name, f.name)
            self.assertEqual(n.description, f.description)
            self.assertEqual(n.utility, f.utility)
        uses_list = [u.id for u in b.uses.all()]
        for u in combo_result.uses:
            card = u.card
            self.assertIn(card.id, uses_list)
            c = Card.objects.get(id=card.id)
            self.assertEqual(card.id, c.id)
            self.assertEqual(card.name, c.name)
            self.assertEqual(card.oracle_id, str(c.oracle_id))
            self.assertEqual(card.identity, c.identity)
            self.assertEqual(card.legal, c.legal)
            self.assertEqual(card.spoiler, c.spoiler)
            cic = CardInCombo.objects.get(combo=b.id, card=c)
            self.assertEqual(set(u.zone_locations), set(cic.zone_locations))
            self.assertEqual(u.card_state, cic.card_state)
        requires_list = [r.id for r in b.requires.all()]
        for r in combo_result.requires:
            template = r.template
            self.assertIn(template.id, requires_list)
            t = Template.objects.get(id=template.id)
            self.assertEqual(template.id, t.id)
            self.assertEqual(template.name, t.name)
            self.assertEqual(template.scryfall_query, t.scryfall_query)
            self.assertEqual(template.scryfall_api, t.scryfall_api())
            tic = TemplateInCombo.objects.get(combo=b.id, template=t)
            self.assertEqual(set(r.zone_locations), set(tic.zone_locations))
            self.assertEqual(r.card_state, tic.card_state)

    def test_combos_list_view(self):
        c = Client()
        response = c.get('/combos', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        combos_count = Combo.objects.count()
        self.assertEqual(len(result.results), combos_count)
        for i in range(combos_count):
            self.combo_assertions(result.results[i])

    def test_combos_detail_view(self):
        c = Client()
        response = c.get('/combos/{}'.format(self.c1_id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(result.id, self.c1_id)
        self.combo_assertions(result)


class VariantViewsTests(AbstractModelTests):
    def setUp(self) -> None:
        super().setUp()
        launch_job_command('generate_variants', None)
        Variant.objects.update(status=Variant.Status.OK)
        self.v1_id = Variant.objects.first().id

    def variant_assertions(self, variant_result):
        v = Variant.objects.get(id=variant_result.id)
        self.assertEqual(variant_result.id, v.id)
        self.assertEqual(variant_result.identity, v.identity)
        self.assertEqual(variant_result.mana_needed, v.mana_needed)
        self.assertEqual(variant_result.other_prerequisites, v.other_prerequisites)
        self.assertEqual(variant_result.description, v.description)
        self.assertEqual(variant_result.legal, v.legal)
        self.assertEqual(variant_result.spoiler, v.spoiler)
        uses_list = [u.id for u in v.uses.all()]
        for u in variant_result.uses:
            card = u.card
            self.assertIn(card.id, uses_list)
            c = Card.objects.get(id=card.id)
            self.assertEqual(card.id, c.id)
            self.assertEqual(card.name, c.name)
            self.assertEqual(card.oracle_id, str(c.oracle_id))
            self.assertEqual(card.identity, c.identity)
            self.assertEqual(card.legal, c.legal)
            self.assertEqual(card.spoiler, c.spoiler)
            vic = CardInVariant.objects.get(variant=v.id, card=c)
            self.assertEqual(set(u.zone_locations), set(vic.zone_locations))
            self.assertEqual(u.card_state, vic.card_state)
        requires_list = [r.id for r in v.requires.all()]
        for r in variant_result.requires:
            template = r.template
            self.assertIn(template.id, requires_list)
            t = Template.objects.get(id=template.id)
            self.assertEqual(template.id, t.id)
            self.assertEqual(template.name, t.name)
            self.assertEqual(template.scryfall_query, t.scryfall_query)
            self.assertEqual(template.scryfall_api, t.scryfall_api())
            tiv = TemplateInVariant.objects.get(variant=v.id, template=t)
            self.assertEqual(set(r.zone_locations), set(tiv.zone_locations))
            self.assertEqual(r.card_state, tiv.card_state)
        produces_list = [p.id for p in v.produces.all()]
        for p in variant_result.produces:
            self.assertIn(p.id, produces_list)
            f = Feature.objects.get(id=p.id)
            self.assertEqual(p.id, f.id)
            self.assertEqual(p.name, f.name)
            self.assertEqual(p.utility, f.utility)
            self.assertEqual(p.description, f.description)
        of_list = [o.id for o in v.of.all()]
        for o in variant_result.of:
            self.assertIn(o.id, of_list)
        includes_list = [i.id for i in v.includes.all()]
        for i in variant_result.includes:
            self.assertIn(i.id, includes_list)

    def test_variants_list_view(self):
        c = Client()
        response = c.get('/variants', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        variants_count = Variant.objects.count()
        self.assertEqual(len(result.results), variants_count)
        for i in range(variants_count):
            self.variant_assertions(result.results[i])

    def test_variants_detail_view(self):
        c = Client()
        response = c.get('/variants/{}'.format(self.v1_id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(result.id, self.v1_id)
        self.variant_assertions(result)


class WebsitePropertiesViewTests(AbstractModelTests):
    def setUp(self):
        super().setUp()
        call_command('seed_website_properties')

    def test_website_properties_view(self):
        c = Client()
        response = c.get('/properties', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Type'), 'application/json')
        result = json.loads(response.content, object_hook=json_to_python_lambda)
        self.assertEqual(len(result.results), len(PROPERTY_KEYS))
        result_keys = {r.key for r in result.results}
        self.assertEqual(result_keys, set(PROPERTY_KEYS))
