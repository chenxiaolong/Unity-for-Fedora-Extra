# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu4

Name:		lightdm-guest-session
Version:	1.3.3
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	Guest Session Support for LightDM

Group:		User Interface/X
License:	GPLv3+
URL:		https://launchpad.net/ubuntu/+source/lightdm
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/lightdm_%{version}-%{_ubuntu_rel}.diff.gz

Patch0:		guest-session-cross-distro.patch

Requires:	lightdm

BuildArch:	noarch

%description
This package includes a modified version of the guest-account script for Ubuntu.


%prep
%setup -q -T -c

zcat '%{SOURCE0}' | patch -Np1
%patch0 -p1 -b .other-distro


%install
install -dm755 $RPM_BUILD_ROOT%{_sbindir}/
install -m755 debian/guest-account $RPM_BUILD_ROOT%{_sbindir}/


%files
%{_sbindir}/guest-account


%changelog
* Sat Sep 29 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.3.3-1.0ubuntu4
- Initial release
- Version 1.3.3
- Ubuntu release 0ubuntu4
