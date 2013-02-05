#!/usr/bin/env bash

SPECFILE=lightdm-remote-session-uccsconfigure.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  $(get_launchpad_version lightdm-remote-session-uccsconfigure)"
echo -e "Ubuntu version:    $(get_ubuntu_version lightdm-remote-session-uccsconfigure ${1:-raring})"
