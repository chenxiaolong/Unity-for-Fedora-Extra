#!/usr/bin/env bash

SPECFILE=remote-login-service.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version remote-login-service)"
echo -e "Ubuntu version:    $(get_ubuntu_version remote-login-service ${1:-raring})"
