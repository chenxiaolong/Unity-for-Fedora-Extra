#!/usr/bin/env bash

SPECFILE=messagingmenu-extension.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
