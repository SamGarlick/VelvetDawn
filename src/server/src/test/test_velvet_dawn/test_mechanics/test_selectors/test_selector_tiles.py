import velvet_dawn.map.creation
from velvet_dawn.dao import app
from test.base_test import BaseTest
from velvet_dawn.dao.models.world_instance import WorldInstance
from velvet_dawn.mechanics import selectors


class TestTileSelectors(BaseTest):

    def test_selector_tile(self):
        with app.app_context():
            self.setup_game()

            unit = velvet_dawn.units.get_unit_at_position(15, 0)
            tile = velvet_dawn.map.get_tile(15, 0)

            selector = selectors.get_selector(unit.entity_id, "tile")
            selector_tiles = selectors.get_selector(unit.entity_id, "tiles")
            self.assertTrue(isinstance(selector, selectors.SelectorTile))
            self.assertTrue(isinstance(selector_tiles, selectors.SelectorTiles))

            one_tile_from_unit = selector.get_selection(unit)
            one_tile_from_tile = selector.get_selection(tile)
            one_tile_from_world = selector.get_selection(WorldInstance())
            self.assertEqual(1, len(one_tile_from_unit))
            self.assertEqual(1, len(one_tile_from_tile))
            self.assertEqual(0, len(one_tile_from_world))
            self.assertEqual(tile.id, one_tile_from_unit[0].id)
            self.assertEqual(tile.id, one_tile_from_tile[0].id)

            self.assertEqual(589, len(selector_tiles.get_selection(unit)))
            self.assertEqual(589, len(selector_tiles.get_selection(tile)))
            self.assertEqual(589, len(selector_tiles.get_selection(WorldInstance())))
