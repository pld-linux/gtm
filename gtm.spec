Summary:	GNOME Transfer Manager
Summary(es):	Gestor de Transferencias Gnome
Summary(it):	Gestore di traferimenti del Gnome
Summary(pl):	Zarz±dca Transferu GNOME
Summary(pt):	Gestor de Transferências Gnome
Name:		gtm
Version:	0.4.11
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/gtm/%{name}-%{version}.tar.gz
# Source0-md5:	30507d4c767c6a88534e3a57bbe7fef0
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_ac.patch
Patch2:		%{name}-wget.patch
URL:		http://gtm.sourceforge.net/
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	wget >= 1.6
Requires:	wget >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
GTM allows the user to retrieve multiple files from the web. These
files can be retrieved in multiple parts and each part retrieved on a
separate session that the user is connected to the Internet. This is
most useful to users with dialup connections. The program performs
these tasks using wget as its back-end.

%description -l es
GTransferManager permite al usuario descargar múltiples ficheros de la
web. Estos ficheros pueden ser descargados en varias partes y cada
parte puede ser descargada en una sesión diferente en la que el
usuario esté conectado a Internet. Esto es especialmente util a los
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
GTM pozwala u¿ytkownikowi na przesy³anie wielu plików ze stron www.
Pliki mog± byæ przesy³ane w wielu czê¶ciach przy czym ka¿da cze¶æ
przesy³ana np. przy kolejnej sesji modemowej. GTM u¿ywa wget'a do
wykonywania tych zadañ.

%description -l pt
GTransferManager permite ao utilizador obter múltiplos ficheiros da
web. Eles podem ser obtidos em múltiplas partes e cada parte obtida
numa diferente sessão em que o utilizador esta ligado à Internet. Isto
é muito útil para utilizadores com ligações dialup. O programa executa
estas tarefas usando o wget.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-applet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	  Networkdir=%{_applnkdir}/Network/Misc install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*/*/*
%{_applnkdir}/Network/Misc/*.desktop
%{_datadir}/applets/Network/*
%{_pixmapsdir}/*
%{_datadir}/sounds/gtm
%{_datadir}/idl/*
%{_datadir}/oaf/*
