"""
The test for the dmidecode
"""

import unittest

from pyRAMSpec.dmidecode_parser import parse_machine_info
from pyRAMSpec.dmidecode_parser import parse_ram_capacity_info
from pyRAMSpec.dmidecode_parser import parse_mem_info_list


class TestDmidecodeSystem(unittest.TestCase):
    """Test the function to parse machine model
    """
    def test_dell_t3610(self):
        """Test the dell build T3610 for machine informaiton
        """
        system_str = """# dmidecode 2.12
SMBIOS 2.7 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
    Manufacturer: Dell Inc.
    Product Name: Precision T3610
    Version: 01
    Serial Number: 2PJF9Z1
    UUID: 4C4C4544-0050-4A10-8046-B2C04F395A31
    Wake-up Type: Power Switch
    SKU Number: Precision T3610
    Family: Not Specified

Handle 0x0030, DMI type 12, 5 bytes
System Configuration Options
    Option 1: To Be Filled By O.E.M.

Handle 0x0031, DMI type 15, 35 bytes
System Event Log
    Area Length: 4 bytes
    Header Start Offset: 0x0000
    Header Length: 2 bytes
    Data Start Offset: 0x0002
    Access Method: Indexed I/O, one 16-bit index port, one 8-bit data port
    Access Address: Index 0x046A, Data 0x046C
    Status: Invalid, Not Full
    Change Token: 0x00000000
    Header Format: No Header
    Supported Log Type Descriptors: 6
    Descriptor 1: End of log
    Data Format 1: OEM-specific
    Descriptor 2: End of log
    Data Format 2: OEM-specific
    Descriptor 3: End of log
    Data Format 3: OEM-specific
    Descriptor 4: End of log
    Data Format 4: OEM-specific
    Descriptor 5: End of log
    Data Format 5: OEM-specific
    Descriptor 6: End of log
    Data Format 6: OEM-specific

Handle 0x0045, DMI type 32, 20 bytes
System Boot Information
    Status: No errors detected"""
        sys_info_dict = parse_machine_info(system_str)
        self.assertEqual(sys_info_dict['manufacturer'], 'Dell Inc.')
        self.assertEqual(sys_info_dict['productname'], 'Precision T3610')

class TestDmidecode16(unittest.TestCase):
    """The summarized capacity about the memory
    """
    def test_dell_t3610(self):
        """Test on Dell T3610
        """
        t16_output = """# dmidecode 2.12
SMBIOS 2.7 present.

Handle 0x0032, DMI type 16, 23 bytes
Physical Memory Array
    Location: System Board Or Motherboard
    Use: System Memory
    Error Correction Type: Multi-bit ECC
    Maximum Capacity: 128 GB
    Error Information Handle: Not Provided
    Number Of Devices: 8"""
        ram_cap = parse_ram_capacity_info(t16_output)
        self.assertEqual(ram_cap['maximum_capacity'], 128)
        self.assertEqual(ram_cap['slots'], 8)

class TestDmidecode17(unittest.TestCase):
    """Test the detail information about the memory list
    """
    def test_dell_t3610(self):
        """Test on unmodified Dell T3610
        """
        t17_output = """# dmidecode 2.12
SMBIOS 2.7 present.

Handle 0x0034, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: 4096 MB
    Form Factor: DIMM
    Set: None
    Locator: DIMM1
    Bank Locator: Not Specified
    Type: DDR3
    Type Detail: Registered (Buffered)
    Speed: 1866 MHz
    Manufacturer: Hynix Semiconductor
    Serial Number: 41B899DE    
    Asset Tag: 01133763
    Part Number: HMT451R7AFR8C-RD  
    Rank: 2
    Configured Clock Speed: 1866 MHz

Handle 0x0036, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM5
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm5_Manufacturer1
    Serial Number: Dimm5_SerNum
    Asset Tag: Dimm5_AT
    Part Number: Dimm5_PartNumber01
    Rank: Unknown
    Configured Clock Speed: Unknown

Handle 0x0038, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM3
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm3_Manufacturer1
    Serial Number: Dimm3_SerNum
    Asset Tag: Dimm3_AT
    Part Number: Dimm3_PartNumber02
    Rank: Unknown
    Configured Clock Speed: Unknown

Handle 0x003A, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM7
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm7_Manufacturer1
    Serial Number: Dimm7_SerNum
    Asset Tag: Dimm7_AT
    Part Number: Dimm7_PartNumber03
    Rank: Unknown
    Configured Clock Speed: Unknown

Handle 0x003C, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: 4096 MB
    Form Factor: DIMM
    Set: None
    Locator: DIMM2
    Bank Locator: Not Specified
    Type: DDR3
    Type Detail: Registered (Buffered)
    Speed: 1866 MHz
    Manufacturer: Hynix Semiconductor
    Serial Number: 413899DF    
    Asset Tag: 01133763
    Part Number: HMT451R7AFR8C-RD  
    Rank: 2
    Configured Clock Speed: 1866 MHz

Handle 0x003E, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM6
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm6_Manufacturer1
    Serial Number: Dimm6_SerNum
    Asset Tag: Dimm6_AT
    Part Number: Dimm6_PartNumber05
    Rank: Unknown
    Configured Clock Speed: Unknown

Handle 0x0040, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM4
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm4_Manufacturer1
    Serial Number: Dimm4_SerNum
    Asset Tag: Dimm4_AT
    Part Number: Dimm4_PartNumber06
    Rank: Unknown
    Configured Clock Speed: Unknown

Handle 0x0042, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0032
    Error Information Handle: Not Provided
    Total Width: 72 bits
    Data Width: 64 bits
    Size: No Module Installed
    Form Factor: DIMM
    Set: None
    Locator: DIMM8
    Bank Locator: Not Specified
    Type: Unknown
    Type Detail: Synchronous
    Speed: Unknown
    Manufacturer: Dimm8_Manufacturer1
    Serial Number: Dimm8_SerNum
    Asset Tag: Dimm8_AT
    Part Number: Dimm8_PartNumber07
    Rank: Unknown
    Configured Clock Speed: Unknown"""
        mem_list = parse_mem_info_list(t17_output)
        true_mem_list = [
            {
                'capacity': 4096,
                'type': 'DDR3',
                'detail': 'Registered (Buffered)',
                'speed': 1866,
                'model': 'HMT451R7AFR8C-RD'
            },
            {
                'capacity': 4096,
                'type': 'DDR3',
                'detail': 'Registered (Buffered)',
                'speed': 1866,
                'model': 'HMT451R7AFR8C-RD'
            }
            ]
        self.assertEqual(mem_list, true_mem_list)

