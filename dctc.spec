Summary:	Direct Connect Text Client
Summary(pl):	Tekstowy klient Direct Connect
Name:		dctc
Version:	0.60
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ac2i.tzo.com/dctc/%{name}_v%{version}.tar.gz
Patch0:		%{name}-CFLAGS.patch
URL:		http://ac2i.tzo.com/dctc/
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
%setup -q -c
%patch0 -p0

%build
pldcflags="%{rpmcflags}" ; export pldcflags
gcc=%{__cc} ; export gcc
%{__make} nomakedepend

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install src/hublist src/dctc $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README COPYING ChangeLog INSTALL Documentation/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Documentation
%attr(755,root,root) %{_bindir}/hublist
%attr(755,root,root) %{_bindir}/dctc
