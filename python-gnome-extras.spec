%define		module			gnome-python-extras
%define		pygtk_req		2:2.8.0
%define		gnome_python_req	2.12.1-3

# Conditional builds:
%bcond_without	mozilla_firefox	# build without mozilla-firefox-devel

Summary:	GNOME bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek GNOME
Name:		python-gnome-extras
Version:	2.14.0
Release:	1
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python-extras/2.14/%{module}-%{version}.tar.bz2
# Source0-md5:	e9390569e18a5e71da1ed9476fa750b3
Patch0:		%{name}-MOZILLA_HOME.patch
Patch1:		%{name}-libgda20.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtkspell-devel >= 2.0.8
BuildRequires:	hal-devel
BuildRequires:	libgda-devel >= 1.9.100-2
BuildRequires:	gdl-devel >= 0.4.0
BuildRequires:	libgksu-devel >= 1.2.5
BuildRequires:	libgksuui-devel >= 1.0.3
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libgtkhtml-devel >= 2.6.3
BuildRequires:	librsvg-devel >= 1:2.9.5-2
BuildRequires:	libtool
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel
%endif
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GNOME bindings for Python.

%description -l pl
Wi±zania Pythona do bibliotek GNOME.

%package devel
Summary:	Development files for GNOME bindings for Python
Summary(pl):	Pliki programistyczne wi±zañ Pythona do GNOME
Group:		Libraries/Python
Requires:	%{name}-gtkhtml = %{version}-%{release}
Requires:	%{name}-egg = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl
Pliki programistyczne wi±zañ Pythona do GNOME.

%package examples
Summary:	Example programs for python-gnome-extras
Summary(pl):	Przyk³adowe programy do python-gnome-extras
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}

%description examples
This package contains example programs for python-gnome-extras.

%description -l pl examples
Ten pakiet zawiera przyk³adowe programy dla python-gnome-extras.

%package egg
Summary:	egg.trayicon bindings for Python
Summary(pl):	Wi±zania Pythona do egg.trayicon
Group:		Libraries/Python
Requires:	python-gnome-ui >= %{gnome_python_req}

%description egg
egg.trayicon bindings for Python.

%description egg -l pl
Wi±zania Pythona do egg.trayicon.

%package gda
Summary:	Libgda bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki libgda
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gda
Libgda bindings for Python.

%description gda -l pl
Wi±zania Pythona do biblioteki libgda.

%package gda-devel
Summary:	Header files for pygda library
Summary(pl):	Pliki nag³ówkowe biblioteki pygda
Group:		Libraries/Python
Requires:	libgda-devel >= 1.9.100-2

%description gda-devel
Header files for pygda library.

%description gda-devel -l pl
Pliki nag³ówkowe biblioteki pygda.

%package gdl
Summary:	GDL bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GDL
Group:		Libraries/Python
Requires:	python-gnome-ui >= %{gnome_python_req}
Requires:	python-pygtk-glade >= %{pygtk_req}
Requires:	gdl >= 0.4.0

%description gdl
GDL bindings for Python.

%description gdl -l pl
Wi±zania Pythona do biblioteki GDL.

%package gtkhtml
Summary:	GtkHtml bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GtkHtml
Group:		Libraries/Python
Requires:	python-gnome-canvas >= %{gnome_python_req}
Obsoletes:	python-gnome-gtkhtml < 2.9.0
Provides:	python-gnome-gtkhtml = %{version}-%{release}

%description gtkhtml
GtkHtml bindings for Python.

%description gtkhtml -l pl
Wi±zania Pythona do biblioteki GtkHtml.

%package gtkspell
Summary:	Gtkspell bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki gtkspell
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gtkspell
Gtkspell bindings for Python.

%description gtkspell -l pl
Wi±zania Pythona do biblioteki gtkspell.

%package libgksu
Summary:	Libgksu and libgksuui bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek libgksu i libgksuui
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description libgksu
Libgksu and libgksuui bindings for Python.

%description libgksu -l pl
Wi±zania Pythona do bibliotek libgksu i libgksuui.

%package mozilla
Summary:	Mozilla bindings for Python
Summary(pl):	Wi±zania Pythona do mozilli
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description mozilla
Mozilla bindings for Python.

%description mozilla -l pl
Wi±zania Pythona do mozilli.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	HTML_DIR=%{_gtkdocdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{*.la,*/{*.la,*.py}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/*
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files egg
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/egg
%attr(755,root,root) %{py_sitedir}/gtk-2.0/egg/*.so
%{py_sitedir}/gtk-2.0/egg/__init__.py?

%files gda
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gda.so

%files gda-devel
%defattr(644,root,root,755)
%{_includedir}/pygda-2.0

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

%files libgksu
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gksu
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gksu/*.so
%{py_sitedir}/gtk-2.0/gksu/*.py?

%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkmozembed.so
%{_gtkdocdir}/pygtkmozembed
