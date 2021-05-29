#!/usr/bin/env python

import os
from subprocess import getoutput, getstatusoutput

prg = './hello.py'


def test_exists():
    #* Exists!

    assert os.path.isfile(prg)


def test_runnable():
    out = getoutput(f"python {prg}")
    assert out.strip() == 'Hello, World!'


def test_executable():
    #* Says 'Hello, World!' by default
    
    out = getoutput({prg})
    assert out.strip() == 'Hello, World!'


def test_usage():

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')