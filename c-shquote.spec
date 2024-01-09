Summary:	POSIX Shell Compatible Argument Parser
Name:		c-shquote
Version:	1.1.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-shquote/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a07c09079200c58f8402b43939463e79
URL:		https://c-util.github.io/c-shquote/
BuildRequires:	c-stdaux-devel >= 1.5.0
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-shquote project is a standalone implementation of POSIX Shell
compatible argument parsing written in Standard ISO-C11.

%package devel
Summary:	Header files for c-shquote library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for c-shquote library.

%package static
Summary:	Static c-shquote library
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static c-shquote library.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libcshquote-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcshquote-1.so
%{_includedir}/c-shquote.h
%{_pkgconfigdir}/libcshquote-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcshquote-1.a
