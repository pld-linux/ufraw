# TODO:
# - cinepaint plugin
#
# Conditional build:
%bcond_without	gomp	# without OpenMP support
#
Summary:	RAW photo loader
Summary(pl.UTF-8):	Narzędzie do wczytywania zdjęć w formacie RAW
Name:		ufraw
Version:	0.19.1
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	fc9e015013e30a198b652d80d156ed49
URL:		http://ufraw.sourceforge.net/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cfitsio-devel
#BuildRequires:	cinepaint-devel >= 0.22 (cinepaint-gtk?)
BuildRequires:	exiv2-devel >= 0.20
%{?with_gomp:BuildRequires:	gcc-c++ >= 6:4.2}
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 2.6.0
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	gtkimageview-devel >= 1.6
BuildRequires:	jasper-devel
BuildRequires:	lcms-devel >= 1.14
BuildRequires:	lensfun-devel >= 0.2.5
%{?with_gomp:BuildRequires:	libgomp-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info >= 0.21
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	exiv2 >= 0.20
Requires:	glib2 >= 1:2.12
Requires:	gtk+2 >= 1:2.12
Requires:	gtkimageview >= 1.6
Requires:	lcms >= 1.14
Requires:	lensfun >= 0.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles.

%description -l pl.UTF-8
UFRaw to narzędzie do czytania i przetwarzania zdjęć w formacie RAW
różnych aparatów cyfrowych. Może być używane samodzielnie lub jako
wtyczka programu GIMP. Zdjęcia w formacie RAW są wczytywane za pomocą
programu DCRaw Dave'a Coffina. Użytkownik ma możliwość stosowania
profili kolorów dzięki bibliotece Little CMS.

%package batch
Summary:	RAW photo loader batch software
Summary(pl.UTF-8):	Program do wsadowego przetwarzania zdjęć w formacie RAW
Group:		Applications/Graphics
Requires:	exiv2 >= 0.20
Requires:	glib2 >= 1:2.12
Requires:	lcms >= 1.14
Requires:	lensfun >= 0.2.5

%description batch
RAW photo loader batch software.

%description batch -l pl.UTF-8
Program do wsadowego przetwarzania zdjęć w formacie RAW.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl.UTF-8):	Wtyczka GIMP-a do wczytywania zdjęć w formacie RAW
Group:		Applications/Graphics
Requires:	exiv2 >= 0.20
Requires:	gimp >= 2.6.0
Requires:	glib2 >= 1:2.12
Requires:	gtk+2 >= 1:2.12
Requires:	gtkimageview >= 1.6
Requires:	lcms >= 1.14
Requires:	lensfun >= 0.2.5

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl.UTF-8
Wtyczka GIMP-a do wczytywania zdjęć w formacie RAW.

%prep
%setup -q

%build
cp -f /usr/share/automake/mkinstalldirs .
%configure \
	--disable-silent-rules \
	%{!?with_gomp:--disable-openmp} \
	--enable-contrast \
	--enable-dst-correction \
	--enable-extras \
	--enable-mime \
	--with-gtk \
	--with-gimp 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	schemasdir=%{_sysconfdir}/gconf/schemas

install ufraw.desktop $RPM_BUILD_ROOT%{_desktopdir}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/dcraw

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ufraw.schemas
%update_desktop_database_post

%preun
%gconf_schema_uninstall ufraw.schemas

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/nikon-curve
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/ufraw.desktop
%{_pixmapsdir}/ufraw.png
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_mandir}/man1/ufraw.1*

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/ufraw-gimp
