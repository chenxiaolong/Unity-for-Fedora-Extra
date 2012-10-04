#!/usr/bin/env bash

SPECFILE=webapps-greasemonkey.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
