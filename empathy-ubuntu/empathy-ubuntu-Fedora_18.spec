# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu1

Name:		empathy
Version:	3.6.0
Release:	100.%{_ubuntu_rel}%{?dist}
Summary:	Instant Messaging Client for GNOME

#Group:		
License:	GPLv2+
URL:		http://live.gnome.org/Empathy
Source0:	http://download.gnome.org/sources/empathy/3.6/empathy-%{version}.tar.xz

Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/empathy_%{version}-%{_ubuntu_rel}.debian.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	yelp-tools

BuildRequires:	pkgconfig(account-plugin)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:	pkgconfig(cheese-gtk)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gst-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
#BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
#BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(folks-telepathy)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(geoclue)
#BuildRequires:	pkgconfig(geocode-glib)
BuildRequires:	pkgconfig(glib-2.0)
#BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-audio-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libaccounts-glib)
BuildRequires:	pkgconfig(libcanberra-gtk3)
#BuildRequires:	pkgconfig(libgee-1.0)
# Maybe
BuildRequires:	pkgconfig(libgnome-control-center)
BuildRequires:	pkgconfig(libido3-0.1)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsignon-glib)
#BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mission-control-plugins)
BuildRequires:	pkgconfig(nautilus-sendto)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(unity)
BuildRequires:	pkgconfig(webkitgtk-3.0)
#BuildRequires:	pkgconfig(x11)

Requires:	gnome-control-center-signon
Requires:	signon-plugins
Requires:	telepathy-filesystem
Requires:	telepathy-mission-control
Requires:	telepathy-gabble
Requires:	telepathy-haze
Requires:	telepathy-idle
Requires:	telepathy-salut

Provides:	empathy-ubuntu = %{version}-%{release}

%description
Empathy is powerful multi-protocol instant messaging client which supports
Jabber, GTalk, MSN, IRC, Salut, and other protocols. It is built on top of the
Telepathy framework.


%package -n account-plugin-aim
Summary:        GNOME Control Center account plugin for Single Sign On - AIM

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-aim
This package contains the GNOME Control Center account plugin for signing on to
AIM.


%package -n account-plugin-gadugadu
Summary:        GNOME Control Center account plugin for Single Sign On - Gadu-Gadu

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-gadugadu
This package contains the GNOME Control Center account plugin for signing on to
Gadu-Gadu.


%package -n account-plugin-groupwise
Summary:        GNOME Control Center account plugin for Single Sign On - GroupWise

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-groupwise
This package contains the GNOME Control Center account plugin for signing on to
GroupWise.


%package -n account-plugin-icq
Summary:        GNOME Control Center account plugin for Single Sign On - ICQ

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-icq
This package contains the GNOME Control Center account plugin for signing on to
ICQ.


%package -n account-plugin-irc
Summary:        GNOME Control Center account plugin for Single Sign On - IRC

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-idle

%description -n account-plugin-irc
This package contains the GNOME Control Center account plugin for signing on to
IRC servers.


%package -n account-plugin-jabber
Summary:        GNOME Control Center account plugin for Single Sign On - Jabber/XMPP

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-gabble

%description -n account-plugin-jabber
This package contains the GNOME Control Center account plugin for signing on to
Jabber or XMPP servers.


%package -n account-plugin-mxit
Summary:        GNOME Control Center account plugin for Single Sign On - Mxit

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-mxit
This package contains the GNOME Control Center account plugin for signing on to
Mxit.


%package -n account-plugin-myspace
Summary:        GNOME Control Center account plugin for Single Sign On - Myspace

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-myspace
This package contains the GNOME Control Center account plugin for signing on to
Myspace.


%package -n account-plugin-salut
Summary:        GNOME Control Center account plugin for Single Sign On - Local XMPP (Salut)

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-salut

%description -n account-plugin-salut
This package contains the GNOME Control Center account plugin for signing on to
Salut.


%package -n account-plugin-sametime
Summary:        GNOME Control Center account plugin for Single Sign On - IBM Sametime

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-sametime
This package contains the GNOME Control Center account plugin for signing on to
Sametime.


%package -n account-plugin-sip
Summary:        GNOME Control Center account plugin for Single Sign On - SIP

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-rakia

%description -n account-plugin-sip
This package contains the GNOME Control Center account plugin for signing on to
SIP servers.


%package -n account-plugin-yahoo
Summary:        GNOME Control Center account plugin for Single Sign On - Yahoo

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-yahoo
This package contains the GNOME Control Center account plugin for signing on to
Yahoo.


%package -n account-plugin-yahoojp
Summary:        GNOME Control Center account plugin for Single Sign On - Yahoo Japan

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-yahoojp
This package contains the GNOME Control Center account plugin for signing on to
Yahoo Japan.


%package -n account-plugin-zephyr
Summary:        GNOME Control Center account plugin for Single Sign On - Zephyr

Requires:	empathy = %{version}-%{release}
Requires:	account-plugin-icons
Requires:	telepathy-haze

%description -n account-plugin-zephyr
This package contains the GNOME Control Center account plugin for signing on to
Zephyr.


%prep
%setup -q

# Apply Ubuntu's patches
tar jxvf '%{SOURCE99}'
for i in $(grep -v '#' debian/patches/series); do
  patch -Np1 -i "debian/patches/${i}"
done

autoreconf -vfi


%build
%configure \
  --disable-static \
  --enable-ubuntu-online-accounts=yes

#make %{?_smp_mflags}
make -j1


%install
make install DESTDIR=$RPM_BUILD_ROOT

install -dm755 $RPM_BUILD_ROOT%{_datadir}/indicators/messages/applications/
install -m644 debian/indicators/empathy \
   $RPM_BUILD_ROOT%{_datadir}/indicators/messages/applications/

sed -i '/NotShowIn/ s/$/;/g' \
  $RPM_BUILD_ROOT%{_datadir}/applications/empathy.desktop
#desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/empathy.desktop

# Remove libtool files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete

%find_lang empathy --with-gnome


%post
touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null || :

%postun
if [ ${1} -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null
  gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%files -f empathy.lang
%doc AUTHORS ChangeLog CONTRIBUTORS NEWS TODO
%doc COPYING COPYING-DOCS COPYING.LGPL COPYING.SHARE-ALIKE
%{_bindir}/empathy
%{_bindir}/empathy-accounts
%{_bindir}/empathy-debugger
%{_libexecdir}/empathy-auth-client
%{_libexecdir}/empathy-call
%{_libexecdir}/empathy-chat
%dir %{_libdir}/empathy/
%{_libdir}/empathy/libempathy.so
%{_libdir}/empathy/libempathy-%{version}.so
%{_libdir}/empathy/libempathy-gtk.so
%{_libdir}/empathy/libempathy-gtk-%{version}.so
%{_libdir}/empathy/libempathy-uoa-account-plugin.so
%{_libdir}/empathy/libempathy-uoa-account-plugin-%{version}.so
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/applications/
%{_libdir}/libaccount-plugin-1.0/applications/libempathy.so
%dir %{_libdir}/mission-control-plugins.0/
%{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%{_libdir}/mission-control-plugins.0/mcp-account-manager-uoa.so
%dir %{_libdir}/nautilus-sendto/
%dir %{_libdir}/nautilus-sendto/plugins/
%{_libdir}/nautilus-sendto/plugins/libnstempathy.so
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/applications/
%{_datadir}/accounts/applications/empathy.application
%dir %{_datadir}/adium/
%dir %{_datadir}/adium/message-styles/
%{_datadir}/adium/message-styles/Boxes.AdiumMessageStyle/
%{_datadir}/adium/message-styles/Classic.AdiumMessageStyle/
%{_datadir}/adium/message-styles/PlanetGNOME.AdiumMessageStyle/
%{_datadir}/applications/empathy.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%{_datadir}/empathy/
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/icons/hicolor/*/apps/empathy.png
%dir %{_datadir}/indicators/
%dir %{_datadir}/indicators/messages/
%dir %{_datadir}/indicators/messages/applications/
%{_datadir}/indicators/messages/applications/empathy
%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client
%{_mandir}/man1/empathy.1.gz
%{_mandir}/man1/empathy-accounts.1.gz


%files -n account-plugin-aim
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libaim.so
%{_datadir}/accounts/providers/aim.provider
%{_datadir}/accounts/services/aim-im.service


%files -n account-plugin-gadugadu
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libgadugadu.so
%{_datadir}/accounts/providers/gadugadu.provider
%{_datadir}/accounts/services/gadugadu-im.service


%files -n account-plugin-groupwise
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libgroupwise.so
%{_datadir}/accounts/providers/groupwise.provider
%{_datadir}/accounts/services/groupwise-im.service


%files -n account-plugin-icq
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libicq.so
%{_datadir}/accounts/providers/icq.provider
%{_datadir}/accounts/services/icq-im.service


%files -n account-plugin-irc
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libirc.so
%{_datadir}/accounts/providers/irc.provider
%{_datadir}/accounts/services/irc-im.service


%files -n account-plugin-jabber
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libjabber.so
%{_datadir}/accounts/providers/jabber.provider
%{_datadir}/accounts/services/jabber-im.service


%files -n account-plugin-mxit
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libmxit.so
%{_datadir}/accounts/providers/mxit.provider
%{_datadir}/accounts/services/mxit-im.service


%files -n account-plugin-myspace
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libmyspace.so
%{_datadir}/accounts/providers/myspace.provider
%{_datadir}/accounts/services/myspace-im.service


%files -n account-plugin-salut
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/liblocal-xmpp.so
%{_datadir}/accounts/providers/local-xmpp.provider
%{_datadir}/accounts/services/local-xmpp-im.service


%files -n account-plugin-sametime
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libsametime.so
%{_datadir}/accounts/providers/sametime.provider
%{_datadir}/accounts/services/sametime-im.service


%files -n account-plugin-sip
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libsip.so
%{_datadir}/accounts/providers/sip.provider
%{_datadir}/accounts/services/sip-im.service


%files -n account-plugin-yahoo
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libyahoo.so
%{_datadir}/accounts/providers/yahoo.provider
%{_datadir}/accounts/services/yahoo-im.service


%files -n account-plugin-yahoojp
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libyahoojp.so
%{_datadir}/accounts/providers/yahoojp.provider
%{_datadir}/accounts/services/yahoojp-im.service


%files -n account-plugin-zephyr
%dir %{_libdir}/libaccount-plugin-1.0/
%dir %{_libdir}/libaccount-plugin-1.0/providers/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%{_libdir}/libaccount-plugin-1.0/providers/libzephyr.so
%{_datadir}/accounts/providers/zephyr.provider
%{_datadir}/accounts/services/zephyr-im.service


%changelog
* Wed Oct 03 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 3.6.0-100.0ubuntu1
- Initial release
- Version 3.6.0
- Ubuntu release 0ubuntu1
