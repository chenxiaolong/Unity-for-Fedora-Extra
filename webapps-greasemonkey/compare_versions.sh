#!/usr/bin/env bash

SPECFILE=webapps-greasemonkey.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version webapps-greasemonkey)"
echo -e "Ubuntu version:    $(get_ubuntu_version webapps-greasemonkey ${1:-raring})"
