#!/usr/bin/env bash

SPECFILE=webaccounts-browser-extension.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version) $(get_spec_release --ubuntu)"
echo -e "Upstream version:  $(get_launchpad_version webaccounts-browser-extension)"
echo -e "Ubuntu version:    $(get_ubuntu_version webaccounts-browser-extension ${1:-raring})"
