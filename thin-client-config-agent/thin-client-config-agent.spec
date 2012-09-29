# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		thin-client-config-agent
Version:	0.6
Release:	1%{?dist}
Summary:	Retrieve the list of remote desktop servers for a user

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/thin-client-config-agent
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/thin-client-config-agent_%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-pycurl
BuildRequires:	python3-setuptools

BuildRequires:	pkgconfig(python3)

Requires:	python3-pycurl

%description
This package contains a tool to retrieve the list of remote desktop servers for
a user from a master server, such as Landscape.


%prep
%setup -q -n %{name}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README
%{python3_sitelib}/tccalib/
%{python3_sitelib}/thin_client_config_agent-%{version}-py*.egg-info/


%changelog
* Fri Sep 28 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.6-1
- Initial release
- Version 0.6
