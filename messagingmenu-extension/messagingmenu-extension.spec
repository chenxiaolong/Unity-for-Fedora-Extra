# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _bzr_rev 145

Name:		thunderbird-messagingmenu
Version:	1.0
Release:	2%{?dist}
Summary:	Messaging Menu Thunderbird Extension

Group:		User Interface/Desktops
License:	MPLv1.1
URL:		https://launchpad.net/messagingmenu-extension
Source0:	messagingmenu-extension-bzr%{_bzr_rev}.tar.xz
# Create source 0 by running this script (change _bzr_rev above as needed)
Source1:	create-source-from-bzr-rev.sh

BuildRequires:	unzip

Requires:	glib2
Requires:	gtk2
Requires:	indicator-messages
Requires:	libdbusmenu-glib
Requires:	libindicate
Requires:	libunity
Requires:	thunderbird

%description
This package provides an extension for Thunderbird that allows it to integrate
with the messaging menu.


%prep
%setup -q -n messagingmenu-extension-bzr%{_bzr_rev}


%build
./build.sh


%install
EMID_GLOBAL=$(sed -n 's/^.*<em:id>\(.*\)<\/em:id>/\1/p' install.rdf | head -n 1)

DIR_THUNDERBIRD=$RPM_BUILD_ROOT%{_libdir}/thunderbird/extensions/${EMID_GLOBAL}

install -dm755 ${DIR_THUNDERBIRD}

unzip messagingmenu.xpi -d ${DIR_THUNDERBIRD}

install -dm755 $RPM_BUILD_ROOT%{_datadir}/indicators/messages/applications/
echo "/usr/share/applications/mozilla-thunderbird.desktop" > \
  $RPM_BUILD_ROOT%{_datadir}/indicators/messages/applications/thunderbird


%files
%{_libdir}/thunderbird/extensions/*/
%dir %{_datadir}/indicators/
%dir %{_datadir}/indicators/messages/
%dir %{_datadir}/indicators/messages/applications/
%{_datadir}/indicators/messages/applications/thunderbird


%changelog
* Wed Oct 03 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-2
- Add %{_datadir}/indicators/messages/applications/thunderbird
  - Otherwise, indicator-messages won't detect Thunderbird

* Tue Oct 02 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-1
- Initial release
- Version 1.0 (bzr rev 145 tags this release)
