%define qgstmajor 1

%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %nil

%define qgsttools_p %mklibname qgsttools_p %{qgstmajor}
%define qgsttools_p_d %mklibname qgsttools_p -d

%define qtmultimedia %mklibname qt%{api}multimedia %{major}
%define qtmultimediad %mklibname qt%{api}multimedia -d
%define qtmultimedia_p_d %mklibname qt%{api}multimedia-private -d

%define qtmultimediaquick_p %mklibname qt%{api}multimediaquick_p %{major}
%define qtmultimediaquick_p_d %mklibname qt%{api}multimediaquick_p -d

%define qtmultimediawidgets %mklibname qt%{api}multimediawidgets %{major}
%define qtmultimediawidgetsd %mklibname qt%{api}multimediawidgets -d
%define qtmultimediawidgets_p_d %mklibname qt%{api}multimediawidgets-private -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtmultimedia
Version:	5.5.1
%if "%{beta}" != ""
Release:	1.%{beta}.1
%define qttarballdir qtmultimedia-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	2
%define qttarballdir qtmultimedia-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
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
BuildRequires:	pkgconfig(Qt5Core) = %version
BuildRequires:	pkgconfig(Qt5Gui) = %version
BuildRequires:	pkgconfig(Qt5Qml) = %version
BuildRequires:	pkgconfig(Qt5Quick) = %version

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%_qt5_plugindir/audio/*.so
%_qt5_plugindir/mediaservice/*.so
%_qt5_plugindir/playlistformats/*.so
%ifarch %arm
%_qt5_plugindir/video/videonode/*.so
%endif
%_qt5_prefix/qml/QtAudioEngine
%_qt5_prefix/qml/QtMultimedia

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
%{_qt5_exampledir}/multimedia
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
%ifarch %arm
%{_qt5_libdir}/cmake/Qt5Quick/Qt5Quick_QSGVideoNodeFactory_EGL.cmake
%endif
%{_qt5_includedir}/QtMultimediaWidgets
%exclude %{_qt5_includedir}/QtMultimediaWidgets/%version
%{_qt5_libdir}/libQt5MultimediaWidgets.so
%{_qt5_libdir}/libQt5MultimediaWidgets.prl
%{_qt5_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{_qt5_exampledir}/multimediawidgets
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

%package -n %{qgsttools_p}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qgsttools_p}
Qt%{api} Lib.

%files -n %{qgsttools_p}
%{_qt5_libdir}/libqgsttools_p.so.%{qgstmajor}*

#------------------------------------------------------------------------------

%package -n %{qgsttools_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qgsttools_p} = %version

%description -n %{qgsttools_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qgsttools_p_d}
%{_qt5_libdir}/libqgsttools_p.prl
%{_qt5_libdir}/libqgsttools_p.so

#------------------------------------------------------------------------------

%package -n %{qtmultimediaquick_p}
Summary: Qt%{api} Lib
Group: System/Libraries

%description -n %{qtmultimediaquick_p}
Qt%{api} Lib.

%files -n %{qtmultimediaquick_p}
%{_qt5_libdir}/libQt5MultimediaQuick_p.so.%{api}*

#------------------------------------------------------------------------------

%package -n %{qtmultimediaquick_p_d}
Summary: Devel files needed to build apps based on QtVersit
Group:    Development/KDE and Qt
Requires: %{qgsttools_p} = %version

%description -n %{qtmultimediaquick_p_d}
Devel files needed to build apps based on QtVersit.

%files -n %{qtmultimediaquick_p_d}
%{_qt5_libdir}/libQt5MultimediaQuick_p.prl
%{_qt5_libdir}/libQt5MultimediaQuick_p.so
%{_qt5_includedir}/QtMultimediaQuick_p
%{_qt5_libdir}/pkgconfig/Qt5MultimediaQuick_p.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%apply_patches

%build
%qmake_qt5 GST_VERSION=1.0

#------------------------------------------------------------------------------
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

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
