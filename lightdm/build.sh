#!/usr/bin/env bash

SPECFILE=lightdm.spec
MULTILIB=false
DO_NOT_INSTALL=('lightdm-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
