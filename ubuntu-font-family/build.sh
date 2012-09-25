#!/usr/bin/env bash

SPECFILE=ubuntu-font-family.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
