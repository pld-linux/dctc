Summary:	Direct Connect Text Client
Summary(pl):	Tekstowy klient Direct Connect
Name:		dctc
Version:	0.83.9
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-gcc2.patch
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a Windows client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%description -l pl
DCTC jest klonem Direct Connect, windowsowego klienta pozwalaj±cego
u¿ytkownikom wspó³dzieliæ pliki i rozmawiaæ (podobnie do IRC-a, ale w
sposób bardziej zorientowany na dzielenie oprogramowania) u¿ywaj±c
w³asnego protoko³u.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

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
