#!/usr/bin/env bash

SPECFILE=libpam-freerdp.spec
MULTILIB=false
DO_NOT_INSTALL=('libpam-freerdp-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
