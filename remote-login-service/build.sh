#!/usr/bin/env bash

SPECFILE=remote-login-service.spec
MULTILIB=false
DO_NOT_INSTALL=('remote-login-service-debuginfo')

source "$(dirname ${0})/../internal_builder.sh"
build ${1}
