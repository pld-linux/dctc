Summary:	Direct Connect Text Client
Summary(pl):	Tekstowy klient Direct Connect
Name:		dctc
Version:	0.69.0
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a Windows client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%description -l pl
DCTC jest klonem Direct Connect, windowsowego klienta pozwalaj±cego
u¿ytkonikom dzieliæ pliki i rozmawiaæ (podobnie do IRC-a, ale w sposób
bardziej zorientowany na dzielenie oprogramowania) u¿ywaj±c w³asnego
protoko³u.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog Documentation/* Documentation/*/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Documentation/*.gz Documentation/*/*.gz
%attr(755,root,root) %{_bindir}/*
