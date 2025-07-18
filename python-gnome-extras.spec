#
# Conditional build:
%bcond_with	gda4			# build gda module / gda4 support
#
%define		module			gnome-python-extras
%define		pygtk_req		2:2.10.4
%define		gnome_python_req	2.16.2
#
Summary:	GNOME bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GNOME
Name:		python-gnome-extras
Version:	2.25.3
Release:	38
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	https://download.gnome.org/sources/gnome-python-extras/2.25/%{module}-%{version}.tar.bz2
# Source0-md5:	9f3b7ec5c57130b96061cb486b79c076
# http://bugzilla.gnome.org/show_bug.cgi?id=584126
Patch0:		%{name}-new-gdl.patch
Patch1:		%{name}-gtkdocdir.patch
URL:		https://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdl-devel >= 3.0.0
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gnome-common
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtkspell-devel >= 2.0.11
%{?with_gda4:BuildRequires:	libgda4-devel >= 3.99.11}
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libgtkhtml-devel >= 2.3.1
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
# for style.css
BuildRequires:	python-pygobject-apidocs
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
%{!?with_gda4:Obsoletes:	python-gnome-extras-gda < 2.25.3-35}
Obsoletes:	python-gnome-extras-libgksu < 2.25.3-33
Obsoletes:	python-gnome-extras-mozilla < 2.25.3-32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek GNOME.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do GNOME
Group:		Libraries/Python
Requires:	%{name}-egg = %{version}-%{release}
Requires:	%{name}-gtkhtml = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}
%{!?with_gda4:Obsoletes:	python-gnome-extras-gda-devel < 2.25.3-35}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do GNOME.

%package examples
Summary:	Example programs for python-gnome-extras
Summary(pl.UTF-8):	Przykładowe programy do python-gnome-extras
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package contains example programs for python-gnome-extras.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla python-gnome-extras.

%package egg
Summary:	egg.trayicon bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do egg.trayicon
Group:		Libraries/Python
Requires:	python-gnome-ui >= %{gnome_python_req}

%description egg
egg.trayicon bindings for Python.

%description egg -l pl.UTF-8
Wiązania Pythona do egg.trayicon.

%package gda
Summary:	Libgda bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libgda
Group:		Libraries/Python
Requires:	libgda4 >= 3.99.11
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gda
Libgda bindings for Python.

%description gda -l pl.UTF-8
Wiązania Pythona do biblioteki libgda.

%package gda-devel
Summary:	Header files for pygda library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pygda
Group:		Libraries/Python
Requires:	libgda4-devel >= 3.99.11
Requires:	python-gnome-devel >= %{gnome_python_req}

%description gda-devel
Header files for pygda library.

%description gda-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pygda.

%package gdl
Summary:	GDL bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GDL
Group:		Libraries/Python
Requires:	gdl >= 0.7.2
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}

%description gdl
GDL bindings for Python.

%description gdl -l pl.UTF-8
Wiązania Pythona do biblioteki GDL.

%package gtkhtml
Summary:	GtkHtml bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GtkHtml
Group:		Libraries/Python
Requires:	python-gnome-canvas >= %{gnome_python_req}
Provides:	python-gnome-gtkhtml = %{version}-%{release}
Obsoletes:	python-gnome-gtkhtml < 2.9.0

%description gtkhtml
GtkHtml bindings for Python.

%description gtkhtml -l pl.UTF-8
Wiązania Pythona do biblioteki GtkHtml.

%package gtkspell
Summary:	Gtkspell bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtkspell
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gtkspell
Gtkspell bindings for Python.

%description gtkspell -l pl.UTF-8
Wiązania Pythona do biblioteki gtkspell.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' examples/egg/trayicon.py

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-docs \
	%{!?with_gda4:--disable-gda} \
	--disable-gksu \
	--disable-gksu2 \
	--disable-gksuui \
	--disable-gtkmozembed

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/*.la}
%py_postclean %{_datadir}/pygtk/2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/gtkhtml2.defs
%{pydefsdir}/trayicon.defs
%{_pkgconfigdir}/gnome-python-extras-2.0.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files egg
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/egg
%attr(755,root,root) %{py_sitedir}/gtk-2.0/egg/*.so
%{py_sitedir}/gtk-2.0/egg/__init__.py[co]

%if %{with gda4}
%files gda
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gda.so

%files gda-devel
%defattr(644,root,root,755)
%{_includedir}/pygda-4.0
%{_datadir}/pygtk/2.0/argtypes/gda-arg-types.py[co]
%{pydefsdir}/gda.defs
%{_pkgconfigdir}/pygda-4.0.pc
%endif

%files gdl
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gdl.so

%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkhtml2.so

%files gtkspell
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkspell.so
%{_gtkdocdir}/pygtkspell
