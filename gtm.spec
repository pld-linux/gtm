Summary:	GNOME Transfer Manager
Summary(es):	Gestor de Transferencias Gnome
Summary(it):	Gestore di traferimenti del Gnome
Summary(pl):	Zarz�dca Transferu GNOME
Summary(pt):	Gestor de Transfer�ncias Gnome
Name:		gtm
Version:	0.4.9
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://prdownloads.sourceforge.net/gtm/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gtm.sourceforge.net/
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
GTM allows the user to retrieve multiple files from the web. These
files can be retrieved in multiple parts and each part retrieved on a
separate session that the user is connected to the Internet. This is
most useful to users with dialup connections. The program performs
these tasks using wget as its back-end.

%description -l es
GTransferManager permite al usuario descargar m�ltiples ficheros de la
web. Estos ficheros pueden ser descargados en varias partes y cada
parte puede ser descargada en una sesi�n diferente en la que el
usuario est� conectado a Internet. Esto es especialmente util a los
usuarions con conexiones tipo dialup (modems). El programa realiza
estas tareas utilizando el wget como herramienta de descarga.

%description -l it
GTransferManager permette all'utente di scaricare piu' file dal
web.Questi file possono essere scaricati in piu' parti e ogni parte
scaricatain una differente sessione in cui l'utente e' collegato ad
Internet.Questo puo' essere utile agli utenti che hanno una
connessione dial-up con Internet. Il programma esegue i suoi compiti
usando wget come back-end.

%description -l pl
GTM pozwala u�ytkownikowi na przesy�anie wielu plik�w ze stron www.
Pliki mog� by� przesy�ane w wielu cz�ciach przy czym ka�da cze��
przesy�ana np. przy kolejnej sesji modemowej. GTM u�ywa wget'a do
wykonywania tych zada�.

%description -l pt
GTransferManager permite ao utilizador obter m�ltiplos ficheiros da
web. Eles podem ser obtidos em m�ltiplas partes e cada parte obtida
numa diferente sess�o em que o utilizador esta ligado � Internet. Isto
� muito �til para utilizadores com liga��es dialup. O programa executa
estas tarefas usando o wget.

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
	Networkdir=%{_applnkdir}/Network/Misc

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
%{_datadir}/applets/Network/Misc/*
%{_pixmapsdir}/*
%{_datadir}/sounds/gtm
