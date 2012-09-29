#!/usr/bin/env bash

SPECFILE=lightdm-guest-session.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
