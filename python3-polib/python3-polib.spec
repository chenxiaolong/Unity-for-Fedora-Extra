# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

# Partially based on Fedora 18's python-polib spec file

Name:		python3-polib
Version:	1.0.1
Release:	1%{?dist}
Summary:	A library to parse and manage gettext catalogs

Group:		Development/Languages
License:	MIT
URL:		http://bitbucket.org/izi/polib/
Source0:	http://bitbucket.org/izi/polib/downloads/polib-%{version}.tar.gz

BuildRequires:	python3

BuildArch:	noarch

%description
polib allows you to manipulate, create, modify gettext files (pot, po and mo
files). You can load existing files, iterate through it's entries, add, modify
entries, comments or metadata, etc... or create new po files from scratch.

polib provides a simple and pythonic API, exporting only three convenience
functions 'pofile', 'mofile' and 'detect_encoding', and the 4 core classes:
POFile, MOFile, POEntry and MOEntry for creating new files/entries.


%prep
%setup -q -n polib-%{version}


%build
export LANG=en_US.UTF-8
%{__python3} setup.py build


%install
export LANG=en_US.UTF-8
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc CHANGELOG LICENSE README.rst
%{python3_sitelib}/polib-%{version}-py3.*.egg-info
%{python3_sitelib}/polib.py
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/polib.cpython-3*.py*


%changelog
* Thu Oct 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0.1-1
- Initial release
- Version 1.0.1
