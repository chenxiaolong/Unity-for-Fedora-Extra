#!/usr/bin/env bash

SPECFILE=telepathy-indicator.spec
MULTILIB=false
DO_NOT_INSTALL=('telepathy-indicator-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
