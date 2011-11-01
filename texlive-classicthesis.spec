Name:		texlive-classicthesis
Version:	3.0
Release:	1
Summary:	A "classically styled" thesis package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/classicthesis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/classicthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The classicthesis package provides an elegant layout designed
in homage to Bringhurst's "The Elements of Typographic Style".
It makes use of a range of techniques to get the best results
achievable using TeX. Included in the bundle are templates to
make thesis writing easier.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/classicthesis/classicthesis-preamble.sty
%{_texmfdistdir}/tex/latex/classicthesis/classicthesis.sty
%doc %{_texmfdistdir}/doc/latex/classicthesis/Bibliography.bib
%doc %{_texmfdistdir}/doc/latex/classicthesis/CHANGES
%doc %{_texmfdistdir}/doc/latex/classicthesis/COPYING
%doc %{_texmfdistdir}/doc/latex/classicthesis/Chapters/Chapter01.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/Chapters/Chapter02.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/Chapters/Chapter03.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/Chapters/Chapter0A.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/ClassicThesis.pdf
%doc %{_texmfdistdir}/doc/latex/classicthesis/ClassicThesis.tcp
%doc %{_texmfdistdir}/doc/latex/classicthesis/ClassicThesis.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/ClassicThesis.tps
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-article.pdf
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-article.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-book.pdf
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-book.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-cv.pdf
%doc %{_texmfdistdir}/doc/latex/classicthesis/Examples/classicthesis-cv.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Abstract.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Acknowledgments.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Bibliography.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Colophon.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Contents.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Declaration.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Dedication.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/DirtyTitlepage.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Publication.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Titleback.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/FrontBackmatter/Titlepage.tex
%doc %{_texmfdistdir}/doc/latex/classicthesis/LISTOFFILES
%doc %{_texmfdistdir}/doc/latex/classicthesis/README
%doc %{_texmfdistdir}/doc/latex/classicthesis/gfx/TFZsuperellipse_bw.pdf
%doc %{_texmfdistdir}/doc/latex/classicthesis/gfx/example_1.jpg
%doc %{_texmfdistdir}/doc/latex/classicthesis/gfx/example_2.jpg
%doc %{_texmfdistdir}/doc/latex/classicthesis/gfx/example_3.jpg
%doc %{_texmfdistdir}/doc/latex/classicthesis/gfx/example_4.jpg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
