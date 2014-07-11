Summary:	Qt plugin for the LXQt desktop
Name:		lxqt-qtplugin
Version:	0.7.0
Release:	3
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(lxqt)

%description
LXQt system integration plugin for Qt. With this plugin, all Qt-based programs
can adopt settings of LXQt, such as the icon theme.

%files
%{_libdir}/qt4/plugins/gui_platform

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

