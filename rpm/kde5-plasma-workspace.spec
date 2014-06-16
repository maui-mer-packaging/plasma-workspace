# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kde5-plasma-workspace

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 1 solution for spell checking
Version:    4.97.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source1:    plasma5-desktop.desktop
Source100:  kde5-plasma-workspace.yaml
Source101:  kde5-plasma-workspace-rpmlintrc
Requires:   kde5-filesystem
Requires:   kf5-kinit
Requires:   kf5-kded
Requires:   kf5-kdoctools
Requires:   qt5-qtquickcontrols
Requires:   coreutils
Requires:   dbus-x11
Requires:   systemd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  zlib-devel
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  glib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  python-devel
BuildRequires:  boost-devel
BuildRequires:  libusb-devel
BuildRequires:  pam-devel
BuildRequires:  libSM-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  kf5-umbrella
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-kjsembed-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kde5-libksysguard-devel
BuildRequires:  libkscreen-devel
BuildRequires:  kde5-kwin-devel
BuildRequires:  desktop-file-utils

%description
KDE Frameworks 5 Tier 1 addon for advanced thread management.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
mkdir -p %{buildroot}%{_datadir}/xsessions
install -p %SOURCE1 %{buildroot}%{_datadir}/xsessions/plasma5-desktop.desktop
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_kde5_bindir}/*
%{_kde5_libdir}/*.so.*
%{_kde5_libdir}/libkdeinit5_*.so
%{_kde5_plugindir}/*
%{_kde5_libdir}/qml/org/kde/*
%{_kde5_libexecdir}/*
%{_kde5_datadir}/ksmserver
%{_kde5_datadir}/ksplash
%{_kde5_datadir}/plasma/plasmoids
%{_kde5_datadir}/plasma/services
%{_kde5_datadir}/plasma/shareprovider
%{_kde5_datadir}/plasma/wallpapers
%{_kde5_datadir}/plasma/look-and-feel
%{_kde5_datadir}/solid
%{_kde5_datadir}/kstyle
%{_kde5_datadir}/drkonqi/debuggers/external/*
%{_kde5_datadir}/drkonqi/debuggers/internal/*
%{_kde5_datadir}/drkonqi/mappings
%{_kde5_datadir}/drkonqi/pics/*.png
%{_kde5_sysconfdir}/xdg/*.knsrc
%{_kde5_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/applications/*.desktop
%{_datadir}/xsessions/plasma5-desktop.desktop
%{_datadir}/config.kcfg
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kde5_libdir}/libweather_ion.so
%{_kde5_libdir}/libtaskmanager.so
%{_kde5_libdir}/libkworkspace.so
%{_kde5_libdir}/libplasma-geolocation-interface.so
%{_kde5_includedir}/*
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/ScreenSaverDBusInterface
%{_datadir}/dbus-1/interfaces/*.xml
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/HTML/en/*
# >> files doc
# << files doc
