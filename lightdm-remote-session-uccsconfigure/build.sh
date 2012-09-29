#!/usr/bin/env bash

SPECFILE=lightdm-remote-session-uccsconfigure.spec
MULTILIB=false
DO_NOT_INSTALL=('lightdm-remote-session-uccsconfigure-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
