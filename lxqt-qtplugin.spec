%define git 0
Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	0.14.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	2
Source0:	https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(qt5xdgiconloader)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(dbusmenu-qt5)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake(fm-qt)
BuildRequires:	pkgconfig(libfm-extra)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	git-core
Requires:	%{_lib}qt5gui5
Requires:	%{_lib}qt5gui5-x11

%description
LXQt system integration plugin for Qt. With this plugin, all Qt-based programs
can adopt settings of LXQt, such as the icon theme.

%files
%dir %{_libdir}/qt5/plugins/platformthemes
%{_libdir}/qt5/plugins/platformthemes/libqtlxqt.so

#----------------------------------------------------------------------------

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%autopatch -p1

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
