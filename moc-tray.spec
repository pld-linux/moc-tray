Summary:	Control your music on console player via tray icon
Name:		moc-tray
Version:	0.3
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://moc-tray.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	f668f12fabe5fca41130955590558001
URL:		http://code.google.com/p/moc-tray/
Requires:	moc
Requires:	perl-Encode
Requires:	perl-Gtk2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moc-Tray allows quick and easy access to mocp basic functions and
console interface via tray pop-up menu. Written in gtk2-perl.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog
%attr(755,root,root) %{_bindir}/moc-tray
%{_desktopdir}/moc-tray.desktop
%{_pixmapsdir}/moc-tray.png
