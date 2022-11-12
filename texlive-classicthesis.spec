Name:		texlive-classicthesis
Version:	48041
Release:	1
Summary:	A "classically styled" thesis package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/classicthesis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.r48041.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.doc.r48041.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The classicthesis package provides an elegant layout designed
in homage to Bringhurst's "The Elements of Typographic Style".
It makes use of a range of techniques to get the best results
achievable using TeX. Included in the bundle are templates to
make thesis writing easier.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/classicthesis
%doc %{_texmfdistdir}/doc/latex/classicthesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
