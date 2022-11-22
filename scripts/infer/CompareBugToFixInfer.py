'''

Created on Jan. 4, 2018

@author Andrew Habib

'''

import json
import os
import sys

from scripts.errorprone.Util import load_parsed_inf, CustomEncoder


def match_inf_msg_no_lines(msg, msgs):
    for msg2 in msgs:
        if (msg.proj == msg2.proj and msg.cls == msg2.cls and
            msg.bug_type == msg2.bug_type and msg.severity == msg2.severity and
            msg.procedure == msg2.procedure):
        
            return True
        
    return False


def get_removed_warnings_inf(inf_b, inf_f):
    removed_warnings = []
    for b_msg in inf_b:
        if not match_inf_msg_no_lines(b_msg, inf_f):
            removed_warnings.append(b_msg)

    return removed_warnings


if __name__ == '__main__':
    
    """Get errors/warnings that disappeared in fixed versions"""
    
    inf_file = "/home/yuliia/PycharmProjects/masters/results/bug/inf_parsed.json"
    inf_res_b = load_parsed_inf(inf_file)
      
    inf_file = "/home/yuliia/PycharmProjects/masters/results/fix/inf_parsed.json"
    inf_res_f = load_parsed_inf(inf_file)
      
    warnings = get_removed_warnings_inf(inf_res_b, inf_res_f)
    
    output_file_name = "inf_removed_warnings.json"
    with open(output_file_name, "w") as file:
        json.dump(warnings, file, cls=CustomEncoder, indent=4)
