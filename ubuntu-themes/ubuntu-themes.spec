# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		ubuntu-themes
Version:	13.04daily13.02.04
Release:	1%{?dist}
Summary:	Ubuntu monochrome icon theme, Ambiance and Radiance themes, and Ubuntu artwork

Group:		User Interface/Desktops
License:	CC-BY-SA
URL:		https://launchpad.net/ubuntu-themes
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-themes_%{version}.orig.tar.gz

BuildRequires:	icon-naming-utils
BuildRequires:	ImageMagick
BuildRequires:	python2

Requires:	dmz-cursor-themes
Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme
Requires:	humanity-icon-theme

Requires:	gtk-murrine-engine
Requires:	gtk-unico-engine

BuildArch:	noarch

%description
This package contains the Ubuntu Monochrome icon theme, the Ambiance and
Radiance GTK themes, and Ubuntu artwork.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
install -dm755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -av Ambiance/ Radiance $RPM_BUILD_ROOT%{_datadir}/themes/

install -dm755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -av ubuntu-mono-dark/ ubuntu-mono-light/ LoginIcons/ \
  $RPM_BUILD_ROOT%{_datadir}/icons/

install -Dm644 distributor-logo.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/distributor-logo.png


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ ${1} -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(0644,root,root,0755)
%{_datadir}/themes/Ambiance/
%{_datadir}/themes/Radiance/
%{_datadir}/icons/hicolor/48x48/apps/distributor-logo.png
%{_datadir}/icons/ubuntu-mono-dark/
%{_datadir}/icons/ubuntu-mono-light/
%{_datadir}/icons/LoginIcons/


%changelog
* Tue Feb 05 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 13.04daily13.02.04-1
- Initial release
- Version 13.04daily13.02.04
