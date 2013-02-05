#!/usr/bin/env bash

SPECFILE=python3-polib.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
UPSTREAM_VER=$(wget -q 'https://bitbucket.org/izi/polib/downloads' -O - | sed -n 's/.*>polib-\(.*\)\.tar\.gz<.*/\1/p' | head -n 1)
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    $(get_ubuntu_version polib ${1:-raring})"
