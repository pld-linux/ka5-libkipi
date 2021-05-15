%define		kdeappsver	21.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		libkipi

Summary:	Kipi library
Summary(pl.UTF-8):	Biblioteka kipi
Name:		ka5-%{kaname}
Version:	21.04.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	bcf3383ae23c9bc003421cf1d6b0cebe
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	libkipi <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kipi library.

%description -l pl.UTF-8
Biblioteka kipi.

%package devel
Summary:	Header files for libkipi development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdegraphics-devel < 4.6.99
Obsoletes:	libkipi-devel <= 4.8.0

%description devel
Header files for libkipi development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKF5Kipi.so.32.0.0
%attr(755,root,root) %{_libdir}/libKF5Kipi.so.5.2.0
%attr(755,root,root) %{_libdir}/qt5/plugins/kipiplugin_kxmlhelloworld.so
%{_iconsdir}/hicolor/128x128/apps/kipi.png
%{_iconsdir}/hicolor/16x16/apps/kipi.png
%{_iconsdir}/hicolor/22x22/apps/kipi.png
%{_iconsdir}/hicolor/32x32/apps/kipi.png
%{_iconsdir}/hicolor/48x48/apps/kipi.png
%{_datadir}/kservices5/kipiplugin_kxmlhelloworld.desktop
%{_datadir}/kservicetypes5/kipiplugin.desktop
%dir %{_datadir}/kxmlgui5/kipi
%{_datadir}/kxmlgui5/kipi/kipiplugin_kxmlhelloworldui.rc


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIPI
%{_includedir}/KF5/libkipi_version.h
%{_libdir}/cmake/KF5Kipi
%{_libdir}/libKF5Kipi.so
