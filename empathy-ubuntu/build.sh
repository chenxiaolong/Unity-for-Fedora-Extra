#!/usr/bin/env bash

SPECFILE=empathy-ubuntu.spec
MULTILIB=false
DO_NOT_INSTALL=('empathy-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
