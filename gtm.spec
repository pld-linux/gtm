Summary:	GNOME Transfer Manager
Summary(pl):	Zarz±dca Transferu GNOME
Name:		gtm
Version:	0.4.9
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp1.sourceforge.net/gtm/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gtm.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
Requires:	wget >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
GTM allows the user to retrieve multiple files from the web. 
These files can be retrieved in multiple parts and each part retrieved on a
separate session that the user is connected to the Internet. This is
most useful to users with dialup connections. The program performs
these tasks using wget as its back-end.

%description -l pl
GTM pozwala u¿ytkownikowi na przesy³anie wielu plików ze stron www.
Pliki mog± byæ przesy³ane w wielu czê¶ciach przy czym ka¿da cze¶æ przesy³ana
np. przy kolejnej sesji modemowej. GTM u¿ywa wget'a do wykonywania tych zadañ.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-applet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Networkdir=%{_applnkdir}/Network

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*/*/*
%{_applnkdir}/Network/*.desktop
%{_datadir}/idl/*.idl
%{_datadir}/applets/Network/*
%{_pixmapsdir}/*
%{_datadir}/sounds/gtm
