#!/usr/bin/env bash

SPECFILE=unity-greeter.spec
MULTILIB=false
DO_NOT_INSTALL=('unity-greeter-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
