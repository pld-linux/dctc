Summary:	Direct Connect Text Client
Summary(pl):	tekstowy klient Direct Connect
Name:		dctc
Version:	0.59
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://ac2i.tzo.com/dctc/%{name}_v%{version}.tar.gz
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a windoz client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
cp src/hublist src/dctc $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README COPYING ChangeLog INSTALL Documentation/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Documentation
%attr(755,root,root) %{_bindir}/hublist
%attr(755,root,root) %{_bindir}/dctc
