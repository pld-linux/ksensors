Summary:	KSensors - lmsensors frontend
Summary(pl):	KSensors - frontend dla lmsensors
Name:		ksensors
Version:	0.7.3
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4f6c5d7dea5e637e772d17f1e547d6f1
URL:		http://ksensors.sourceforge.net/
BuildRequires:	lm_sensors-devel
BuildRequires:	qt-devel >= 3.0
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KSensors is a nice frontend for lm-sensors, a set of tools for
monitoring the hardware health of Linux systems equipped with certain
hardware health monitoring hardware such as the LM78 or LM75, and
HDDtemp, a tool for monitoring hard drive temperatures.

%description -l pl
KSensors jest przyjemnym interfejsem graficznym dla pakietu
lm-sensors (czyli zestawu narzêdzi do monitorowania sprzêtu
wspó³pracuj±cego ze sprzêtem takim jak LM78 czy LM75) oraz HDDtemp
(narzêdziem do monitorowania temperatury dysku twardego).

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        desktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*
%dir %{_datadir}/apps/ksensors
%dir %{_datadir}/apps/ksensors/pics
%dir %{_datadir}/apps/sounds
%{_datadir}/apps/ksensors/ksensorsui.rc
%{_datadir}/apps/ksensors/pics/*
%{_datadir}/apps/sounds/*

%{_pixmapsdir}/*/*/apps/*
