"""
Get the ram information in the mac os with built in system_profiler
system_profiler SPMemoryDataType
system_profiler SPHardwareDataType
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from pyRAMSpec.ramspec_util import execute_cmd

def get_sys_info():
    """
    system_profiler SPMemoryDataType
    Example of results
    """
    sys_info = {}

    # machine model
    output = execute_cmd(['system_profiler' 'SPHardwareDataType'])
    machine_info = parse_mac_sphardwaredatatype(output)
    sys_info = dict(sys_info, **machine_info)

    # system information
    # TODO, the ram of macbook air is onboard and not upgradeable

    # memory information
    output = execute_cmd(['system_profiler' 'SPMemoryDataType'])
    mem_info = parse_mac_spmemorydatatype(output)
    sys_info = dict(sys_info, **mem_info)

def parse_mac_sphardwaredatatype(hardware_info_str):
    """
    system_profiler SPHardwareDataType
    Example is shown below and the key is "Model Identifier",
    move the example to test file

    :return :
    """
    machine_info = {"manufacturer": "Apple"}
    lines = [line.strip() for line in hardware_info_str.split("\n")]
    for line in lines:
        if line.startswith("Model Identifier"):
            machine_info['productname'] = line[line.index(":")+1:].strip()
    return machine_info

def parse_mac_spmemorydatatype(mem_info_str):
    """
    system_profiler SPMemoryDataType

    :return: information about the upgradeable and detail of memory list information
    """
    res = {}

    # upgradable
    upgrade_regex = r"Upgradeable(\s|\S)*?: ((\S)*?)\n"
    upgrade_flag_m = re.search(upgrade_regex, mem_info_str)
    res['upgradeable'] = True if upgrade_flag_m.group(2) == "Yes" else False

    # memory list
    any_pattern = r"(\s|\S)*?"
    one_slot_regex = r"BANK{0}Size:({0})\n{0}Type:({0})\n"
    one_slot_regex += r"{0}Speed:({0})\n{0}Manufacturer:({0})\n"
    one_slot_regex += r"{0}Part Number:({0})\n{0}Serial Number:({0})"
    one_slot_regex = one_slot_regex.format(any_pattern)
    mem_info_list = []
    for mem_m in re.findall(one_slot_regex, mem_info_str):
        mem_info = {
            'capacity': int(mem_m[1].strip().split(' ')[0]) * 1024,
            'type': mem_m[4].strip(),
            'speed': int(mem_m[7].strip().split(' ')[0]),
            'manufacturer': mem_m[10].strip(),
            'model': mem_m[13].strip()
            }
        mem_info_list.append(mem_info)

    res['mem_info_list'] = mem_info_list

    return res
