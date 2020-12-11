#
# Conditional build:
%bcond_without	gimp		# GIMP plugin
%bcond_without	openmp		# OpenMP support
#
Summary:	RAW photo loader
Summary(pl.UTF-8):	Narzędzie do wczytywania zdjęć w formacie RAW
Name:		ufraw
Version:	0.22
Release:	12
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	c30767cae2c44310f2a3d67d7a76f2c3
Patch0:		05_fix_build_due_to_unsigned_char.patch
Patch1:		ufraw-find_green.patch
Patch2:		ufraw-lf-destroy.patch
Patch3:		ufraw-multipliers.patch
Patch4:		exiv2-0.27.patch
Patch5:		%{name}-include.patch
URL:		http://ufraw.sourceforge.net/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cfitsio-devel
BuildRequires:	exiv2-devel >= 0.20
%{?with_openmp:BuildRequires:	gcc-c++ >= 6:4.2}
BuildRequires:	gettext-tools
%{?with_gimp:BuildRequires:	gimp-devel >= 2.6.0}
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	gtkimageview-devel >= 1.6
BuildRequires:	jasper-devel
BuildRequires:	lcms2-devel >= 2
BuildRequires:	lensfun-devel >= 0.2.5
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info >= 0.21
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	exiv2-libs >= 0.20
Requires:	glib2 >= 1:2.12
Requires:	gtk+2 >= 1:2.12
Requires:	gtkimageview >= 1.6
Requires:	lcms2 >= 2
Requires:	lensfun >= 0.2.5
Obsoletes:	cinepaint-plugin-ufraw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimp_plugindir		%(gimptool --gimpplugindir)/plug-ins
%endif

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
Requires:	lcms2 >= 2
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
Requires:	lcms2 >= 2
Requires:	lensfun >= 0.2.5

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl.UTF-8
Wtyczka GIMP-a do wczytywania zdjęć w formacie RAW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cp -f /usr/share/automake/mkinstalldirs .
%configure \
	--disable-silent-rules \
	%{!?with_openmp:--disable-openmp} \
	--enable-contrast \
	--enable-dst-correction \
	--enable-extras \
	--enable-mime \
	--with-gimp%{!?with_gimp:=no} \
	--with-gtk

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
%{_datadir}/appdata/ufraw.appdata.xml
%{_mandir}/man1/ufraw.1*

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch

%if %{with gimp}
%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{gimp_plugindir}/ufraw-gimp
%endif
