%ifarch %{aarch64}
%bcond_with avplayer
%else
%bcond_without avplayer
%endif

%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define qtgsttools %mklibname qt%{api}multimediagsttools %{major}
%define qtgsttools_d %mklibname qt%{api}multimediagsttools -d

%define qgsttools_p %mklibname qgsttools_p 1
%define qgsttools_p_d %mklibname qgsttools_p -d

%define qtmultimedia %mklibname qt%{api}multimedia %{major}
%define qtmultimediad %mklibname qt%{api}multimedia -d
%define qtmultimedia_p_d %mklibname qt%{api}multimedia-private -d

%define qtmultimediaquick %mklibname qt%{api}multimediaquick %{major}
%define qtmultimediaquick_d %mklibname qt%{api}multimediaquick -d

%define qtmultimediaquick_p %mklibname qt%{api}multimediaquick_p %{major}
%define qtmultimediaquick_p_d %mklibname qt%{api}multimediaquick_p -d

%define qtmultimediawidgets %mklibname qt%{api}multimediawidgets %{major}
%define qtmultimediawidgetsd %mklibname qt%{api}multimediawidgets -d
%define qtmultimediawidgets_p_d %mklibname qt%{api}multimediawidgets-private -d

%define qtmultimediaavplayer %mklibname qt%{api}multimediaavplayer %{major}
%define qtmultimediaavplayerd %mklibname qt%{api}multimediaavplayer -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtmultimedia
Version:	5.15.11
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtmultimedia-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtmultimedia-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# Introduce an alternative to ****ing dreadful gstreamer crap
# that can't even handle the pinephone camera
# https://codereview.qt-project.org/c/qt/qtmultimedia/+/305276
Source100:	bcc261c.diff
# And make it compile...
Source101:	qtavplayer-fix-build.patch
# With ffmpeg 5.0 too
Source102:	qtmultimedia-avplayer-ffmpeg-5.0.patch
# Patches from KDE
Patch1001:	0001-Pass-explicit-GL-api-when-initializing-GStreamer-bac.patch
Patch1002:	0002-Drop-obsolete-QtOpengl-dependency.patch
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qt5-qtbase-devel = %version
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(Qt5Core) = %version
BuildRequires:	pkgconfig(Qt5Gui) = %version
BuildRequires:	pkgconfig(Qt5Qml) = %version
BuildRequires:	pkgconfig(Qt5Quick) = %version
# FIXME the autogenerator doesn't see the correct version number
Provides:	qml(QtMultimedia) = %version
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1
%if %{with avplayer}
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(libva-drm)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpulse)
%endif

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%_qt5_plugindir/audio
%_qt5_plugindir/mediaservice
%_qt5_plugindir/playlistformats
# This exists if Qt is built with OpenGL ES support, but not
# with OpenGL desktop
%optional %_qt5_plugindir/video
%_qt5_prefix/qml/QtAudioEngine
%_qt5_prefix/qml/QtMultimedia

#------------------------------------------------------------------------------
%package examples
Summary: Examples for the QtMultimedia engine
Group: Documentation

%description examples
Examples for the QtMultimedia engine

%files examples
%{_qt5_exampledir}/multimedia
%{_qt5_exampledir}/multimediawidgets

#------------------------------------------------------------------------------

%package -n %{qtmultimedia}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtmultimedia}
Qt%{api} Lib.

%files -n %{qtmultimedia}
%{_qt5_libdir}/libQt5Multimedia.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtmultimediad}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtmultimedia} = %{version}
Requires: %{name} = %{version}

%description -n %{qtmultimediad}
Devel files needed to build apps based on QtVersit.

%files -n %{qtmultimediad}
%{_qt5_libdir}/cmake/Qt5Multimedia
%{_qt5_includedir}/QtMultimedia
%exclude %{_qt5_includedir}/QtMultimedia/%version
%{_qt5_libdir}/libQt5Multimedia.so
%{_qt5_libdir}/libQt5Multimedia.prl
%{_qt5_libdir}/pkgconfig/Qt5Multimedia.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_multimedia.pri

#------------------------------------------------------------------------------

%package -n %{qtmultimedia_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtmultimediad} = %version
Provides: qt5-qtmultimedia-private-devel = %version

%description -n %{qtmultimedia_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtmultimedia_p_d}
%{_qt5_includedir}/QtMultimedia/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_multimedia_private.pri

#------------------------------------------------------------------------------

%package -n %{qtmultimediawidgets}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtmultimediawidgets}
Qt%{api} Lib.

%files -n %{qtmultimediawidgets}
%{_qt5_libdir}/libQt5MultimediaWidgets.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtmultimediawidgetsd}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtmultimediawidgets} = %version

%description -n %{qtmultimediawidgetsd}
Devel files needed to build apps based on QtVersit.

%files -n %{qtmultimediawidgetsd}
%{_qt5_libdir}/cmake/Qt5MultimediaWidgets
%{_qt5_includedir}/QtMultimediaWidgets
%exclude %{_qt5_includedir}/QtMultimediaWidgets/%version
%{_qt5_libdir}/libQt5MultimediaWidgets.so
%{_qt5_libdir}/libQt5MultimediaWidgets.prl
%{_qt5_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_multimediawidgets.pri

#------------------------------------------------------------------------------

%package -n %{qtmultimediawidgets_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtmultimediawidgetsd} = %version
Provides: qt5-qtmultimediawidgets-private-devel = %version

%description -n %{qtmultimediawidgets_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtmultimediawidgets_p_d}
%{_qt5_includedir}/QtMultimediaWidgets/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_multimediawidgets_private.pri

#------------------------------------------------------------------------------

%package -n %{qtgsttools}
Summary: Qt%{api} Lib
Group: System/Libraries
Obsoletes: %{qgsttools_p} < %{EVRD}

%description -n %{qtgsttools}
Qt%{api} Lib.

%files -n %{qtgsttools}
%{_qt5_libdir}/libQt%{api}MultimediaGstTools.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{qtgsttools_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qtgsttools} = %{EVRD}
Obsoletes: %{qgsttools_p_d} < %{EVRD}

%description -n %{qtgsttools_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtgsttools_d}
%{_includedir}/qt5/QtMultimediaGstTools
%{_qt5_libdir}/libQt%{api}MultimediaGstTools.prl
%{_qt5_libdir}/libQt%{api}MultimediaGstTools.so
%{_libdir}/qt5/mkspecs/modules/qt_lib_multimediagsttools_private.pri
%{_libdir}/cmake/Qt5MultimediaGstTools

#------------------------------------------------------------------------------

%package -n %{qtmultimediaquick}
Summary: Qt%{api} Lib
Group: System/Libraries
Obsoletes: %{qtmultimediaquick_p} < %{EVRD}

%description -n %{qtmultimediaquick}
Qt%{api} Lib.

%files -n %{qtmultimediaquick}
%{_qt5_libdir}/libQt5MultimediaQuick.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtmultimediaquick_d}
Summary: Devel files needed to build apps based on QtMultimedia Quick
Group:    Development/KDE and Qt
Requires: %{qtgsttools} = %{EVRD}
Obsoletes: %{qtmultimediaquick_p_d} < %{EVRD}

%description -n %{qtmultimediaquick_d}
Devel files needed to build apps based on QtMultimedia Quick.

%files -n %{qtmultimediaquick_d}
%{_qt5_libdir}/libQt5MultimediaQuick.prl
%{_qt5_libdir}/libQt5MultimediaQuick.so
%{_qt5_includedir}/QtMultimediaQuick
%{_libdir}/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri
%{_libdir}/cmake/Qt5MultimediaQuick

#------------------------------------------------------------------------------
%if %{with avplayer}
%package -n %{qtmultimediaavplayer}
Summary: Qt%{api} multimedia lib with FFMPEG backend
Group: System/Libraries

%description -n %{qtmultimediaavplayer}
Qt%{api} multimedia lib with FFMPEG backend.

%files -n %{qtmultimediaavplayer}
%{_libdir}/libQt5MultimediaAVPlayer.so.5*

%package -n %{qtmultimediaavplayerd}
Summary: Devel files needed to build apps based on QtMultimediaAVPlayer
Group:    Development/KDE and Qt
Requires: %{qtmultimediaavplayer} = %{EVRD}
Requires: %{qtmultimediawidgetsd} = %{EVRD}

%description -n %{qtmultimediaavplayerd}
Devel files needed to build apps based on QtMultimediaAVPlayer

%files -n %{qtmultimediaavplayerd}
%{_qt5_includedir}/QtMultimediaAVPlayer
%{_libdir}/cmake/Qt5MultimediaAVPlayer/Qt5MultimediaAVPlayerConfig.cmake
%{_libdir}/cmake/Qt5MultimediaAVPlayer/Qt5MultimediaAVPlayerConfigVersion.cmake
%{_libdir}/libQt5MultimediaAVPlayer.prl
%{_libdir}/libQt5MultimediaAVPlayer.so
%{_libdir}/qt5/mkspecs/modules/qt_lib_multimediaavplayer_private.pri
%endif
#------------------------------------------------------------------------------


%prep
%autosetup -n %(echo %qttarballdir |sed -e 's,-opensource,,') -p1
%if %{with avplayer}
patch -p1 -z .avp1~ -b <%{S:100}
patch -p1 -z .avp2~ -b <%{S:101}
patch -p1 -z .avp2~ -b <%{S:102}
%endif

# Needed after introducing extra headers from Patch0
%{_libdir}/qt5/bin/syncqt.pl -version %{version}

%qmake_qt5 GST_VERSION=1.0

%build
# "|| make" is a workaround for Makefiles that aren't 100% SMP clean
# needed as of 5.15.2 with the avplayer patch
%make_build || make

%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la

# Don't create bogus dependencies
# (QT.multimedia.uses = pulseaudio results in "Project ERROR: Library 'pulseaudio' is not defined." while building qtdeclarative)
sed -i -e 's,^QT.multimedia.uses = pulse,# QT.multimedia.uses = pulse,' %{buildroot}%{_libdir}/qt5/mkspecs/modules/qt_lib_multimedia.pri
