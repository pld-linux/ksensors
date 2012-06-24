Summary:	KSensors - lmsensors frontend
Summary(pl):	KSensors - frontend dla lmsensors
Name:		ksensors
Version:	0.7.3
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://dl.sourceforge.net/ksensors/%{name}-%{version}.tar.gz
# Source0-md5:	4f6c5d7dea5e637e772d17f1e547d6f1
URL:		http://ksensors.sourceforge.net/
BuildRequires:	automake
BuildRequires:	lm_sensors-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	qt-devel >= 3.0
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSensors is a nice frontend for lm-sensors, a set of tools for
monitoring the hardware health of Linux systems equipped with certain
hardware health monitoring hardware such as the LM78 or LM75, and
HDDtemp, a tool for monitoring hard drive temperatures.

%description -l pl
KSensors jest przyjemnym interfejsem graficznym dla pakietu
lm-sensors (czyli zestawu narz�dzi do monitorowania sprz�tu
wsp�pracuj�cego ze sprz�tem takim jak LM78 czy LM75) oraz HDDtemp
(narz�dziem do monitorowania temperatury dysku twardego).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/apps/ksensors
%{_datadir}/apps/ksensors/ksensorsui.rc
%dir %{_datadir}/apps/ksensors/pics
%{_datadir}/apps/ksensors/pics/*
%dir %{_datadir}/apps/sounds
%{_datadir}/apps/sounds/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*
