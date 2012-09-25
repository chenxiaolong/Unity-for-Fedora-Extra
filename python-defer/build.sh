#!/usr/bin/env bash

SPECFILE=python-defer.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
