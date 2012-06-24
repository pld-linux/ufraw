
# todo:
# - manual page for ufraw-batch?

Summary:	RAW photo loader
Summary(pl):	Narz�dzie do wczytywania zdj�� RAW
Name:		ufraw
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	2074676b9437738630eee72b9fc6c50c
URL:		http://ufraw.sourceforge.net/
BuildRequires:	gimp-devel >= 2.0
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _plugindir      %(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles.

%description -l pl
UFRaw to narz�dzie do czytania i przetwarzania surowych obraz�w z
aparat�w cyfrowych. Mo�e by� u�ywane samodzielnie lub jako wtyczka
GIMP-a. Czyta surowe zdj�cia przy u�yciu narz�dzia do konwersji DCRaw
Dave'a Coffina. Obs�uguje podstawowe zarz�dzanie kolorami przy u�yciu
Little CMS, pozwalaj�c u�ytkownikowi zastosowa� profile kolor�w.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl):	Wtyczka GIMP-a do wczytywania zdj�� RAW
Group:		Applications

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl
Wtyczka GIMP-a do wczytywania zdj�� RAW.

%package batch
Summary:	RAW photo loader batch software
Summary(pl):	Program do wsadowego wczytywania zdj�� RAW
Group:		Applications

%description batch
RAW photo loader batch software.

%description batch -l pl
Program do wsadowego wczytywania zdj�� RAW.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/ufraw*

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/ufraw-gimp

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch
