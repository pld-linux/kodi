# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - add and/or fix users/groups permissions
#  - split to subpackages?
# - bundled ffmpeg build (tools/depends/target/ffmpeg/autobuild.sh) enables nonfree & gpl!
#
# Conditional build:
# Features:
%bcond_with	airtunes	# AirTunes support
%bcond_without	dvdcss		# DVDCSS support
%bcond_without	gbm		# GBM platform
%bcond_without	optical_drive	# optical drive
%bcond_without	upnp		# UPnP support
%bcond_without	x11		# X11 platform
%ifarch %{arm} aarch64
%bcond_without	gles		# OpenGL rendering
%else
%bcond_with	gles		# OpenGLES rendering
%endif
%bcond_with	gold		# Use gold linker
%bcond_without	wayland		# Wayland platform
# System libs:
%bcond_without	system_ffmpeg	# system ffmpeg
# CPU instructions
%bcond_with	avx		# AVX instructions
%bcond_with	avx2		# AVX2 instructions
%bcond_with	neon		# NEON instructions
%bcond_with	sse		# SSE instructions
%bcond_with	sse2		# SSE2 instructions
%bcond_with	sse3		# SSE3 instructions
%bcond_with	ssse3		# SSSE3 instructions
%bcond_with	sse41		# SSE4.1 instructions
%bcond_with	sse42		# SSE4.2 instructions

%ifarch %{arm_with_neon}
%define		with_neon	1
%endif
%ifarch %{x86_with_sse}
%define		with_sse	1
%endif
%ifarch %{x86_with_sse2}
%define		with_sse2	1
%endif
%ifarch %{x8664} x32
%define		kodi_arch	x86_64-linux
%endif
%ifarch %{x86}
%define		kodi_arch	i486-linux
%endif
%ifnarch %{x8664} %{x86} x32
%define		kodi_arch	%{_target_base_arch}
%endif

%define		dvdread_ver		7.0.1
%define		dvdcss_ver		1.5.0
%define		dvdnav_ver		7.0.0

%{?use_default_jdk}

%define		_rc	rc1

%define		codename	Piers
Summary:	Kodi - a free and open source media-player and entertainment hub
Summary(pl.UTF-8):	Kodi - wolnodostępny, mający otwarte źródła odtwarzacz multimediów i hub rozrywkowy
Name:		kodi
Version:	22.0
Release:	0.%{_rc}.1
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
#Source0Download: https://github.com/xbmc/xbmc/releases
Source0:	https://github.com/xbmc/xbmc/archive/%{version}%{_rc}-%{codename}/%{version}%{_rc}-%{codename}.tar.gz
# Source0-md5:	bf004b52aca3ad160249e02717977c40
Source1:	https://mirrors.kodi.tv/build-deps/sources/libdvdread-%{dvdread_ver}.tar.bz2
# Source1-md5:	120e9ead9f59e2031d05e6a61ffea8ec
Source2:	https://mirrors.kodi.tv/build-deps/sources/libdvdcss-%{dvdcss_ver}.tar.bz2
# Source2-md5:	5ff8b0240506b96d04f1a0cf04ab77d1
Source3:	https://mirrors.kodi.tv/build-deps/sources/libdvdnav-%{dvdnav_ver}.tar.bz2
# Source3-md5:	a0f4805cd9bb44fd635378b5c0447623
Patch0:		ffmpeg7.patch
URL:		https://kodi.tv/
BuildRequires:	EGL-devel
%{?with_gbm:BuildRequires:	Mesa-libgbm-devel}
# for eglextchromium.h
%{?with_x11:BuildRequires:	Mesa-libEGL-devel}
%if %{without gles}
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%if %{with x11}
BuildRequires:	OpenGL-GLX-devel
%endif
%endif
%{?with_gles:BuildRequires:	OpenGLES-devel}
BuildRequires:	alsa-lib-devel >= 1.0.27
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	cmake >= 3.20
BuildRequires:	crossguid-devel >= 0.2.3
BuildRequires:	curl-devel
%{!?with_system_ffmpeg:BuildRequires:	dav1d-devel}
BuildRequires:	dbus-devel
BuildRequires:	exiv2-devel
# libavcodec >= 61.3.100 libavfilter >= 10.1.100 libavformat >= 61.1.100 libavutil >= 59.8.100 libpostproc >= 58.1.100 libswscale >= 8.1.100 libswresample >= 5.1.100
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 7.0.0}
BuildRequires:	flatbuffers-devel >= 1.9.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	fstrcmp-devel >= 0.7
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel >= 5
BuildRequires:	harfbuzz-devel
%buildrequires_jdk
BuildRequires:	lcms2-devel >= 2.10
BuildRequires:	libass-devel >= 0.15.0
BuildRequires:	libatomic-devel
BuildRequires:	libbluray-devel >= 0.9.3
BuildRequires:	libcap-devel
BuildRequires:	libcdio-c++-devel >= 2.1.0
BuildRequires:	libcdio-devel >= 2.1.0
BuildRequires:	libcec-devel >= 7.0.0
BuildRequires:	libdisplay-info-devel
BuildRequires:	libdrm-devel >= 2.4.95
BuildRequires:	libfmt-devel >= 6.1.2
%{?with_gbm:BuildRequires:	libinput-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libmicrohttpd-devel >= 0.9.40
BuildRequires:	libnfs-devel >= 3.0.0
BuildRequires:	libplist-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libtool
BuildRequires:	libudfread-devel >= 1.0.0
BuildRequires:	libuuid-devel
BuildRequires:	libva-devel
BuildRequires:	libva-drm-devel
%{?with_wayland:BuildRequires:	libva-wayland-devel}
%{?with_x11:BuildRequires:	libva-x11-devel}
%if %{with x11} && %{without gles}
BuildRequires:	libvdpau-devel
%endif
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	lirc-devel
BuildRequires:	lzo-devel >= 2
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	mysql-devel
BuildRequires:	nlohmann-json-devel >= 3.2.0
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pcre2-8-devel
BuildRequires:	pipewire-devel >= 0.3.50
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 11.0.0
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	sed >= 4.0
BuildRequires:	spdlog-devel >= 1.5.0
BuildRequires:	sqlite3-devel
BuildRequires:	swig >= 4.5.0
BuildRequires:	swig-python >= 4.5.0
BuildRequires:	taglib-devel >= 1.9.0
BuildRequires:	tinyxml-devel
BuildRequires:	tinyxml2-devel
BuildRequires:	udev-devel
%if %{with wayland}
BuildRequires:	wayland-protocols >= 1.7
BuildRequires:	waylandpp-devel >= 0.2.2
%endif
%if %{with x11}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
%endif
%if %{with gbm} || %{with wayland}
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.1
%endif
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	alsa-lib >= 1.0.27
Requires:	crossguid >= 0.2.3
Requires:	desktop-file-utils
Requires:	ffmpeg-libs >= 7.0.0
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.10
Requires:	libass >= 0.15.0
Requires:	libbluray >= 0.9.3
Requires:	libcdio >= 2.1.0
Requires:	libcdio-c++ >= 2.1.0
Requires:	libcec >= 7.0.0
Requires:	libdrm >= 2.4.95
Requires:	libfmt >= 6.1.2
Requires:	libmicrohttpd >= 0.9.40
Requires:	libnfs >= 3.0.0
Requires:	libplist >= 2.0
Requires:	libudfread >= 1.0.0
Requires:	lsb-release
Requires:	openssl >= 1.1.0
Requires:	pipewire-libs >= 0.3.50
Requires:	pulseaudio-libs >= 11.0.0
Requires:	spdlog >= 1.5.0
Requires:	taglib >= 1.9.0
Requires:	tinyxml >= 2.6.2
%{?with_wayland:Requires:	waylandpp >= 0.2.2}
%if %{with gbm} || %{with wayland}
Requires:	xorg-lib-libxkbcommon >= 0.4.1
%endif
Obsoletes:	xbmc < 14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debug enabled causes oom on i686/x32
%define		_enable_debug_packages	0

%description
Kodi Entertainment Center (formerly XBMC) is a free and open-source
media player software developed by the XBMC Foundation, a non-profit
technology consortium. Kodi is available for multiple operating
systems and hardware platforms, with a software 10-foot user interface
for use with televisions and remote controls. It allows users to play
and view most videos, music, such as podcasts from the internet, and
all common digital media files from local and network storage media.

%description -l pl.UTF-8
Kodi Entertainment Center (Centrum Rozrywkowe Kodi, dawniej XBMC) to
wolnodostępny programowy odtwarzacz multimedialny, rozwijany przez
XBMC Foundation - niedochodowe konsorcjum technologiczne. Kodi jest
dostępne na wiele systemów operacyjnych i platform sprzętowych, z
programowanym interfejsem użytkownika nadającym się do wykorzystania w
telewizorach i pilotach. Pozwala użytkownikom odtwarzać i oglądać
większość filmów, muzyki, podkastów z Internetu oraz wszystkich
popularnych nośników cyfrowych.

%package common
Summary:	Common files for Kodi
Summary(pl.UTF-8):	Wspólne pliki Kodi
Group:		Applications/Multimedia

%description common
Common files for Kodi.

%description common -l pl.UTF-8
Wspólne pliki Kodi.

%package devel
Summary:	Header files for Kodi
Summary(pl.UTF-8):	Pliki nagłówkowe Kodi
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description devel
Header files for Kodi.

%description devel -l pl.UTF-8
Pliki nagłówkowe Kodi.

%prep
%setup -q -n xbmc-%{version}%{_rc}-%{codename}
%patch -P0 -p1

%if %{without system_ffmpeg}
#ln -s %{SOURCE1} tools/depends/target/ffmpeg/ffmpeg-2.4.4-%{codename}.tar.gz
%endif

grep -q '^VERSION=%{dvdread_ver}$' tools/depends/target/libdvdread/LIBDVDREAD-VERSION
grep -q '^VERSION=%{dvdcss_ver}$' tools/depends/target/libdvdcss/LIBDVDCSS-VERSION
grep -q '^VERSION=%{dvdnav_ver}$' tools/depends/target/libdvdnav/LIBDVDNAV-VERSION
install -d build/build/download
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} build/build/download

%build
%cmake -B build \
	-DHOST_CAN_EXECUTE_TARGET:BOOL=TRUE \
	-DAPP_RENDER_SYSTEM=%{!?with_gles:gl}%{?with_gles:gles} \
	-DCORE_PLATFORM_NAME="%{?with_gbm:GBM;}%{?with_x11:X11;}%{?with_wayland:WAYLAND;}" \
	%{cmake_on_off airtunes ENABLE_AIRTUNES} \
	%{cmake_on_off dvdcss ENABLE_DVDCSS} \
	-DENABLE_INTERNAL_ASS:BOOL=OFF \
	-DENABLE_INTERNAL_BLURAY:BOOL=OFF \
	-DENABLE_INTERNAL_CEC:BOOL=OFF \
	-DENABLE_INTERNAL_CROSSGUID:BOOL=OFF \
	-DENABLE_INTERNAL_CURL:BOOL=OFF \
	-DENABLE_INTERNAL_DAV1D:BOOL=OFF \
	-DENABLE_INTERNAL_EXIV2:BOOL=OFF \
	-DENABLE_INTERNAL_FFMPEG:BOOL=%{?with_system_ffmpeg:OFF}%{!?with_system_ffmpeg:ON} \
	-DENABLE_INTERNAL_FLATBUFFERS:BOOL=OFF \
	-DENABLE_INTERNAL_FMT:BOOL=OFF \
	-DENABLE_INTERNAL_FSTRCMP:BOOL=OFF \
	-DENABLE_INTERNAL_LCMS2:BOOL=OFF \
	-DENABLE_INTERNAL_LIBMICROHTTPD:BOOL=OFF \
	-DENABLE_INTERNAL_MARIADBCLIENT:BOOL=OFF \
	-DENABLE_INTERNAL_NFS:BOOL=OFF \
	-DENABLE_INTERNAL_NLOHMANNJSON:BOOL=OFF \
	-DENABLE_INTERNAL_PCRE2:BOOL=OFF \
	-DENABLE_INTERNAL_SPDLOG:BOOL=OFF \
	-DENABLE_INTERNAL_SWIG:BOOL=OFF \
	-DENABLE_INTERNAL_TAGLIB:BOOL=OFF \
	-DENABLE_INTERNAL_UDFREAD:BOOL=OFF \
	-DENABLE_INTERNAL_XSLT:BOOL=OFF \
	%{cmake_on_off gold ENABLE_GOLD} \
	-DENABLE_TESTING:BOOL=OFF \
	%{cmake_on_off optical_drive ENABLE_OPTICAL} \
	%{cmake_on_off upnp ENABLE_UPNP} \
	%{cmake_on_off avx ENABLE_AVX} \
	%{cmake_on_off avx2 ENABLE_AVX2} \
	%{cmake_on_off neon ENABLE_NEON} \
	%{cmake_on_off sse ENABLE_SSE} \
	%{cmake_on_off sse2 ENABLE_SSE2} \
	%{cmake_on_off sse3 ENABLE_SSE3} \
	%{cmake_on_off ssse3 ENABLE_SSSE3} \
	%{cmake_on_off sse41 ENABLE_SSE4_1} \
	%{cmake_on_off sse42 ENABLE_SSE4_2} \
	-DWITH_ARCH=%{kodi_arch} \
	-DWITH_CPU=%{_target_cpu}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/addons

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_docdir}/{version.txt,README.Linux.md,LICENSE.md}

# not packaged
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/firewalld/services/kodi-*.xml

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc README.md docs/README.Linux.md
%attr(755,root,root) %{_bindir}/kodi
%attr(755,root,root) %{_bindir}/kodi-TexturePacker
%attr(755,root,root) %{_bindir}/kodi-standalone
%{_datadir}/%{name}/addons
%{_datadir}/%{name}/media
%{_datadir}/%{name}/privacy-policy.txt
%{_datadir}/%{name}/python-stubs
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%attr(755,root,root) %{_libdir}/%{name}/%{name}.bin
%{?with_x11:%attr(755,root,root) %{_libdir}/%{name}/%{name}-xrandr}
%dir %{_libdir}/%{name}/addons
%dir %{_libdir}/%{name}/system
%dir %{_libdir}/%{name}/system/players
%dir %{_libdir}/%{name}/system/players/VideoPlayer
%attr(755,root,root) %{_libdir}/%{name}/system/players/VideoPlayer/libdvdnav-%{kodi_arch}.so
%{_desktopdir}/kodi.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/kodi.svg
%{_datadir}/metainfo/org.xbmc.kodi.metainfo.xml
%{_datadir}/xsessions/kodi.desktop
%{_datadir}/wayland-sessions/kodi-gbm.desktop

%files common
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/kodi
%{_libdir}/%{name}/cmake
%{_datadir}/%{name}/cmake
