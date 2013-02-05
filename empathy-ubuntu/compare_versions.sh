#!/usr/bin/env bash

SPECFILE=empathy-ubuntu-Fedora_18.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "F18 spec version: $(get_spec_version) $(get_spec_release --ubuntu)"
echo -e "Fedora version:   $(get_fedora_version empathy 18)"
echo -e "Upstream version: $(get_gnome_version empathy 3.6)"
echo -e "Ubuntu version:   $(get_ubuntu_version empathy ${1:-raring})"
