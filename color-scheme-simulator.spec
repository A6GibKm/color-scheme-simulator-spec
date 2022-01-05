%define commit     3ceb7225466c23f0a737a7aa17d5337b8e24991e

Name:       color-scheme-simulator
Version:    1.0.0
Release:    2%{?dist}
Summary:    Building blocks for modern GNOME applications
License:        GPLv3+
URL:            https://gitlab.gnome.org/exalm/color-scheme-simulator
Requires:       glibc
BuildRequires:  meson
BuildRequires:  ninja-build
Buildrequires:  gtk4-devel
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
Buildrequires:  vala
Buildrequires:  systemd-devel

Source0:        https://gitlab.gnome.org/exalm/color-scheme-simulator/-/archive/%{commit}/color-scheme-simulator-%{commit}.tar.gz

%description
Provides color schemes on systems with GNOME 40 or 41. It can be useful for testing apps when working on the dark style preference initiative.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%meson -Dgui=false
%meson_build

%install
%meson_install

%files
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.Impatience.service
%{_datadir}/glib-2.0/schemas/org.gnome.gitlab.exalm.Impatience.gschema.xml
%{_datadir}/xdg-desktop-portal/portals/0001-impatience.portal
%{_userunitdir}/xdg-desktop-portal-impatience.service
%{_libexecdir}/xdg-desktop-portal-impatience

%changelog
