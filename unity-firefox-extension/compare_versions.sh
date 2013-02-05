#!/usr/bin/env bash

SPECFILE=unity-firefox-extension.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version unity-firefox-extension)"
echo -e "Ubuntu version:    $(get_ubuntu_version unity-firefox-extension ${1:-raring})"
