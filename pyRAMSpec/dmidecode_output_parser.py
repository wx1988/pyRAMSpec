#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This file format the output of dmidecode output
"""

def parse_machine_info(dmidecode_output):
    """output
    :return : dict that contains manufacturer and productname
    """
    machine_info = {}
    lines = [line.strip() for line in dmidecode_output.split("\n")]
    for line in lines:
        if line.startswith("Manufacturer"):
            machine_info['manufacturer'] = line[line.index(":")+1:]
        if line.startswith("Product Name"):
            machine_info['productname'] = line[line.index(":")+1:]
    return machine_info

def get_machine_info(dmidecode_path='dmidecode'):
    """
    """
    get_sys_cmd = [dmidecode_path, "-t", "system"]
    system_str = execute_cmd(get_sys_cmd) 
    return parse_machine_info(system_str)

def parse_ram_capacity_info(dmidecode_output):
    """Parse the output of ram capacity information in dmidecode
    """
    cap_info = {}
    lines = [line.strip() for line in dmidecode_output.split("\n")]
    for line in lines:
        word_list = line.split(':')
        if line.startswith("Max"):
            max_capacity = int(word_list[1].strip().split(' ')[0])
            cap_info['maximum_capacity'] = max_capacity
        if line.startswith("Num"):
            cap_info['slots'] = int(word_list[1])
    return cap_info

def get_ram_capacity_info(dmidecode_path='dmidecode'):
    """TODO, what does 16 mean?
    """
    get_rc_cmd = [dmidecode_path, "-t", "16"]
    rc_str = execute_cmd(get_rc_cmd) 
    return parse_ram_capcity_info(rc_str)

def parse_mem_info_list(dmidecode_output):
    """get list of memory information from output of 
    dmidecode -t 17
    """
    lines = [line.strip() for line in dmidecode_output.split("\n")]
    #print output

    # 1. size
    size_re = re.compile(r"Size: (\d+) MB")
    # 2. type
    type_re = re.compile(r"Type: ([\s\S]*?)\n")
    typed_re = re.compile(r"Type Detail: ([\w ]+)")
    # 3. speed
    speed_re = re.compile(r"Speed: (\d+) MHz")
    # 4. Part number
    pn_re = re.compile(r"Part Number: ([\s|\S]*?)\n")

    mem_info_list = []
    mem_list = output.split('\n\n')
    for mem in mem_list:
        mem = mem.strip()
        #print '0', mem[0]
        if mem == "":
            continue
        if mem.startswith("Handle"):
            print 'Mem', mem
            size_str = size_re.search(mem).group(1)
            print 'size'
            type_str = type_re.search(mem).group(1)
            print 'type'
            typed_str = typed_re.search(mem).group(1)
            print 'speed'
            speed_str = speed_re.search(mem).group(1)
            print 'pn'
            pn_str = pn_re.search(mem).group(1)
            mem_info = {
                'capacity':int(size_str),
                'type':type_str,
                'detail':typed_str.strip(),
                'speed':int(speed_str),
                'model': pn_str.strip()
                }
            mem_info_list.append(mem_info)
            
    return mem_info_list

def get_mem_info_list(dmidecode_path="dmidecode"):    
    dmidecode_cmd = [dmidecode_path, "-t", "17"]
    output = execute_cmd(dmidecode_cmd)
    return parse_mem_info_list(output)

def get_sys_info():
    dmidecode_path = ""
    if os.path.isfile("./dmidecode.exe"):
        dmidecode_path = "./dmidecode.exe"
    elif os.path.isfile("./dist/dmidecode.exe"):
        dmidecode_path = "./dist/dmidecode.exe"
    else:
        raise Exception("dmidecode not found")
    print "detected dmidecode", dmidecode_path
    
    sys_info = {}
    
    # machine model
    machine_info = get_machine_info()
    sys_info = dict(sys_info, **machine_info)
    
    # maximal capacity
    ram_cap_info = get_ram_capacity_info()
    sys_info = dict(sys_info, **ram_cap_info)

    # get existing memories
    mem_info_list = get_mem_info_list()
    sys_info['mem_info_list'] = mem_info_list

    return sys_info

