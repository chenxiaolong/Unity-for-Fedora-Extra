#!/usr/bin/env bash

SPECFILE=ubuntu-mono.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
