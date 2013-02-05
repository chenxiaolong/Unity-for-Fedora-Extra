#!/usr/bin/env bash

SPECFILE=thin-client-config-agent.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "spec file version: $(get_spec_version)"
echo -e "Upstream version:  (none)"
echo -e "Ubuntu version:    $(get_ubuntu_version thin-client-config-agent ${1:-raring} native)"
