# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

# This package is called online-accounts-browser-extension upstream

%define _ubuntu_rel 0ubuntu4

Name:		webaccounts-browser-extension
Version:	0.4.5
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	Web Accounts extension for FF and Chromium

Group:		User Interface/Desktops
License:	GPLv2+
URL:		https://launchpad.net/online-accounts-browser-extension
Source0:	https://launchpad.net/online-accounts-browser-extension/trunk/%{version}/+download/webaccounts-browser-extension-%{version}.tar.gz

Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/webaccounts-browser-extension_%{version}-%{_ubuntu_rel}.debian.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	openssl
# Hmm?
#BuildRequires:	vim
BuildRequires:	zip

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libaccounts-glib)

%description
(contains no files)


%package -n webaccounts-extension-common
Summary:	Common files for the Firefox and Chromium webaccounts extensions
Group:		User Interface/Desktops

%description -n webaccounts-extension-common
This package contains the common files needed by both the Firefox and Chromium
webaccounts extensions.


%package -n webaccounts-chromium-extension
Summary:	Ubuntu Online Accounts extension for Chromium
Group:		User Interface/Desktops

Requires:	webaccounts-extension-common = %{version}-%{release}
Requires:	gnome-control-center-signon
# Google Chrome is supported too
#Requires:	chromium-browser
#Requires:	chromium

%description -n webaccounts-chromium-extension
This package contains the Ubuntu Online Accounts extension for Chromium and
Google Chrome.


%package -n firefox-webaccounts
Summary:	Ubuntu Online Accounts extension for Firefox
Group:		User Interface/Desktops

Requires:	webaccounts-extension-common = %{version}-%{release}
Requires:	firefox
Requires:	gnome-control-center-signon

%description -n firefox-webaccounts
This package contains the Ubuntu Online Accounts extension for Firefox.


%prep
%setup -q

tar zxvf '%{SOURCE99}'
cp debian/webaccounts.pem .

autoreconf -vfi


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Make the Chromium extension work for Google Chrome too
install -dm755 $RPM_BUILD_ROOT%{_datadir}/google-chrome/extensions/
ln -s %{_datadir}/chromium/extensions/egllpaionoammpdioefpakaanmhocgca.json \
  $RPM_BUILD_ROOT%{_datadir}/google-chrome/extensions/

# Unpack Firefox extension
EMID=$(sed -n 's/.*<em:id>\(.*\)<\/em:id>.*/\1/p' \
  firefox-extension/install.rdf | head -1)
install -dm755 $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/
unzip \
  $RPM_BUILD_ROOT%{_libdir}/webaccounts-firefox/webaccounts-firefox-extension.xpi \
  -d $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/
rm $RPM_BUILD_ROOT%{_libdir}/webaccounts-firefox/webaccounts-firefox-extension.xpi

# Remove libtool files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete


%postun
if [ ${1} -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%files -n webaccounts-extension-common
%doc COPYING
%dir %{_libdir}/webaccounts-browser-extension/
%{_libdir}/webaccounts-browser-extension/libwebaccounts.so
%{_libdir}/webaccounts-browser-extension/libwebaccounts-%{version}.so
%{_datadir}/glib-2.0/schemas/com.canonical.webcredentials.capture.gschema.xml


%files -n webaccounts-chromium-extension
%dir %{_libdir}/webaccounts-chromium/
%{_libdir}/webaccounts-chromium/webaccounts.crx
%dir %{_datadir}/chromium/
%dir %{_datadir}/chromium/extensions/
%{_datadir}/chromium/extensions/egllpaionoammpdioefpakaanmhocgca.json
%dir %{_datadir}/google-chrome/
%dir %{_datadir}/google-chrome/extensions/
%{_datadir}/google-chrome/extensions/egllpaionoammpdioefpakaanmhocgca.json


%files -n firefox-webaccounts
%{_libdir}/firefox/extensions/online-accounts@lists.launchpad.net/


%changelog
* Tue Feb 05 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.4.5-1.0ubuntu4
- Version 0.4.5
- Ubuntu release 0ubuntu4

* Thu Oct 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.4.4-1.0ubuntu1
- Initial release
- Version 0.4.4
- Ubuntu release 0ubuntu1
