# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		python-defer
Version:	1.0.6
Release:	1%{?dist}
Summary:	Small framework for asynchronous programming

Group:		System Environment/Libraries
License:	GPLv2+
URL:		https://launchpad.net/python-defer
Source0:	https://launchpad.net/python-defer/trunk/%{version}/+download/defer-%{version}.tar.gz
Source1:	0001_Python_3_fix.patch

BuildRequires:	python-devel
BuildRequires:	python3-devel
BuildRequires:	python-setuptools
BuildRequires:	python3-setuptools

BuildArch:	noarch

%description
Small framework for asynchronous programming in Python. It is a stripped down
version of Twisted's defer.


%package -n python3-defer
Summary:	Small framework for asynchronous programming
Group:		System Environment/Libraries

%description -n python3-defer
Small framework for asynchronous programming in Python. It is a stripped down
version of Twisted's defer.



%prep
%setup -q -n defer-%{version}


%install
%{__python} setup.py install --root $RPM_BUILD_ROOT
patch -Np1 -i '%{SOURCE1}'
%{__python3} setup.py install --root $RPM_BUILD_ROOT


%files
%doc AUTHORS NEWS README README.tests
%{python_sitelib}/defer/
%{python_sitelib}/defer-%{version}-py*.egg-info/


%files -n python3-defer
%doc AUTHORS NEWS README README.tests
%{python3_sitelib}/defer/
%{python3_sitelib}/defer-%{version}-py*.egg-info/


%changelog
* Tue Sep 25 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0.6-1
- Initial release
- Version 1.0.6
