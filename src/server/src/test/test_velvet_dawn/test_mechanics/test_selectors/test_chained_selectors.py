import velvet_dawn.units
from test.base_test import BaseTest
from velvet_dawn.dao import app
from velvet_dawn.mechanics import selectors


class TestChainedSelectors(BaseTest):

    def test_selector_parsing(self):
        selector = selectors.get_selector("0", "world>units>commanders>closest-unit.max.health.example")

        self.assertIsInstance(selector, selectors.SelectorWorld)
        self.assertIsInstance(selector.chained_selector, selectors.SelectorUnits)
        self.assertIsInstance(selector.chained_selector.chained_selector, selectors.SelectorCommanders)
        self.assertIsInstance(selector.chained_selector.chained_selector.chained_selector, selectors.SelectorClosest)

        self.assertEqual(selector.attribute, "max.health.example")

    def test_chained_selectors(self):
        with app.app_context():
            self.setup_game()

            selector = selectors.get_selector("0", "world>units>commander>tile.max.health.example")

            tiles = selector.get_chained_selection(velvet_dawn.units.get_unit_at_position(15, 0))

            # 3 units with two commanders each on 1 tile results in 2 tiles
            self.assertEqual(2, len(tiles))
