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

def simple_command(command_pieces):
    return lambda args: ' '.join(command_pieces + args)

def splat_params_command(command_pieces, splat_text):
    return lambda args: ' '.join(command_pieces).replace(splat_text, ' '.join(args))

def make_lookup(alias_object, current_path=[], current_command=[], result={}):
    '''
    Given a raw alias object, make it easily searchable
    '''

    for alias in alias_object:
        p = current_path + [alias['token']]
        c = current_command + [alias['command']]
        if 'splatParamsInto' in alias:
            result[tuple(p)] = splat_params_command(c, alias['splatParamsInto'])
        else:
            result[tuple(p)] = simple_command(c)

        make_lookup(alias.get('branches', []), p, c, result)

    return result

def chopback_lookup(alias_dict, args):
    for i in xrange(len(alias_dict), -1, -1):
        seek = tuple(args[:i])
        if seek in alias_dict:
            return alias_dict[seek](args[i:])

    return None

if __name__ == '__main__':
    lookup = make_lookup(raw_aliases())

    command = chopback_lookup(lookup, sys.argv[1:])

    if command:
        os.system(command)
    else:
        print 'Couldn\'t find alias for', (' '.join(sys.argv[1:]) or 'the absence of a pattern')
