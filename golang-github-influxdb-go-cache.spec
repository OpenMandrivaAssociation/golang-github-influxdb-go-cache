# http://github.com/influxdb/go-cache

%global goipath         github.com/influxdb/go-cache
%global commit		7d1d6d6ae935664bc8b80ab2b1fc7ab77a7e46da


%gometa -i

Name:           golang-github-influxdb-go-cache
Version:	0
Release:	0.11%{?dist}
Summary:	An in-memory key:value store/cache library for Go
License:	MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
BuildArch:	noarch

%description
An in-memory key:value store/cache (similar to Memcached) library for Go,
suitable for single-machine applications

%package devel
Summary:	An in-memory key:value store/cache library for Go

%description devel
An in-memory key:value store/cache (similar to Memcached) library for Go,
suitable for single-machine applications

This package contains library source intended for 
building other packages which use %{goipath}.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

%files devel -f devel.file-list
%doc LICENSE README CONTRIBUTORS

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git7d1d6d6.git7d1d6d6
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.20130808git7d1d6d6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git7d1d6d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git7d1d6d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git7d1d6d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git7d1d6d6
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git7d1d6d6
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git7d1d6d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git7d1d6d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git7d1d6d6
- First package for Fedora

