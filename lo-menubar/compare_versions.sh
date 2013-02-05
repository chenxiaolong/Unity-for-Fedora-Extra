#!/usr/bin/env bash

SPECFILE=lo-menubar.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version lo-menubar)"
echo -e "Ubuntu version:    $(get_ubuntu_version lo-menubar ${1:-raring})"
