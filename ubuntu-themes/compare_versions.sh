#!/usr/bin/env bash

SPECFILE=ubuntu-themes.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "PKGBUILD version: $(get_spec_version)"
echo -e "Upstream version: (none)"
echo -e "Ubuntu version:   $(get_ubuntu_version ubuntu-themes ${1:-raring})"
