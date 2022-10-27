Summary:	Command-line copy/paste utilities for Wayland
Name:		wl-clipboard
Version:	2.1.0
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/bugaevc/wl-clipboard/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e39e266bca009d00a9ab99c29eb41ebc
URL:		https://github.com/bugaevc/wl-clipboard
BuildRequires:	meson >= 0.44.0
BuildRequires:	ninja
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project implements two command-line Wayland clipboard utilities,
wl-copy and wl-paste, that let you easily copy data between the
clipboard and Unix pipes, sockets, files and so on.

%package -n bash-completion-wl-clipboard
Summary:	Bash completion for wl-clipboard
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-wl-clipboard
Bash completion for wl-clipboard.

%package -n fish-completion-wl-clipboard
Summary:	fish-completion for wl-clipboard
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-wl-clipboard
fish-completion for wl-clipboard.

%package -n zsh-completion-wl-clipboard
Summary:	ZSH completion for wl-clipboard
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-wl-clipboard
ZSH completion for wl-clipboard.

%prep
%setup -q

%build
%meson build \
	-Dzshcompletiondir=%{zsh_compdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/wl-copy
%attr(755,root,root) %{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1*
%{_mandir}/man1/wl-copy.1*
%{_mandir}/man1/wl-paste.1*

%files -n bash-completion-wl-clipboard
%defattr(644,root,root,755)
%{bash_compdir}/wl-copy
%{bash_compdir}/wl-paste

%files -n fish-completion-wl-clipboard
%defattr(644,root,root,755)
%{fish_compdir}/wl-copy.fish
%{fish_compdir}/wl-paste.fish

%files -n zsh-completion-wl-clipboard
%defattr(644,root,root,755)
%{zsh_compdir}/_wl-copy
%{zsh_compdir}/_wl-paste
