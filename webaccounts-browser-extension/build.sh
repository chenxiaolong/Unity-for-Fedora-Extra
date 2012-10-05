#!/usr/bin/env bash

SPECFILE=webaccounts-browser-extension.spec
MULTILIB=false
DO_NOT_INSTALL=('webaccounts-browser-extension-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
