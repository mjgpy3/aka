#!/usr/bin/env python

import json
import os
import sys

def raw_aliases():
    '''
    Reads in the aliases file as a Python object
    '''
    with open(os.environ['AKA_ALIASES'], 'r') as f:
        return json.loads(f.read())

def make_lookup(alias_object, current_path=[], current_command=[], result={}):
    '''
    Given a raw alias object, make it easily searchable
    '''

    for alias in alias_object:
        p = current_path + [alias['token']]
        c = current_command + [alias['command']]
        result[tuple(p)] = ' '.join(c)

        make_lookup(alias.get('branches', []), p, c, result)

    return result


lookup = make_lookup(raw_aliases())

print(lookup)
print(sys.argv)[1:]

os.system(lookup[tuple(sys.argv[1:])])
