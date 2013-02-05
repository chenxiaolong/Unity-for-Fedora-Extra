#!/usr/bin/env bash

SPECFILE=unity-greeter.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "PKGBUILD version: $(get_spec_version) $(get_spec_release --ubuntu)"
echo -e "Upstream version: $(get_launchpad_version unity-greeter)"
echo -e "Ubuntu version:   $(get_ubuntu_version unity-greeter ${1:-raring})"
