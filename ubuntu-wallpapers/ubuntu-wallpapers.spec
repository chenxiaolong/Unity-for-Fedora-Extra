# Written by: Xiao-Long chen <chenxiaolong@cxl.epac.to>

Name:		ubuntu-wallpapers
Version:	0.35.2
Release:	1%{?dist}
Summary:	Ubuntu's wallpapers from 9.10 to 12.10

Group:		User Interface/Desktops
License:	CC-BY-SA
URL:		https://launchpad.net/ubuntu-wallpapers
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-wallpapers_%{version}.tar.gz

BuildRequires:	libxslt-devel
BuildRequires:	python-distutils-extra

BuildArch:	noarch

%description
This package contains Ubuntu's wallpapers from Ubuntu 9.10 to Ubuntu 12.10.


%prep
%setup -q


%install
python2 setup.py install --root=$RPM_BUILD_ROOT


%files
%doc AUTHORS
%{python_sitelib}/ubuntu_wallpapers-%{version}-py2.7.egg-info
%dir %{_datadir}/backgrounds/
%dir %{_datadir}/backgrounds/contest/
%{_datadir}/backgrounds/*.jpg
%{_datadir}/backgrounds/warty-final-ubuntu.png
%{_datadir}/backgrounds/contest/*.xml
%{_datadir}/gnome-background-properties/*-wallpapers.xml



%changelog
* Mon Sep 24 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.35.2-1
- Initial release
- Version 0.35.0
