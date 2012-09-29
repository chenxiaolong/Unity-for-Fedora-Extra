#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' thin-client-config-agent.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/thin-client-config-agent' -O - | sed -n 's/.*>thin-client-config-agent_\(.*\)\.tar\.gz<.*/\1/p'))

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  (none)"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
