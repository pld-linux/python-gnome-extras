%define		module			gnome-python-extras
%define		pygtk_req		2:2.6.0
%define		gnome_python_req	2.10.0

# Conditional builds:
%bcond_without totem # disable totem support

Summary:	GNOME bindings for Python
Summary(pl):	Wi±zania Pythona do bibliotek GNOME
Name:		python-gnome-extras
Version:	2.10.1
Release:	1
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-python-extras/2.10/%{module}-%{version}.tar.bz2
# Source0-md5:	4258c783e0d8fbf18e9b4b33693384e7
Patch0:		%{name}-MOZILLA_HOME.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.10.1
BuildRequires:	gnome-vfs2-devel >= 2.10.1
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtksourceview-devel >= 1.2.0
BuildRequires:	gtkspell-devel >= 2.0.8
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libgtkhtml-devel >= 2.6.3
BuildRequires:	libgtop-devel >= 2.10.1
BuildRequires:	librsvg-devel >= 1:2.9.5-2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	mozilla-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.10.0-2
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
%{?with_totem:BuildRequires:	totem-devel >= 0.101}
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
Requires:	%{name}-applet = %{version}-%{release}
Requires:	%{name}-gtkhtml = %{version}-%{release}
Requires:	%{name}-nautilus-cd-burner = %{version}-%{release}
Requires:	%{name}-print = %{version}-%{release}
Requires:	%{name}-egg = %{version}-%{release}
Requires:	%{name}-libwnck = %{version}-%{release}
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
Development files for GNOME bindings for Python.

%description devel -l pl
Pliki programistyczne wi±zañ Pythona do GNOME.

%package egg
Summary:	egg.trayicon bindings for Python
Summary(pl):	Wi±zania Pythona do egg.trayicon
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description egg
egg.trayicon bindings for Python.

%description egg -l pl
Wi±zania Pythona do egg.trayicon.

%package applet
Summary:	GNOME Applet bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GNOME Applet
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= %{pygtk_req}
Requires:	python-gnome >= %{gnome_python_req}
Obsoletes:	python-gnome-applet
Provides:	python-gnome-applet

%description applet
GNOME Applet bindings for Python.

%description applet -l pl
Wi±zania Pythona do biblioteki GNOME Applet.

%package print
Summary:	GNOME Print bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GNOME obs³ugi drukowania
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-pango >= %{pygtk_req}
Obsoletes:	python-gnome-print
Obsoletes:	python-gnome-print-ui
Provides:	python-gnome-print
Provides:	python-gnome-print-ui

%description print
GNOME Print bindings for Python.

%description print -l pl
Wi±zania Pythona do biblioteki GNOME obs³ugi drukowania.

%package gtkhtml
Summary:	GtkHtml bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki GtkHtml
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}
Obsoletes:	python-gnome-gtkhtml
Provides:	python-gnome-gtkhtml

%description gtkhtml
GtkHtml bindings for Python.

%description gtkhtml -l pl
Wi±zania Pythona do biblioteki GtkHtml.

%package mozilla
Summary:	Mozilla bindings for Python
Summary(pl):	Wi±zania Pythona do mozilli
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description mozilla
Mozilla bindings for Python.

%description mozilla -l pl
Wi±zania Pythona do mozilli.

%package gtksourceview
Summary:	Gtksourceview bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki gtksourceview
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gtksourceview
Gtksourceview bindings for Python.

%description gtksourceview -l pl
Wi±zania Pythona do biblioteki gtksourceview.

%package gtkspell
Summary:	Gtkspell bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki gtkspell
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description gtkspell
Gtkspell bindings for Python.

%description gtkspell -l pl
Wi±zania Pythona do biblioteki gtkspell.

%package libgtop
Summary:	Libgtop bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki libgtop
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description libgtop
Libgtop bindings for Python.

%description libgtop -l pl
Wi±zania Pythona do biblioteki libgtop.

%package nautilus-cd-burner
Summary:	Nautilus-cd-burner bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki nautilus-cd-burner
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description nautilus-cd-burner
Nautilus-cd-burner bindings for Python.

%description nautilus-cd-burner -l pl
Wi±zania Pythona do biblioteki nautilus-cd-burner.

%package totem
Summary:	Totem bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki totem
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description totem
Totem bindings for Python.

%description totem -l pl
Wi±zania Pythona do biblioteki totem.

%package libwnck
Summary:	Libwnck bindings for Python
Summary(pl):	Wi±zania Pythona do biblioteki libwnck
Group:		Libraries/Python
Requires:	python-pygtk-gtk >= %{pygtk_req}

%description libwnck
Libwnck bindings for Python.

%description libwnck -l pl
Wi±zania Pythona do biblioteki libwnck.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%files egg
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/egg
%attr(755,root,root) %{py_sitedir}/gtk-2.0/egg/*.so
%{py_sitedir}/gtk-2.0/egg/__init__.py?

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeapplet.so
%{py_sitedir}/gtk-2.0/gnome/applet.py?

%files print
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gnomeprint
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gnomeprint/*.so
%{py_sitedir}/gtk-2.0/gnomeprint/*.py?

%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkhtml2.so

%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkmozembed.so

%files gtksourceview
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtksourceview.so

%files gtkspell
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkspell.so

%files libgtop
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtop.so

%files nautilus-cd-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/nautilusburn.so

%if %{with totem}
%files totem
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/totem
%attr(755,root,root) %{py_sitedir}/gtk-2.0/totem/*.so
%{py_sitedir}/gtk-2.0/totem/__init__.py?
%endif

%files libwnck
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/wnck.so
