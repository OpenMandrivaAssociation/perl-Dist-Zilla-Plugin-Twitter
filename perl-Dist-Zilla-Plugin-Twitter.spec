%define upstream_name    Dist-Zilla-Plugin-Twitter
%define upstream_version 0.026

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Twitter when you release with Dist::Zilla


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/dagolden/dist-zilla-plugin-twitter
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DOHERTY/Dist-Zilla-Plugin-Twitter-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::Visitor::Callback)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::App::Tester)
BuildRequires:	perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:	perl(Dist::Zilla::Role::Releaser)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(Dist::Zilla::Tester)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Math::BigFloat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::MultiInitArg)
BuildRequires:	perl(Net::Netrc)
BuildRequires:	perl(Net::Twitter)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WWW::Shorten::Simple)
BuildRequires:	perl(WWW::Shorten::TinyURL)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(utf8)
BuildArch:	noarch

%description
This plugin will use the Net::Twitter manpage with the login and password
in your '.netrc' file to send a release notice to Twitter. By default, it
will include a link to your README file as extracted on a fast CPAN mirror.
This works very nicely with the Dist::Zilla::Plugin::ReadmeFromPod manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*



