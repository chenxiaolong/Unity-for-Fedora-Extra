#!/usr/bin/env bash

SPECFILE=lo-menubar.spec
MULTILIB=false
DO_NOT_INSTALL=('libreoffice-menubar-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
