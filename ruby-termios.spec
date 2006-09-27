Summary:	Ruby termios library
Name:		ruby-termios
Version:	0.9.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://arika.org/archive/ruby-termios-0.9.4.tar.gz
# Source0-md5:	41db1c72b11d1ac2a950b062922f2fde
URL:		http://arika.org/ruby/termios
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	cracklib-dicts
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-termios provides Termios module to Ruby. Termios module is a simple wrapper for termios(3). It can be included into IO-family classes and can extend IO-family objects. In addition, the methods can use as module function.

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
