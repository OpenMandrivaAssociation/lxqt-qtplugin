%define git 20140803
Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	0.8.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(lxqt-qt5)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)

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
%setup -q -c %{name}-%{version}
%endif

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

