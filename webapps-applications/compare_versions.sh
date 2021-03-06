#!/usr/bin/env bash

SPECFILE=webapps-applications.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version) $(get_spec_release --ubuntu)"
echo -e "Upstream version:  $(get_launchpad_version webapps-applications webapps)"
echo -e "Ubuntu version:    $(get_ubuntu_version webapps-applications ${1:-raring})"
