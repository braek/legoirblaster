import unittest
from unittest.mock import MagicMock
import subprocess
from .. import core, exceptions


class CoreTestCase(unittest.TestCase):
    """
    Unit tests for the core of the Lego IR Blaster
    """
    def setUp(self):
        # Make backup of method that we are going to mock
        CoreTestCase.call_method_backup = subprocess.call

    def tearDown(self):
        # Put backup version of mocked method back
        subprocess.call = CoreTestCase.call_method_backup

    def test_send_command_should_not_raise_file_not_found_error(self):
        subprocess.call = MagicMock()
        self.assertIsNone(core.send_command('RANDOM_COMMAND'))

    def test_send_command_should_raise_file_not_found_error(self):
        subprocess.call = MagicMock(side_effect=FileNotFoundError)
        self.assertRaises(exceptions.LircError, core.send_command, 'RANDOM_COMMAND')

    def test_create_command_1r_m7(self):
        cmd = core.create_command(channel=1, output='R', speed=-7, brake=False)
        self.assertEqual(cmd, '1R_M7')

    def test_create_command_1r_m6(self):
        cmd = core.create_command(channel=1, output='R', speed=-6, brake=False)
        self.assertEqual(cmd, '1R_M6')

    def test_create_command_1r_m5(self):
        cmd = core.create_command(channel=1, output='R', speed=-5, brake=False)
        self.assertEqual(cmd, '1R_M5')

    def test_create_command_1r_m4(self):
        cmd = core.create_command(channel=1, output='R', speed=-4, brake=False)
        self.assertEqual(cmd, '1R_M4')

    def test_create_command_1r_m3(self):
        cmd = core.create_command(channel=1, output='R', speed=-3, brake=False)
        self.assertEqual(cmd, '1R_M3')

    def test_create_command_1r_m2(self):
        cmd = core.create_command(channel=1, output='R', speed=-2, brake=False)
        self.assertEqual(cmd, '1R_M2')

    def test_create_command_1r_m1(self):
        cmd = core.create_command(channel=1, output='R', speed=-1, brake=False)
        self.assertEqual(cmd, '1R_M1')

    def test_create_command_1r0(self):
        cmd = core.create_command(channel=1, output='R', speed=0, brake=False)
        self.assertEqual(cmd, '1R_0')

    def test_create_command_1r1(self):
        cmd = core.create_command(channel=1, output='R', speed=1, brake=False)
        self.assertEqual(cmd, '1R_1')

    def test_create_command_1r2(self):
        cmd = core.create_command(channel=1, output='R', speed=2, brake=False)
        self.assertEqual(cmd, '1R_2')

    def test_create_command_1r3(self):
        cmd = core.create_command(channel=1, output='R', speed=3, brake=False)
        self.assertEqual(cmd, '1R_3')

    def test_create_command_1r4(self):
        cmd = core.create_command(channel=1, output='R', speed=4, brake=False)
        self.assertEqual(cmd, '1R_4')

    def test_create_command_1r5(self):
        cmd = core.create_command(channel=1, output='R', speed=5, brake=False)
        self.assertEqual(cmd, '1R_5')

    def test_create_command_1r6(self):
        cmd = core.create_command(channel=1, output='R', speed=6, brake=False)
        self.assertEqual(cmd, '1R_6')

    def test_create_command_1r7(self):
        cmd = core.create_command(channel=1, output='R', speed=7, brake=False)
        self.assertEqual(cmd, '1R_7')

    def test_create_command_1r_brake(self):
        cmd = core.create_command(channel=1, output='R', speed=7, brake=True)
        self.assertEqual(cmd, '1R_BRAKE')
