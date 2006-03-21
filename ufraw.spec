
# todo:
# - manual page for ufraw-batch?

Summary:	RAW photo loader
Summary(pl):	Narz�dzie do wczytywania zdj�� w formacie RAW
Name:		ufraw
Version:	0.7
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	e8ea903f2679275f7a5d05d408af225d
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
UFRaw to narz�dzie do czytania i przetwarzania zdj�� w formacie RAW r�nych
aparat�w cyfrowych. Mo�e by� u�ywane samodzielnie lub jako wtyczka programu
GIMP. Zdj�cia w formacie RAW s� wczytywane za pomoc� programu DCRaw Dave'a
Coffina. U�ytkownik ma mo�liwo�� stosowania profili kolor�w dzi�ki
bibliotece Little CMS.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl):	Wtyczka GIMP-a do wczytywania zdj�� w formacie RAW
Group:		Applications

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl
Wtyczka GIMP-a do wczytywania zdj�� w formacie RAW.

%package batch
Summary:	RAW photo loader batch software
Summary(pl):	Program do wsadowego przetwarzania zdj�� w formacie RAW
Group:		Applications

%description batch
RAW photo loader batch software.

%description batch -l pl
Program do wsadowego przetwarzania zdj�� w formacie RAW.

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
