#!/usr/bin/env bash

SPECFILE=ubuntu-sounds.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
