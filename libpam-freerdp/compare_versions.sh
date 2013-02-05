#!/usr/bin/env bash

SPECFILE=libpam-freerdp.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version libpam-freerdp)"
echo -e "Ubuntu version:    $(get_ubuntu_version libpam-freerdp ${1:-raring})"
