%define upstream_name    Dist-Zilla-Plugin-Twitter
%define upstream_version 0.009

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Twitter when you release with Dist::Zilla
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::App::Tester)
BuildRequires: perl(Dist::Zilla::Role::AfterRelease)
BuildRequires: perl(Dist::Zilla::Role::Releaser)
BuildRequires: perl(Dist::Zilla::Role::TextTemplate)
BuildRequires: perl(Dist::Zilla::Tester)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Math::BigFloat)
BuildRequires: perl(Moose)
BuildRequires: perl(Net::Netrc)
BuildRequires: perl(Net::Twitter)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Shorten::TinyURL)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(utf8)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin will use the Net::Twitter manpage with the login and password
in your '.netrc' file to send a release notice to Twitter. By default, it
will include a link to your README file as extracted on a fast CPAN mirror.
This works very nicely with the Dist::Zilla::Plugin::ReadmeFromPod manpage.

The default configuration is as follows:

   [Twitter]
   tweet_url = http://cpan.cpantesters.org/authors/id/{{$AUTHOR_PATH}}/{{$DIST}}-{{$VERSION}}.readme
   tweet = Released {{$DIST}}-{{$VERSION}} {{$URL}}

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%perl_vendorlib/*


