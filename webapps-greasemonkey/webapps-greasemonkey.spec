# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

# Upstream package name is webapps-greasemonkey
# Ubuntu's package name is xul-ext-websites-integration

%global debug_package %{nil}

Name:		webapps-greasemonkey
Version:	2.3.4
Release:	1%{?dist}
Summary:	Firefox extension to support user scripts

Group:		User Interface/Desktops
License:	MIT and BSD
URL:		https://launchpad.net/webapps-greasemonkey
Source0:	https://launchpad.net/webapps-greasemonkey/trunk/%{version}/+download/webapps-greasemonkey-%{version}.tar.gz

BuildRequires:	unzip

# Uses libdir
#BuildArch:	noarch

%description
(no files)


%package -n firefox-websites-integration
Summary:	Firefox extension to support user scripts
Group:		User Interface/Desktops

Requires:	firefox
Requires:	libunity-webapps

%description -n firefox-websites-integration
This package contains a Firefox extension which allows Unity to integrate with
websites.


%prep
%setup -q


%build
./build.sh
echo "$(date +%Y.%m.%d)" > build_date


%install
EMID=$(sed -n 's/.*<em:id>\(.*\)<\/em:id>.*/\1/p' install.rdf | head -1)
install -dm755 $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/

unzip webapps-$(cat build_date).beta.xpi -d \
  $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/

rm $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/LICENSE.*


%files -n firefox-websites-integration
%doc LICENSE.bsd LICENSE.mit LICENSE.mpl
%{_libdir}/firefox/extensions/*/


%changelog
* Thu Oct 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.3.4-1
- Initial release
- Version 2.3.4
