Summary:	Direct Connect Text Client
Summary(pl):	Tekstowy klient Direct Connect
Name:		dctc
Version:	0.85.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	99fdcb356a4a59fbd5bf892af2e79f78
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	db-devel
BuildRequires:	glib-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a Windows client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%description -l pl
DCTC jest klonem Direct Connect, windowsowego klienta pozwalaj�cego
u�ytkownikom wsp�dzieli� pliki i rozmawia� (podobnie do IRC-a, ale w
spos�b bardziej zorientowany na dzielenie oprogramowania) u�ywaj�c
w�asnego protoko�u.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
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
