import unittest
from portal.energy import fix_wiring


class TestFixWiring(unittest.TestCase):
    def test_default(self):
        plugs = ['plug1', 'plug2', 'plug3']
        sockets = ['socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable1', 'cable2', 'cable3', 'cable4']
        result = ['plug cable1 into socket1 using plug1',
                  'plug cable2 into socket2 using plug2',
                  'plug cable3 into socket3 using plug3',
                  'weld cable4 to socket4 without plug']
        self.assertEqual(result, list(fix_wiring(cables, sockets, plugs)))

    def test_none(self):
        plugs = ['plugZ', None, 'plugY', 'plugX']
        sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable2', 'cable1', False]
        result = ['plug cable2 into socket1 using plugZ',
                  'plug cable1 into socket2 using plugY']
        self.assertEqual(result, list(fix_wiring(cables, sockets, plugs)))

    def test_two_cables(self):
        plugs = ['plug1', 'plug2', 'plug3', 'plug4']
        sockets = ['socket1', 'socket2', 'socket3']
        cables = ['cable1', 'cable2']
        result = ['plug cable1 into socket1 using plug1',
                  'plug cable2 into socket2 using plug2']
        self.assertEqual(result, list(fix_wiring(cables, sockets, plugs)))

    def test_four_sockets(self):
        plugs = ['plug1', 'plug2', 'plug3', 'plug4']
        sockets = ['socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable1', 'cable2', 'cable3']
        result = ['plug cable1 into socket1 using plug1',
                  'plug cable2 into socket2 using plug2',
                  'plug cable3 into socket3 using plug3']
        self.assertEqual(result, list(fix_wiring(cables, sockets, plugs)))


if __name__ == '__main__':
    unittest.main()
