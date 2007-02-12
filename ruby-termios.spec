Summary:	Ruby termios library
Summary(pl.UTF-8):	Biblioteka termios dla języka Ruby
Name:		ruby-termios
Version:	0.9.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://arika.org/archive/%{name}-%{version}.tar.gz
# Source0-md5:	41db1c72b11d1ac2a950b062922f2fde
URL:		http://arika.org/ruby/termios
BuildRequires:	cracklib-dicts
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-termios provides Termios module to Ruby. Termios module is a
simple wrapper for termios(3). It can be included into IO-family
classes and can extend IO-family objects. In addition, the methods can
use as module function.

%description -l pl.UTF-8
ruby-termios udostępnia moduł Termios dla języka Ruby. Moduł ten to
proste obudowanie termios(3). Może być dołączony do klas z rodziny IO
i może rozszerzać obiekty z rodziny IO. Ponadto załączone metod można
używać jako funkcji modułu.

%prep
%setup -q

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc -o rdoc/ --main README README *.c --title "%{name} %{version}" --inline-source
rdoc --ri -o ri *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_bindir}}

%{__make} install \
  archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitelibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	rubylibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_ridir}/Termios
