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

    def test_create_command_1r_0(self):
        cmd = core.create_command(channel=1, output='R', speed=0, brake=False)
        self.assertEqual(cmd, '1R_0')

    def test_create_command_1r_1(self):
        cmd = core.create_command(channel=1, output='R', speed=1, brake=False)
        self.assertEqual(cmd, '1R_1')

    def test_create_command_1r_2(self):
        cmd = core.create_command(channel=1, output='R', speed=2, brake=False)
        self.assertEqual(cmd, '1R_2')

    def test_create_command_1r_3(self):
        cmd = core.create_command(channel=1, output='R', speed=3, brake=False)
        self.assertEqual(cmd, '1R_3')

    def test_create_command_1r_4(self):
        cmd = core.create_command(channel=1, output='R', speed=4, brake=False)
        self.assertEqual(cmd, '1R_4')

    def test_create_command_1r_5(self):
        cmd = core.create_command(channel=1, output='R', speed=5, brake=False)
        self.assertEqual(cmd, '1R_5')

    def test_create_command_1r_6(self):
        cmd = core.create_command(channel=1, output='R', speed=6, brake=False)
        self.assertEqual(cmd, '1R_6')

    def test_create_command_1r_7(self):
        cmd = core.create_command(channel=1, output='R', speed=7, brake=False)
        self.assertEqual(cmd, '1R_7')

    def test_create_command_1r_brake(self):
        cmd = core.create_command(channel=1, output='R', speed=7, brake=True)
        self.assertEqual(cmd, '1R_BRAKE')

    def test_create_command_2r_m7(self):
        cmd = core.create_command(channel=2, output='R', speed=-7, brake=False)
        self.assertEqual(cmd, '2R_M7')

    def test_create_command_2r_m6(self):
        cmd = core.create_command(channel=2, output='R', speed=-6, brake=False)
        self.assertEqual(cmd, '2R_M6')

    def test_create_command_2r_m5(self):
        cmd = core.create_command(channel=2, output='R', speed=-5, brake=False)
        self.assertEqual(cmd, '2R_M5')

    def test_create_command_2r_m4(self):
        cmd = core.create_command(channel=2, output='R', speed=-4, brake=False)
        self.assertEqual(cmd, '2R_M4')

    def test_create_command_2r_m3(self):
        cmd = core.create_command(channel=2, output='R', speed=-3, brake=False)
        self.assertEqual(cmd, '2R_M3')

    def test_create_command_2r_m2(self):
        cmd = core.create_command(channel=2, output='R', speed=-2, brake=False)
        self.assertEqual(cmd, '2R_M2')

    def test_create_command_2r_m1(self):
        cmd = core.create_command(channel=2, output='R', speed=-1, brake=False)
        self.assertEqual(cmd, '2R_M1')

    def test_create_command_2r_0(self):
        cmd = core.create_command(channel=2, output='R', speed=0, brake=False)
        self.assertEqual(cmd, '2R_0')

    def test_create_command_2r_1(self):
        cmd = core.create_command(channel=2, output='R', speed=1, brake=False)
        self.assertEqual(cmd, '2R_1')

    def test_create_command_2r_2(self):
        cmd = core.create_command(channel=2, output='R', speed=2, brake=False)
        self.assertEqual(cmd, '2R_2')

    def test_create_command_2r_3(self):
        cmd = core.create_command(channel=2, output='R', speed=3, brake=False)
        self.assertEqual(cmd, '2R_3')

    def test_create_command_2r_4(self):
        cmd = core.create_command(channel=2, output='R', speed=4, brake=False)
        self.assertEqual(cmd, '2R_4')

    def test_create_command_2r_5(self):
        cmd = core.create_command(channel=2, output='R', speed=5, brake=False)
        self.assertEqual(cmd, '2R_5')

    def test_create_command_2r_6(self):
        cmd = core.create_command(channel=2, output='R', speed=6, brake=False)
        self.assertEqual(cmd, '2R_6')

    def test_create_command_2r_7(self):
        cmd = core.create_command(channel=2, output='R', speed=7, brake=False)
        self.assertEqual(cmd, '2R_7')

    def test_create_command_2r_brake(self):
        cmd = core.create_command(channel=2, output='R', speed=7, brake=True)
        self.assertEqual(cmd, '2R_BRAKE')

    def test_create_command_3r_m7(self):
        cmd = core.create_command(channel=3, output='R', speed=-7, brake=False)
        self.assertEqual(cmd, '3R_M7')

    def test_create_command_3r_m6(self):
        cmd = core.create_command(channel=3, output='R', speed=-6, brake=False)
        self.assertEqual(cmd, '3R_M6')

    def test_create_command_3r_m5(self):
        cmd = core.create_command(channel=3, output='R', speed=-5, brake=False)
        self.assertEqual(cmd, '3R_M5')

    def test_create_command_3r_m4(self):
        cmd = core.create_command(channel=3, output='R', speed=-4, brake=False)
        self.assertEqual(cmd, '3R_M4')

    def test_create_command_3r_m3(self):
        cmd = core.create_command(channel=3, output='R', speed=-3, brake=False)
        self.assertEqual(cmd, '3R_M3')

    def test_create_command_3r_m2(self):
        cmd = core.create_command(channel=3, output='R', speed=-2, brake=False)
        self.assertEqual(cmd, '3R_M2')

    def test_create_command_3r_m1(self):
        cmd = core.create_command(channel=3, output='R', speed=-1, brake=False)
        self.assertEqual(cmd, '3R_M1')

    def test_create_command_3r_0(self):
        cmd = core.create_command(channel=3, output='R', speed=0, brake=False)
        self.assertEqual(cmd, '3R_0')

    def test_create_command_3r_1(self):
        cmd = core.create_command(channel=3, output='R', speed=1, brake=False)
        self.assertEqual(cmd, '3R_1')

    def test_create_command_3r_2(self):
        cmd = core.create_command(channel=3, output='R', speed=2, brake=False)
        self.assertEqual(cmd, '3R_2')

    def test_create_command_3r_3(self):
        cmd = core.create_command(channel=3, output='R', speed=3, brake=False)
        self.assertEqual(cmd, '3R_3')

    def test_create_command_3r_4(self):
        cmd = core.create_command(channel=3, output='R', speed=4, brake=False)
        self.assertEqual(cmd, '3R_4')

    def test_create_command_3r_5(self):
        cmd = core.create_command(channel=3, output='R', speed=5, brake=False)
        self.assertEqual(cmd, '3R_5')

    def test_create_command_3r_6(self):
        cmd = core.create_command(channel=3, output='R', speed=6, brake=False)
        self.assertEqual(cmd, '3R_6')

    def test_create_command_3r_7(self):
        cmd = core.create_command(channel=3, output='R', speed=7, brake=False)
        self.assertEqual(cmd, '3R_7')

    def test_create_command_3r_brake(self):
        cmd = core.create_command(channel=3, output='R', speed=7, brake=True)
        self.assertEqual(cmd, '3R_BRAKE')

    def test_create_command_4r_m7(self):
        cmd = core.create_command(channel=4, output='R', speed=-7, brake=False)
        self.assertEqual(cmd, '4R_M7')

    def test_create_command_4r_m6(self):
        cmd = core.create_command(channel=4, output='R', speed=-6, brake=False)
        self.assertEqual(cmd, '4R_M6')

    def test_create_command_4r_m5(self):
        cmd = core.create_command(channel=4, output='R', speed=-5, brake=False)
        self.assertEqual(cmd, '4R_M5')

    def test_create_command_4r_m4(self):
        cmd = core.create_command(channel=4, output='R', speed=-4, brake=False)
        self.assertEqual(cmd, '4R_M4')

    def test_create_command_4r_m3(self):
        cmd = core.create_command(channel=4, output='R', speed=-3, brake=False)
        self.assertEqual(cmd, '4R_M3')

    def test_create_command_4r_m2(self):
        cmd = core.create_command(channel=4, output='R', speed=-2, brake=False)
        self.assertEqual(cmd, '4R_M2')

    def test_create_command_4r_m1(self):
        cmd = core.create_command(channel=4, output='R', speed=-1, brake=False)
        self.assertEqual(cmd, '4R_M1')

    def test_create_command_4r_0(self):
        cmd = core.create_command(channel=4, output='R', speed=0, brake=False)
        self.assertEqual(cmd, '4R_0')

    def test_create_command_4r_1(self):
        cmd = core.create_command(channel=4, output='R', speed=1, brake=False)
        self.assertEqual(cmd, '4R_1')

    def test_create_command_4r_2(self):
        cmd = core.create_command(channel=4, output='R', speed=2, brake=False)
        self.assertEqual(cmd, '4R_2')

    def test_create_command_4r_3(self):
        cmd = core.create_command(channel=4, output='R', speed=3, brake=False)
        self.assertEqual(cmd, '4R_3')

    def test_create_command_4r_4(self):
        cmd = core.create_command(channel=4, output='R', speed=4, brake=False)
        self.assertEqual(cmd, '4R_4')

    def test_create_command_4r_5(self):
        cmd = core.create_command(channel=4, output='R', speed=5, brake=False)
        self.assertEqual(cmd, '4R_5')

    def test_create_command_4r_6(self):
        cmd = core.create_command(channel=4, output='R', speed=6, brake=False)
        self.assertEqual(cmd, '4R_6')

    def test_create_command_4r_7(self):
        cmd = core.create_command(channel=4, output='R', speed=7, brake=False)
        self.assertEqual(cmd, '4R_7')

    def test_create_command_4r_brake(self):
        cmd = core.create_command(channel=4, output='R', speed=7, brake=True)
        self.assertEqual(cmd, '4R_BRAKE')

    def test_create_command_1b_m7(self):
        cmd = core.create_command(channel=1, output='B', speed=-7, brake=False)
        self.assertEqual(cmd, '1B_M7')

    def test_create_command_1b_m6(self):
        cmd = core.create_command(channel=1, output='B', speed=-6, brake=False)
        self.assertEqual(cmd, '1B_M6')

    def test_create_command_1b_m5(self):
        cmd = core.create_command(channel=1, output='B', speed=-5, brake=False)
        self.assertEqual(cmd, '1B_M5')

    def test_create_command_1b_m4(self):
        cmd = core.create_command(channel=1, output='B', speed=-4, brake=False)
        self.assertEqual(cmd, '1B_M4')

    def test_create_command_1b_m3(self):
        cmd = core.create_command(channel=1, output='B', speed=-3, brake=False)
        self.assertEqual(cmd, '1B_M3')

    def test_create_command_1b_m2(self):
        cmd = core.create_command(channel=1, output='B', speed=-2, brake=False)
        self.assertEqual(cmd, '1B_M2')

    def test_create_command_1b_m1(self):
        cmd = core.create_command(channel=1, output='B', speed=-1, brake=False)
        self.assertEqual(cmd, '1B_M1')

    def test_create_command_1b_0(self):
        cmd = core.create_command(channel=1, output='B', speed=0, brake=False)
        self.assertEqual(cmd, '1B_0')

    def test_create_command_1b_1(self):
        cmd = core.create_command(channel=1, output='B', speed=1, brake=False)
        self.assertEqual(cmd, '1B_1')

    def test_create_command_1b_2(self):
        cmd = core.create_command(channel=1, output='B', speed=2, brake=False)
        self.assertEqual(cmd, '1B_2')

    def test_create_command_1b_3(self):
        cmd = core.create_command(channel=1, output='B', speed=3, brake=False)
        self.assertEqual(cmd, '1B_3')

    def test_create_command_1b_4(self):
        cmd = core.create_command(channel=1, output='B', speed=4, brake=False)
        self.assertEqual(cmd, '1B_4')

    def test_create_command_1b_5(self):
        cmd = core.create_command(channel=1, output='B', speed=5, brake=False)
        self.assertEqual(cmd, '1B_5')

    def test_create_command_1b_6(self):
        cmd = core.create_command(channel=1, output='B', speed=6, brake=False)
        self.assertEqual(cmd, '1B_6')

    def test_create_command_1b_7(self):
        cmd = core.create_command(channel=1, output='B', speed=7, brake=False)
        self.assertEqual(cmd, '1B_7')

    def test_create_command_1b_brake(self):
        cmd = core.create_command(channel=1, output='B', speed=7, brake=True)
        self.assertEqual(cmd, '1B_BRAKE')

    def test_create_command_2b_m7(self):
        cmd = core.create_command(channel=2, output='B', speed=-7, brake=False)
        self.assertEqual(cmd, '2B_M7')

    def test_create_command_2b_m6(self):
        cmd = core.create_command(channel=2, output='B', speed=-6, brake=False)
        self.assertEqual(cmd, '2B_M6')

    def test_create_command_2b_m5(self):
        cmd = core.create_command(channel=2, output='B', speed=-5, brake=False)
        self.assertEqual(cmd, '2B_M5')

    def test_create_command_2b_m4(self):
        cmd = core.create_command(channel=2, output='B', speed=-4, brake=False)
        self.assertEqual(cmd, '2B_M4')

    def test_create_command_2b_m3(self):
        cmd = core.create_command(channel=2, output='B', speed=-3, brake=False)
        self.assertEqual(cmd, '2B_M3')

    def test_create_command_2b_m2(self):
        cmd = core.create_command(channel=2, output='B', speed=-2, brake=False)
        self.assertEqual(cmd, '2B_M2')

    def test_create_command_2b_m1(self):
        cmd = core.create_command(channel=2, output='B', speed=-1, brake=False)
        self.assertEqual(cmd, '2B_M1')

    def test_create_command_2b_0(self):
        cmd = core.create_command(channel=2, output='B', speed=0, brake=False)
        self.assertEqual(cmd, '2B_0')

    def test_create_command_2b_1(self):
        cmd = core.create_command(channel=2, output='B', speed=1, brake=False)
        self.assertEqual(cmd, '2B_1')

    def test_create_command_2b_2(self):
        cmd = core.create_command(channel=2, output='B', speed=2, brake=False)
        self.assertEqual(cmd, '2B_2')

    def test_create_command_2b_3(self):
        cmd = core.create_command(channel=2, output='B', speed=3, brake=False)
        self.assertEqual(cmd, '2B_3')

    def test_create_command_2b_4(self):
        cmd = core.create_command(channel=2, output='B', speed=4, brake=False)
        self.assertEqual(cmd, '2B_4')

    def test_create_command_2b_5(self):
        cmd = core.create_command(channel=2, output='B', speed=5, brake=False)
        self.assertEqual(cmd, '2B_5')

    def test_create_command_2b_6(self):
        cmd = core.create_command(channel=2, output='B', speed=6, brake=False)
        self.assertEqual(cmd, '2B_6')

    def test_create_command_2b_7(self):
        cmd = core.create_command(channel=2, output='B', speed=7, brake=False)
        self.assertEqual(cmd, '2B_7')

    def test_create_command_2b_brake(self):
        cmd = core.create_command(channel=2, output='B', speed=7, brake=True)
        self.assertEqual(cmd, '2B_BRAKE')

    def test_create_command_3b_m7(self):
        cmd = core.create_command(channel=3, output='B', speed=-7, brake=False)
        self.assertEqual(cmd, '3B_M7')

    def test_create_command_3b_m6(self):
        cmd = core.create_command(channel=3, output='B', speed=-6, brake=False)
        self.assertEqual(cmd, '3B_M6')

    def test_create_command_3b_m5(self):
        cmd = core.create_command(channel=3, output='B', speed=-5, brake=False)
        self.assertEqual(cmd, '3B_M5')

    def test_create_command_3b_m4(self):
        cmd = core.create_command(channel=3, output='B', speed=-4, brake=False)
        self.assertEqual(cmd, '3B_M4')

    def test_create_command_3b_m3(self):
        cmd = core.create_command(channel=3, output='B', speed=-3, brake=False)
        self.assertEqual(cmd, '3B_M3')

    def test_create_command_3b_m2(self):
        cmd = core.create_command(channel=3, output='B', speed=-2, brake=False)
        self.assertEqual(cmd, '3B_M2')

    def test_create_command_3b_m1(self):
        cmd = core.create_command(channel=3, output='B', speed=-1, brake=False)
        self.assertEqual(cmd, '3B_M1')

    def test_create_command_3b_0(self):
        cmd = core.create_command(channel=3, output='B', speed=0, brake=False)
        self.assertEqual(cmd, '3B_0')

    def test_create_command_3b_1(self):
        cmd = core.create_command(channel=3, output='B', speed=1, brake=False)
        self.assertEqual(cmd, '3B_1')

    def test_create_command_3b_2(self):
        cmd = core.create_command(channel=3, output='B', speed=2, brake=False)
        self.assertEqual(cmd, '3B_2')

    def test_create_command_3b_3(self):
        cmd = core.create_command(channel=3, output='B', speed=3, brake=False)
        self.assertEqual(cmd, '3B_3')

    def test_create_command_3b_4(self):
        cmd = core.create_command(channel=3, output='B', speed=4, brake=False)
        self.assertEqual(cmd, '3B_4')

    def test_create_command_3b_5(self):
        cmd = core.create_command(channel=3, output='B', speed=5, brake=False)
        self.assertEqual(cmd, '3B_5')

    def test_create_command_3b_6(self):
        cmd = core.create_command(channel=3, output='B', speed=6, brake=False)
        self.assertEqual(cmd, '3B_6')

    def test_create_command_3b_7(self):
        cmd = core.create_command(channel=3, output='B', speed=7, brake=False)
        self.assertEqual(cmd, '3B_7')

    def test_create_command_3b_brake(self):
        cmd = core.create_command(channel=3, output='B', speed=7, brake=True)
        self.assertEqual(cmd, '3B_BRAKE')

    def test_create_command_4b_m7(self):
        cmd = core.create_command(channel=4, output='B', speed=-7, brake=False)
        self.assertEqual(cmd, '4B_M7')

    def test_create_command_4b_m6(self):
        cmd = core.create_command(channel=4, output='B', speed=-6, brake=False)
        self.assertEqual(cmd, '4B_M6')

    def test_create_command_4b_m5(self):
        cmd = core.create_command(channel=4, output='B', speed=-5, brake=False)
        self.assertEqual(cmd, '4B_M5')

    def test_create_command_4b_m4(self):
        cmd = core.create_command(channel=4, output='B', speed=-4, brake=False)
        self.assertEqual(cmd, '4B_M4')

    def test_create_command_4b_m3(self):
        cmd = core.create_command(channel=4, output='B', speed=-3, brake=False)
        self.assertEqual(cmd, '4B_M3')

    def test_create_command_4b_m2(self):
        cmd = core.create_command(channel=4, output='B', speed=-2, brake=False)
        self.assertEqual(cmd, '4B_M2')

    def test_create_command_4b_m1(self):
        cmd = core.create_command(channel=4, output='B', speed=-1, brake=False)
        self.assertEqual(cmd, '4B_M1')

    def test_create_command_4b_0(self):
        cmd = core.create_command(channel=4, output='B', speed=0, brake=False)
        self.assertEqual(cmd, '4B_0')

    def test_create_command_4b_1(self):
        cmd = core.create_command(channel=4, output='B', speed=1, brake=False)
        self.assertEqual(cmd, '4B_1')

    def test_create_command_4b_2(self):
        cmd = core.create_command(channel=4, output='B', speed=2, brake=False)
        self.assertEqual(cmd, '4B_2')

    def test_create_command_4b_3(self):
        cmd = core.create_command(channel=4, output='B', speed=3, brake=False)
        self.assertEqual(cmd, '4B_3')

    def test_create_command_4b_4(self):
        cmd = core.create_command(channel=4, output='B', speed=4, brake=False)
        self.assertEqual(cmd, '4B_4')

    def test_create_command_4b_5(self):
        cmd = core.create_command(channel=4, output='B', speed=5, brake=False)
        self.assertEqual(cmd, '4B_5')

    def test_create_command_4b_6(self):
        cmd = core.create_command(channel=4, output='B', speed=6, brake=False)
        self.assertEqual(cmd, '4B_6')

    def test_create_command_4b_7(self):
        cmd = core.create_command(channel=4, output='B', speed=7, brake=False)
        self.assertEqual(cmd, '4B_7')

    def test_create_command_4b_brake(self):
        cmd = core.create_command(channel=4, output='B', speed=7, brake=True)
        self.assertEqual(cmd, '4B_BRAKE')
