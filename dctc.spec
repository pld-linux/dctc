Summary:	Direct Connect Text Client
Summary(pl.UTF-8):	Tekstowy klient Direct Connect
Name:		dctc
Version:	0.85.9
Release:	2
License:	GPL
Group:		Applications/Communications
#Source0:	http://ac2i.linuxhome.com/dctc/%{name}-%{version}.tar.gz
Source0:	http://brainz.servebeer.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	3e2772cbbc36fac47fd31d01a7520a2e
Patch0:		%{name}-home_etc.patch
URL:		http://ac2i.homelinux.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 3.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a Windows client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%description -l pl.UTF-8
DCTC jest klonem Direct Connect, windowsowego klienta pozwalającego
użytkownikom współdzielić pliki i rozmawiać (podobnie do IRC-a, ale w
sposób bardziej zorientowany na dzielenie oprogramowania) używając
własnego protokołu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KNOWN_BUGS TODO README ChangeLog Documentation/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
