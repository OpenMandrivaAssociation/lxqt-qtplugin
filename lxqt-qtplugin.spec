%define git 0
Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	0.9.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	2
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Patch0:		lxqt-qtplugin-0.9.0-fix-cmake.patch
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
BuildRequires:	cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:	qt5-devel
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(lxqt) >= %{version}

Requires:	%{_lib}Qt5Gui5

%description
LXQt system integration plugin for Qt. With this plugin, all Qt-based programs
can adopt settings of LXQt, such as the icon theme.

%files
%{_libdir}/qt5/plugins/platformthemes

#----------------------------------------------------------------------------

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

