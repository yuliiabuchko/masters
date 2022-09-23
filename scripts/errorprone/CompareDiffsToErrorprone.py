'''

Created on Nov. 30, 2017

@author Andrew Habib

'''

import json
import os
import sys

from Util import load_parsed_diffs, load_parsed_ep, find_msg_by_proj_and_cls, \
                LineMatchesToMessages, CustomEncoder

from main import *


def match_diff_ep(d, ep_list):
    matches = []
    lines_matches = []
    for inst in ep_list:
        if inst.line in d.lines:
            matches.append(inst)
            lines_matches.append(inst.line)
    return matches, set(lines_matches)


def get_hits_diffs_ep(diffs, ep_res_set):
    ep_count = 0
    ep_all_matches = []
    diffs_match_ep = []
    for d in diffs:
        
        proj = d.proj
        try:
            cls = d.cls.split("src.main.java.")[1][:-5]
            # cls = cls.split(".")[-2]
            # print(cls)
        except:
            cls = d.cls
        
        ep_list = find_msg_by_proj_and_cls(proj, cls, ep_res_set)
        diff_ep, lines = match_diff_ep(d, ep_list)
        if diff_ep:

            ep_count += len(diff_ep)
            ep_all_matches.append(LineMatchesToMessages(lines, diff_ep))
            diffs_match_ep.extend(diff_ep)
#     print(ep_count)

#     return ep_all_matches
    return diffs_match_ep


if __name__ == '__main__':

    """Get lines matches between each tool and  bug fixes diffs"""

    diffs_file = os.path.join(PATH_TO_RESULTS, "diffs_parsed.json")
    diffs = load_parsed_diffs(diffs_file)
      
    ep_file = os.path.join(PATH_TO_RESULTS, BUG_FOLDER, "ep_parsed.json")
    ep_res_set = load_parsed_ep(ep_file)
  
    diffs_ep = get_hits_diffs_ep(diffs, ep_res_set)

    output_file_name = "ep_diffs_warnings.json"
    with open(os.path.join(PATH_TO_RESULTS, output_file_name), "w") as file:
        json.dump(diffs_ep, file, cls=CustomEncoder, indent=4)

# for a in res:
# s.append(" ".join(
#     ["    ", a[' Proj'].split("_")[0], "&", a[' Proj'].split("bugs-dot-jar_")[1].replace("_", "\_"), "&", a['  Cat'],
#      "& \\\\ "]))
