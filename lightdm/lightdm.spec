### This is a copy of the Fedora 18 lightdm spec file with a few Ubuntu patches
### added. This package can be dropped when the patches are upstreamed.

%if 0%{?fedora} > 17
# conditionalize systemd unit support (consider -systemd subpkg? --rex)
%define systemd 1
%endif

Name:    lightdm
Summary: Lightweight Display Manager
Version: 1.3.3
Release: 100%{?dist}

# library/bindings are LGPLv3, the rest GPLv3+
License: LGPLv3+ and GPLv3+
#URL:     http://www.freedesktop.org/wiki/Software/LightDM
URL:     https://launchpad.net/lightdm/
Source0: https://launchpad.net/lightdm/1.4/%{version}/+download/lightdm-%{version}.tar.gz
Source1: lightdm.pam
Source2: lightdm-autologin.pam
Source3: lightdm-tmpfiles.conf
Source4: lightdm.service
Source5: lightdm.preset

Patch0: lightdm-lock-screen-before-switch.patch
## Downstream patches:
Patch10: lightdm-1.3.1-fedora_config.patch
# hack in support for --nodaemon option
Patch11: lightdm-1.2.2-nodaemon_option.patch

Patch20:	03_launch_dbus.patch
Patch21:	06_add_remote_login_hint.patch
Patch22:	07_fix_types_in_vapi.patch

BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: gtk-doc itstool
BuildRequires: intltool
BuildRequires: pam-devel
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gio-2.0) >= 2.26
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: vala

Requires: %{name}-gobject%{?_isa} = %{version}-%{release}
Requires: accountsservice
## this seems to still be a hard-requirement for now, at least
## until support for systemd restart/shutdown is implemented
#if 0%{?fedora} < 17
Requires: ConsoleKit
#endif
Requires: dbus-x11
# aka /sbin/shutdown, and friends
Requires: systemd
Requires: xorg-x11-xinit

Requires(pre): shadow-utils

# beware of bootstrapping -- rex
# leaving this here, means greeters will have to require lightdm too,
# instead of relying on -gobject, -qt to pull it in
Requires: lightdm-greeter = 1.2

# needed for anaconda to boot into runlevel 5 after install
Provides: service(graphical-login) = lightdm

%if 0%{?systemd}
BuildRequires:    systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%endif

%description
LightDM is an X display manager that:
* Has a lightweight codebase
* Is standards compliant (PAM, ConsoleKit, etc)
* Has a well defined interface between the server and user interface
* Fully themeable (easiest with the webkit interface)
* Cross-desktop (greeters can be written in any toolkit)

%package gobject
Summary: LightDM GObject client library
# omit base package, to allow for easier bootstrapping
# requires greeters to manually
# Requires: lightdm
#Requires: %{name} = %{version}-%{release}
%description gobject
This package contains a GObject based library for LightDM clients to use to
interface with LightDM.

%package gobject-devel
Summary: Development files for %{name}-gobject
Requires: %{name}-gobject%{?_isa} = %{version}-%{release}
%description gobject-devel
%{summary}.

%package qt
Summary: LightDM QT client library
# see comment in -gobject above
#Requires: %{name} = %{version}-%{release}
%description qt
This package contains a QT based library for LightDM clients to use to interface
with LightDM.

%package qt-devel
Summary: Development files for %{name}-qt
Requires: %{name}-qt%{?_isa} = %{version}-%{release}
%description qt-devel
%{summary}.


%prep
%setup -q

%patch0 -p1 -b .lock-screen
%patch10 -p1 -b .fedora_config
%patch11 -p1 -b .nodaemon_option

%patch20 -p1 -b .launch_dbus
%patch21 -p1 -b .remote_login
%patch22 -p1 -b .vapi_types


# rpath hack
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure


%build
%configure \
  --disable-static \
  --enable-gtk-doc \
  --enable-introspection \
  --with-greeter-user=lightdm \
  --with-greeter-session=lightdm-greeter

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

find %{buildroot} -name 'lib*.la' -exec rm -fv {} ';'

# We don't ship AppAmor
rm -rfv %{buildroot}%{_sysconfdir}/apparmor.d/

# install pam file
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/lightdm
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin

install -Dpm 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/tmpfiles.d/lightdm.conf

# We need to own these
#mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}/{authority,dmrc}
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}/
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}/authority
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}

%find_lang %{name} --with-gnome

%if 0%{?systemd}
install -m644 -p -D %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/lightdm.service
install -m644 -p -D %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}-preset/82-fedora-lightdm.preset
%endif


%pre
getent group lightdm >/dev/null || groupadd -r lightdm
getent passwd lightdm >/dev/null || \
  /usr/sbin/useradd -g lightdm -M -d /var/log/lightdm -s /sbin/nologin -r lightdm > /dev/null 2>&1
## ignore errors, as we can't disambiguate between lightdm already existed
## and couldn't create account with the current adduser.
exit 0

%if 0%{?systemd}
%post
%systemd_post lightdm.service

%preun
%systemd_preun lightdm.service

%postun
%systemd_postun
%endif

%files -f %{name}.lang
%doc COPYING
%doc ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%config(noreplace) %{_sysconfdir}/init/lightdm.conf
%config(noreplace) %{_sysconfdir}/pam.d/lightdm*
%dir %{_sysconfdir}/lightdm/
%config(noreplace) %{_sysconfdir}/lightdm/keys.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf
%config(noreplace) %{_sysconfdir}/lightdm/users.conf
%{_bindir}/dm-tool
%{_sbindir}/lightdm
%{_libexecdir}/lightdm/
%{_libdir}/girepository-1.0/LightDM-1.typelib
%{_mandir}/man*/lightdm.*.*
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/cache/lightdm/
%if 0%{?systemd}
%{_unitdir}/lightdm.service
%{_unitdir}-preset/82-fedora-lightdm.preset
%endif

# because of systemd
%{_prefix}/lib/tmpfiles.d/lightdm.conf
%ghost %dir %{_localstatedir}/run/lightdm

%dir %attr(-,lightdm,lightdm) %{_localstatedir}/lib/lightdm/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/log/lightdm/

%post gobject -p /sbin/ldconfig
%postun gobject -p /sbin/ldconfig

%files gobject
# no LGPLv3+ license file included
%{_libdir}/liblightdm-gobject-1.so.0*

%files gobject-devel
%doc %{_datadir}/gtk-doc/html/lightdm-gobject-1/
%{_includedir}/lightdm-gobject-1/
%{_libdir}/liblightdm-gobject-1.so
%{_libdir}/pkgconfig/liblightdm-gobject-1.pc
%{_datadir}/gir-1.0/LightDM-1.gir
%{_datadir}/vala/vapi/liblightdm-gobject-1.vapi

%post qt -p /sbin/ldconfig
%postun qt -p /sbin/ldconfig

%files qt
# no LGPLv3+ license file included
%{_libdir}/liblightdm-qt-2.so.0*

%files qt-devel
%{_includedir}/lightdm-qt-2/
%{_libdir}/liblightdm-qt-2.so
%{_libdir}/pkgconfig/liblightdm-qt-2.pc


%changelog
* Sat Sep 29 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.3.3-100
- Add some Ubuntu patches

* Tue Sep 04 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-2
- lightdm.service: After=+livesys-late.service (#853985)

* Thu Aug 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.3.3-1
- lightdm-1.3.3
- ship systemd preset for lightdm (#852845)

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.3.2-7
- conditionalize systemd unit support
- lightdm.pam: +-session optional pam_ck_connector.so

* Tue Aug  7 2012 Lennart Poettering <lpoetter@redhat.com> - 1.3.2-6
- Add bus name to service file

* Tue Aug  7 2012 Lennart Poettering <lpoetter@redhat.com> - 1.3.2-5
- Display Manager Rework
- https://fedoraproject.org/wiki/Features/DisplayManagerRework
- https://bugzilla.redhat.com/show_bug.cgi?id=846153

* Tue Jul 24 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.3.2-4
- import working lightdm-autologin pam config

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.3.2-2
- comply with guidelines concerning user and group handling

* Fri Jul 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-1
- lightdm-1.3.2

* Sun Jul 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-2
- lightdm.conf: minimum-vt=1 (allows for better plymouth no vt-switch)

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-1
- lightdm-1.3.1

* Fri Jun 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-15
- default to alternatives-provided greeter

* Thu Jun 14 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 1.2.2-14
- check if lightdm user exists, before creating him
- reset patch numbering
- use standard dir perm

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-13
- Requires: lightdm-greeter = 1.2

* Tue Jun 12 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-12
- move headers into -qt-devel pkg

* Mon Jun 11 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-11
- License: LGPLv3+ and GPLv3+
- make dbus files %%config
- gobject-devel, qt-devel subpkgs

* Mon May 14 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-10
- move /etc/tmpfiles.d/* => /usr/lib/tempfiles.d/

* Wed May 09 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-9
- fix typo, Requires: accountsservice

* Thu Apr 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-8
- Requires: accountservice ConsoleKit systemd

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-7
- respin nodaemon_option patch

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-6
- Requires: xorg-x11-xinit
- Requires: lightdm-greeter
- -gobject,-qt: drop dep on base pkg (easier for bootstrapping)

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-5
- make sane default lightdm.conf for fedora
- nodaemon_option.patch
- Requires: xorg-x11-xinit

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-4
- update lightdm.pam
- make /var/log/lightdm /var/lib/lightdm group-writable too

* Wed Apr 25 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-3
- omit useless %%post(un) scriptlets
- %%pre: add lightdm user/group
- BR: gnome-common
- %%build: --with-greeter-session=lightdm-gtk-greeter (for now)

* Tue Apr 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-2
- pkgconfig-style deps

* Tue Apr 24 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-1
- 1.2.2

* Fri Feb 17 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Fri Feb 17 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- Make build verbose

* Sun Oct 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Aug 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Fri Jul 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Jul 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sat Jun 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Apr 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sun Jan 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sat Oct 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Initial package
