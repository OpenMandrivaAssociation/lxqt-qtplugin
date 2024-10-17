%define git 0
Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	2.0.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	2
Source0:	https://github.com/lxqt/lxqt-qtplugin/releases/download/%{version}/lxqt-qtplugin-%{version}.tar.xz
%endif
Patch:		lxqt-qtplugin-config.patch
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
BuildRequires:	cmake
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(qt6xdgiconloader)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(dbusmenu-lxqt)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(fm-qt6)
BuildRequires:	pkgconfig(libfm-extra)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	git-core

%description
LXQt system integration plugin for Qt. With this plugin, all Qt-based programs
can adopt settings of LXQt, such as the icon theme.

%files
%dir %{_libdir}/qt6/plugins/platformthemes
%{_libdir}/qt6/plugins/platformthemes/libqtlxqt.so

#----------------------------------------------------------------------------

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%autopatch -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
