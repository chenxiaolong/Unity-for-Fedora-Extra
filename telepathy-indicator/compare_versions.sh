#!/usr/bin/env bash

SPECFILE=telepathy-indicator.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version telepathy-indicator)"
echo -e "Ubuntu version:    $(get_ubuntu_version telepathy-indicator ${1:-raring})"
