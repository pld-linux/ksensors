Summary:	KSensors - lmsensors frontend
Summary(pl):	KSensors - frontend dla lmsensors
Name:		ksensors
Version:	0.7.2
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://ksensors.sourceforge.net/
BuildRequires:	lm_sensors-devel
BuildRequires:	qt >= 3.0
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSensors is a nice frontend for lm-sensors, a set of tools for
monitoring the hardware health of Linux systems equipped with certain
hardware health monitoring hardware such as the LM78 or LM75, and
HDDtemp, a tool for monitoring hard drive temperatures.

%description -l pl
KSensors jest przyjemnym interfejsem graficznym dla pakietu
lm-sensors, jest to zestaw narzedzi do monitorowania sprzetu
wspó³pracuj±cy ze sprzêtem takim jak LM78 czy LM75 i HDDtemp,
narzêdziem do monitorowania temperatury dysku twardego.

%prep
%setup -q
rm config.cache

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install-strip

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{hicolor,locolor}/{16x16,32x32}/apps \
	   $RPM_BUILD_ROOT%{_applnkdir}/Applications

mv -f $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_pixmapsdir}
install ksensors/ksensors.desktop $RPM_BUILD_ROOT%{_applnkdir}/Applications

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
%{_datadir}/apps/ksensors/pics/*
%{_pixmapsdir}/*/*
%{_datadir}/autostart/*
