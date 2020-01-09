Name:            emacs-php-mode
Version:         1.18.2
Release:         1%{?dist}
Summary:         Major GNU Emacs mode for editing PHP code
Group:           Applications/Editors
License:         GPLv3+
URL:             http://github.com/ejmr/php-mode
Source0:         https://github.com/ejmr/php-mode/archive/v%{version}.tar.gz#/php-mode-%{version}.tar.gz
Source1:         php-mode-init.el
BuildArch:       noarch
BuildRequires:   emacs emacs-el texinfo
Requires:        emacs(bin) >= %{_emacs_version}
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

%description
Major GNU Emacs mode for editing PHP code.

%prep
%setup -q -n php-mode-%{version}

%build
make %{?_smp_mflags} all
# Temporarily provide php-mode.elc into skeleton/ just so everything there compiles correctly.
ln -s ../php-mode.elc skeleton/php-mode.elc
%{_emacs_bytecompile} skeleton/*.el
rm -f skeleton/php-mode.elc

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/php-mode
install -p -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/php-mode/
install -p -m 644 skeleton/*.el{,c} %{buildroot}/%{_emacs_sitelispdir}/php-mode/

# Install php-mode-init.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%check
make test

%post
/sbin/install-info %{_infodir}/php-mode.info %{_infodir}/dir 2> /dev/null || :

%preun
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/php-mode.info %{_infodir}/dir 2> /dev/null || :
fi

%files
%doc Changelog.md
%license LICENSE
%{_emacs_sitestartdir}/php-mode-init.el
%dir %{_emacs_sitelispdir}/php-mode
%{_emacs_sitelispdir}/php-mode/*

%changelog
* Wed Sep 20 2017 Jan Synacek <jsynacek@redhat.com> - 1.18.2-1
- initial import
