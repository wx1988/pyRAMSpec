"""
This module is the unittest for the information retrieval from Mac system.
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from pyRAMSpec.mac import parse_mac_sphardwaredatatype, parse_mac_spmemorydatatype

class TestSPHardwareDataType(unittest.TestCase):
    """
    unittest to get machine model for Apple product
    """
    def test_macbook71(self):
        """
        This function is to test the output from a Macbook machine around 2011
        """
        hardware_desc = """Hardware Overview:

      Model Name: MacBook
      Model Identifier: MacBook7,1
      Processor Name: Intel Core 2 Duo
      Processor Speed: 2.4 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache: 3 MB
      Memory: 4 GB
      Bus Speed: 1.07 GHz
      Boot ROM Version: MB71.0039.B0E
      SMC Version (system): 1.60f6
      Serial Number (system): 45118AJ8F5W
      Hardware UUID: 852D63CA-1795-5BC2-A9A4-CC7D1531C39B
      Sudden Motion Sensor:
          State: Enabled"""
        res = parse_mac_sphardwaredatatype(hardware_desc)
        self.assertEqual(res['productname'], 'MacBook7,1')


class TestSPMemoryDataType(unittest.TestCase):
    """
    Unit test about memory information
    """
    def test_macbook71_full(self):
        """
        This function is to test an updated Macbook around 2011
            with memory upgraded from single to double
        """
        mem_desc = """    Memory Slots:
      ECC: Disabled
      Upgradeable Memory: Yes

        BANK 0/DIMM0:

          Size: 2 GB
          Type: DDR3
          Speed: 1067 MHz
          Status: OK
          Manufacturer: 0x80CE
          Part Number: 0x4D34373142353637334548312D4346382020
          Serial Number: 0x6173F8BE

        BANK 1/DIMM0:

          Size: 2 GB
          Type: DDR3
          Speed: 1067 MHz
          Status: OK
          Manufacturer: 0x80CE
          Part Number: 0x4D3437314235363733445A312D4346382020
          Serial Number: 0x465B1F22"""
        res = parse_mac_spmemorydatatype(mem_desc)
        self.assertEqual(res['upgradeable'], True)
        mem_info_list_groundtruth = [
            {
                'capacity': 2048,
                'type': 'DDR3',
                'speed': 1067,
                'manufacturer': '0x80CE',
                'model': '0x4D34373142353637334548312D4346382020',
                },
            {
                'capacity': 2048,
                'type': 'DDR3',
                'speed': 1067,
                'manufacturer': '0x80CE',
                'model': '0x4D3437314235363733445A312D4346382020',
                }
            ]
        self.assertEqual(res['mem_info_list'], mem_info_list_groundtruth)

