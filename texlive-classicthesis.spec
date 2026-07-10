%global tl_name classicthesis
%global tl_revision 73676

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.8
Release:	%{tl_revision}.1
Summary:	A classically styled thesis package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/classicthesis
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an elegant layout designed in homage to
Bringhurst's "The Elements of Typographic Style". It makes use of a
range of techniques to get the best results achievable using TeX.
Included in the bundle are templates to make thesis writing easier.

