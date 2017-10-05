import unittest
from legoirblaster import core, exceptions


class CoreTestCase(unittest.TestCase):

    def test_send_command_should_raise_error(self):
        self.assertRaises(exceptions.LircError, core.send_command, '1')

    def test_command_creation_with_channel_1_output_r_brake_false_speed_0_returns_1r_0(self):
        self.assertEqual(core.create_command(1, 'R', 0, False), '1R_0')

    def test_command_creation_with_channel_1_output_r_brake_false_speed_1_returns_1r_1(self):
        self.assertEqual(core.create_command(1, 'R', 1, False), '1R_1')


if __name__ == '__main__':
    unittest.main()
