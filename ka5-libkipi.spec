%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		libkipi

Summary:	Kipi library
Summary(pl.UTF-8):	Biblioteka kipi
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	36542096568f918cf58c57c5c3c9004f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.1.0
BuildRequires:	kf5-kservice-devel >= 5.1.0
BuildRequires:	kf5-kxmlgui-devel >= 5.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libdir}/libKF5Kipi.so.32.0.0
%{_libdir}/libKF5Kipi.so.5.2.0
%{_libdir}/qt5/plugins/kipiplugin_kxmlhelloworld.so
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
