#define git 0
Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	2.5.0
%if 0%{?git:1}
Release:	1.%git.3
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	https://github.com/lxqt/lxqt-qtplugin/releases/download/%{version}/lxqt-qtplugin-%{version}.tar.xz
%endif
Patch:		lxqt-qtplugin-config.patch
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
BuildSystem:	cmake
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiPrivate)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(qt6xdgiconloader) >= 4.5.0
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(dbusmenu-lxqt) >= 0.5.0
BuildRequires:	cmake(lxqt2-build-tools) >= 2.5.0
BuildRequires:	cmake(fm-qt6) >= 2.5.0
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	git-core

%description
LXQt system integration plugin for Qt. With this plugin, all Qt-based programs
can adopt settings of LXQt, such as the icon theme.

%files
%dir %{_libdir}/qt6/plugins/platformthemes
%{_libdir}/qt6/plugins/platformthemes/libqtlxqt.so
