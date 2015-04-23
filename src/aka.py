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
    return lambda args, _: ' '.join(command_pieces + args)

def splat_params_command(command_pieces, splat_text):
    return lambda args, _: ' '.join(command_pieces).replace(splat_text, ' '.join(args))

def on_success_command(old_command, name):
    return lambda args, env: old_command(args, env) + ' && ' + env['named_aliases'][name](args, env)

def build_command(alias, current_command):
    if 'splatParamsInto' in alias:
        command =  splat_params_command(current_command, alias['splatParamsInto'])
    else:
        command = simple_command(current_command)

    if 'onSuccessRun' in alias:
        command = (lambda f: on_success_command(f, alias['onSuccessRun']))(command)

    return command

def make_lookup(alias_object, current_path=[], current_command=[], result={ 'commands': {}, 'named_aliases': {} }):
    '''
    Given a raw alias object, make it easily searchable
    '''

    for alias in alias_object:
        p = current_path + [alias.get('token', None)]
        c = current_command + [alias['command']]

        result['commands'][tuple(p)] = build_command(alias, c)

        if 'name' in alias:
            result['named_aliases'][alias['name']] = result['commands'][tuple(p)]

        make_lookup(alias.get('branches', []), p, c, result)

    return result

def chopback_lookup(alias_dict, args):
    commands = alias_dict['commands']
    for i in xrange(len(commands), -1, -1):
        seek = tuple(args[:i])
        if seek in commands:
            return commands[seek](args[i:], alias_dict)

    return None

if __name__ == '__main__':
    lookup = make_lookup(raw_aliases())

    command = chopback_lookup(lookup, sys.argv[1:])

    if command:
        os.system(command)
    else:
        print 'Couldn\'t find alias for', (' '.join(sys.argv[1:]) or 'the absence of a pattern')
