# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		sound-theme-ubuntu
Version:	0.13
Release:	1%{?dist}
Summary:	Ubuntu's sound theme

Group:		User Interface/Desktops
License:	CC-BY-SA
URL:		https://launchpad.net/ubuntu-sounds
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-sounds_%{version}.tar.gz

BuildRequires:	vorbis-tools

BuildArch:	noarch

%description
This package contains Ubuntu's sound theme used in Ubuntu 11.04 through 12.10.


%prep
%setup -q -n ubuntu-sounds-%{version}


%build
./convert.sh


%install
find ubuntu/ -type f -exec \
  install -Dm644 {} $RPM_BUILD_ROOT%{_datadir}/sounds/{} \;
ln -s dialog-question.ogg \
  $RPM_BUILD_ROOT%{_datadir}/sounds/ubuntu/stereo/system-ready.ogg


%files
%doc COPYING
%{_datadir}/sounds/ubuntu/


%changelog
* Mon Sep 24 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.13-1
- Initial release
- Version 0.13
