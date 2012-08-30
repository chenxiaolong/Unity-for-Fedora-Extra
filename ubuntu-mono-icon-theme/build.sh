#!/usr/bin/env bash

SPECFILE=ubuntu-mono-icon-theme.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
