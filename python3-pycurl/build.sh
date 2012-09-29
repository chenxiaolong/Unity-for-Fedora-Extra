#!/usr/bin/env bash

SPECFILE=python3-pycurl.spec
MULTILIB=true
MULTILIB_PACKAGES=('python3-pycurl')
DO_NOT_INSTALL=('python3-pycurl-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
