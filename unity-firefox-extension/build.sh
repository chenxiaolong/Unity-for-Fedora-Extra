#!/usr/bin/env bash

SPECFILE=unity-firefox-extension.spec
MULTILIB=false
DO_NOT_INSTALL=('unity-firefox-extension-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
