#!/usr/bin/env bash

SPECFILE=globalmenu-extension.spec
NO_BASE_PACKAGE=true
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
