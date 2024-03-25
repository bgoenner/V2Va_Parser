
import os, sys

import regex
import mmap

import networkx as nx


#module_reg = r"\s*module\s*(?P<module>\s*[a-zA-Z][\w]*)\s*\((?P<ports>[\s*\w*,]*)\)\s*;(?P<module_netlist>[\w*\s*,;\(\)\.]*?)endmodule"
module_reg = r"^[ ]*module\s*(?P<module_name>[a-zA-Z][\w]*)\s\((?P<module_ports>[\s\w,]*)\)\s*;(?P<module_netlist>[\s\w.,\(\);]*?)endmodule"
input_reg  = r"^[ ]*input\s*(?P<input_port>[\w*, \n]*);"
output_reg = r"^[ ]*output\s*(?P<output_port>[\w*, \n]*);"
wire_reg   = r"^[ ]*wire\s*(?P<wires>[\w*, \n]*);"
comp_reg   = r"^[ ]*(?P<component>[a-zA-Z][\w]*)\s*(?P<name>[a-zA-Z][\w]*)\s*\((?P<ports>[\w\(\),\s.]*)\)\s*;"
single_mod_reg = r"^[ ]*(module\s*(?P<module_name>[a-zA-Z][\w]*)\s*\((?P<module_ports>[\s\w,]*\);)|wire\s*(?P<wires>[a-zA-Z][\w\s,]*);|input\s*(?P<in_ports>[a-zA-Z][\w\s,]*);|output\s*(?P<out_ports>[a-zA-Z][\w\s,]*);|(?P<component>[a-zA-Z][\w]*)\s*(?P<name>[a-zA-Z][\w]*)\s*\((?P<ports>[\w\(\),\s.]*)\)\s*;)"
component_port_reg = r".(?P<component_port>[a-zA-Z][\w]*)\s*\(\s*(?P<net_port>[a-zA-Z][\w]*)\s*\)\s*"

m_frm = 'utf-8'
"""
in_v input verilog file
"""
def get_modules(in_v, debug=False):

    # get modules
    mod_re_b = bytes(module_reg, 'utf-8')

    with open(in_v, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        mo = regex.findall(mod_re_b, data, re.MULTILINE)

    mod_net = nx.Graph()

    for m in mo:
        mod_net.add_node(m.group('module_name').decode('uft-8'))
        # remove ws and split by ,
        mod_ports = regex.sub('\s', '', m.group('module_ports').decode('utf-8')).split(',')
        
    # build out netlist

    # get top level module
 
    pass


def main(in_v, out_dir):
    pass

