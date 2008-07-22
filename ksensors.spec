Summary:	KSensors - lmsensors frontend
Summary(pl.UTF-8):	KSensors - frontend dla lmsensors
Name:		ksensors
Version:	0.7.3
Release:	2
License:	GPL
Group:		X11/Applications
# Upstream is dead
#Source0:	http://dl.sourceforge.net/ksensors/%{name}-%{version}.tar.gz
Source0:	http://people.atrpms.net/~hdegoede/%{name}-%{version}-fedora-14.tar.gz
# Source0-md5:	7c64a2ef836c13d72b5711791819072e
URL:		http://ksensors.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	qt-devel >= 6:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSensors is a nice frontend for lm-sensors, a set of tools for
monitoring the hardware health of Linux systems equipped with certain
hardware health monitoring hardware such as the LM78 or LM75, and
HDDtemp, a tool for monitoring hard drive temperatures.

%description -l pl.UTF-8
KSensors jest przyjemnym interfejsem graficznym dla pakietu lm-sensors
(czyli zestawu narzędzi do monitorowania sprzętu współpracującego ze
sprzętem takim jak LM78 czy LM75) oraz HDDtemp (narzędziem do
monitorowania temperatury dysku twardego).

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

# Theme name has changed from locolor to Locolor
mv -f $RPM_BUILD_ROOT%{_iconsdir}/locolor $RPM_BUILD_ROOT%{_iconsdir}/Locolor

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
%{_datadir}/apps/ksensors/pics/*.png
%{_datadir}/sounds/ksensors_alert.wav
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*
