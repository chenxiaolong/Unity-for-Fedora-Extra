# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		ubuntu-mono-icon-theme
Version:	0.0.42
Release:	1%{?dist}
Summary:	Icons for the panel, designed in a simplified monochrome style

Group:		User Interface/Desktops
License:	CC-BY-SA
URL:		https://launchpad.net/ubuntu-mono
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-mono_%{version}.tar.gz

BuildRequires:	ImageMagick
BuildRequires:	python2

Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme
Requires:	humanity-icon-theme

Provides:	monochrome-icon-theme = %{version}-%{release}

BuildArch:	noarch

%description
This package contains the default Ubuntu icon theme, a theme that uses
monochrome icons for the panel.


%prep
%setup -q -n ubuntu-mono-%{version}


%build
make %{?_smp_mflags}


%install
# Install icons
install -dm755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -av ubuntu-mono-dark $RPM_BUILD_ROOT%{_datadir}/icons/
cp -av ubuntu-mono-light $RPM_BUILD_ROOT%{_datadir}/icons/
cp -av LoginIcons $RPM_BUILD_ROOT%{_datadir}/icons/

for i in $RPM_BUILD_ROOT%{_datadir}/icons/ubuntu-mono-*; do
  cp -avt ${i} debian/places/
done


%files
%doc debian/copyright
%{_datadir}/icons/LoginIcons/
%{_datadir}/icons/ubuntu-mono-dark/
%{_datadir}/icons/ubuntu-mono-light/


%changelog
* Thu Aug 29 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.0.42-1
- Initial release
- Version 0.0.42
