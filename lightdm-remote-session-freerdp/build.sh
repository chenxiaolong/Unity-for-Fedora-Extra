#!/usr/bin/env bash

SPECFILE=lightdm-remote-session-freerdp.spec
MULTILIB=false
DO_NOT_INSTALL=('lightdm-remote-session-freerdp-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
