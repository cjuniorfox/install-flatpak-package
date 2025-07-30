Name:           install-flatpak-package
Version:        1.1
Release:        1%{?dist}
Summary:        Systemd service to install Flatpak packages after network becomes available

License:        GPL-3.0
URL:            https://github.com/cjuniorfox/install-flatpak-package

Source0: %{name}-%{version}.tar.gz

Requires:       flatpak
Requires(post): systemd
Requires(preun): systemd

BuildArch:      noarch

%description
This package provides a systemd template unit and script that automatically installs
specified Flatpak applications once network connectivity is available. Intended for use
in post-installation environments like preconfigured Fedora-based ISOs.

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 0755 install-flatpak-package.sh %{buildroot}%{_libexecdir}/%{name}

install -d %{buildroot}%{_unitdir}
install -m 0644 install-flatpak-package@.service %{buildroot}%{_unitdir}

install -d %{buildroot}%{_docdir}/%{name}
install -m 644 README.md %{buildroot}%{_docdir}/%{name}

install -d %{buildroot}%{_licensedir}/%{name}
install -m 644 LICENSE %{buildroot}%{_licensedir}/%{name}

%post

%preun

%files
%{_docdir}/%{name}/README.md
%{_licensedir}/%{name}/LICENSE
%{_libexecdir}/%{name}/install-flatpak-package.sh
%{_unitdir}/install-flatpak-package@.service

%changelog
* Wed Jul 30 2025 Junior <cjuniorfox@gmail.com> 1.1-1
- new package built with tito


* Wed Jul 30 2025 Carlos Junior <cjuniorfox@gmail.com> - 1.0-0
- Initial release

