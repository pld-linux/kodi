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
%bcond_without	system_ffmpeg	# build with system ffmpeg
# CPU instructions
%bcond_with	avx		# use AVX instructions
%bcond_with	avx2		# use AVX2 instructions
%bcond_with	neon		# use NEON instructions
%bcond_with	sse		# use SSE instructions
%bcond_with	sse2		# use SSE2 instructions
%bcond_with	sse3		# use SSE3 instructions
%bcond_with	ssse3		# use SSSE3 instructions
%bcond_with	sse41		# use SSE4.1 instructions
%bcond_with	sse42		# use SSE4.2 instructions

%ifarch %{arm_with_neon}
%define		with_neon	1
%endif
%ifarch %{x86_with_sse}
%define		with_sse	1
%endif
%ifarch %{x86_with_sse2}
%define		with_sse2	1
%endif

%define	codename Matrix
#define	subver	rc1
Summary:	Kodi is a free and open source media-player and entertainment hub
Name:		kodi
Version:	19.4
Release:	4
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
#Source0Download: https://github.com/xbmc/xbmc/releases
Source0:	https://github.com/xbmc/xbmc/archive/%{version}-%{codename}.tar.gz
# Source0-md5:	a668854505eff3ca5ed9f33e3ac91c80
Patch0:		disable-static.patch
Patch1:		libdvd.patch
Patch2:		libfmt9.patch
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
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	cmake >= 3.4
BuildRequires:	crossguid-devel
BuildRequires:	curl-devel
%{!?with_system_ffmpeg:BuildRequires:	dav1d-devel}
BuildRequires:	dbus-devel
# libavcodec >= 58.91.100 libavfilter >= 7.85.100 libavformat >= 58.45.100 libavutil >= 56.51.100 libpostproc >= 55.7.100 libswscale >= 5.7.100 libswresample >= 3.7.100
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 4.3}
BuildRequires:	flatbuffers-devel >= 1.9.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	fstrcmp-devel >= 0.7
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel >= 5
BuildRequires:	jre
BuildRequires:	lcms2-devel
BuildRequires:	libass-devel
BuildRequires:	libatomic-devel
BuildRequires:	libbluray-devel >= 0.9.3
BuildRequires:	libcap-devel
BuildRequires:	libcdio-c++-devel >= 2.1.0
BuildRequires:	libcdio-devel >= 2.1.0
BuildRequires:	libcec-devel >= 3.0.0
BuildRequires:	libdrm-devel >= 2.4.95
%{?with_dvdcss:BuildRequires:	libdvdcss-devel >= 1.4.1}
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libfmt-devel >= 6.1.2
%{?with_gbm:BuildRequires:	libinput-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libmicrohttpd-devel >= 0.9.40
BuildRequires:	libnfs-devel
BuildRequires:	libplist-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel >= 6:5
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
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel >= 1.0.2
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 11.0.0
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	rapidjson-devel >= 1.1.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRequires:	sed >= 4.0
BuildRequires:	spdlog-devel >= 1.5.0
BuildRequires:	sqlite3-devel
BuildRequires:	swig
BuildRequires:	taglib-devel >= 1.9.0
BuildRequires:	tinyxml-devel >= 2.6.2
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
Requires:	desktop-file-utils
Requires:	ffmpeg-libs >= 4.3
Requires:	hicolor-icon-theme
Requires:	libbluray >= 0.9.3
Requires:	libcdio >= 2.1.0
Requires:	libcdio-c++ >= 2.1.0
Requires:	libcec >= 3.0.0
Requires:	libdrm >= 2.4.95
%{?with_dvdcss:Requires:	libdvdcss >= 1.4.1}
Requires:	libfmt >= 6.1.2
Requires:	libmicrohttpd >= 0.9.40
Requires:	libplist >= 2.0
Requires:	libudfread >= 1.0.0
Requires:	lsb-release
Requires:	openssl >= 1.0.2
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

%package common
Summary:	Common files for Kodi
BuildArch:	noarch

%description common
Common files for Kodi.

%package devel
Summary:	Header files for Kodi
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description devel
Header files for Kodi.

%prep
%setup -q -n xbmc-%{version}%{?subver}-%{codename}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} -r lib/win32

%if %{without system_ffmpeg}
#ln -s %{SOURCE1} tools/depends/target/ffmpeg/ffmpeg-2.4.4-%{codename}.tar.gz
%endif

%build
%cmake -B build \
	-DAPP_RENDER_SYSTEM=%{!?with_gles:gl}%{?with_gles:gles} \
	-DCORE_PLATFORM_NAME="%{?with_gbm:GBM;}%{?with_x11:X11;}%{?with_wayland:WAYLAND;}" \
	%{cmake_on_off airtunes ENABLE_AIRTUNES} \
	%{cmake_on_off dvdcss ENABLE_DVDCSS} \
	-DENABLE_INTERNAL_CROSSGUID:BOOL=OFF \
	-DENABLE_INTERNAL_DAV1D:BOOL=OFF \
	-DENABLE_INTERNAL_FFMPEG:BOOL=%{?with_system_ffmpeg:OFF}%{!?with_system_ffmpeg:ON} \
	-DENABLE_INTERNAL_FLATBUFFERS:BOOL=OFF \
	-DENABLE_INTERNAL_FMT:BOOL=OFF \
	-DENABLE_INTERNAL_FSTRCMP:BOOL=OFF \
	-DENABLE_INTERNAL_LIBDVD:BOOL=OFF \
	-DENABLE_INTERNAL_RapidJSON:BOOL=OFF \
	-DENABLE_INTERNAL_SPDLOG:BOOL=OFF \
	-DENABLE_INTERNAL_UDFREAD:BOOL=OFF \
	%{cmake_on_off gold ENABLE_LDGOLD} \
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
	%{cmake_on_off sse42 ENABLE_SSE4_2}

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
%attr(755,root,root) %{_bindir}/JsonSchemaBuilder
%attr(755,root,root) %{_bindir}/TexturePacker
%attr(755,root,root) %{_bindir}/kodi
%attr(755,root,root) %{_bindir}/kodi-standalone
%{_datadir}/%{name}/addons
%{_datadir}/%{name}/media
%{_datadir}/%{name}/privacy-policy.txt
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%attr(755,root,root) %{_libdir}/%{name}
%{_desktopdir}/kodi.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/org.xbmc.kodi.metainfo.xml
%{_datadir}/xsessions/kodi.desktop

%files common
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/kodi
%{_datadir}/%{name}/cmake
