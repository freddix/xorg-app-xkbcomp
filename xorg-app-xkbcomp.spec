Summary:	xkbcomp application
Name:		xorg-app-xkbcomp
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbcomp-%{version}.tar.bz2
# Source0-md5:	0012a8e3092cddf7f87b250f96bb38c5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libxkbfile-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbcomp application.

%prep
%setup -qn xkbcomp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README*
%attr(755,root,root) %{_bindir}/xkbcomp
%{_pkgconfigdir}/xkbcomp.pc
%{_mandir}/man1/xkbcomp.1x*

