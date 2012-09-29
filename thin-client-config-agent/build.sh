#!/usr/bin/env bash

SPECFILE=thin-client-config-agent.spec
MULTILIB=false

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
