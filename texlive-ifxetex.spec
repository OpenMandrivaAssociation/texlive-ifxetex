# revision 19685
# category Package
# catalog-ctan /macros/generic/ifxetex
# catalog-date 2009-01-27 08:30:55 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-ifxetex
Version:	0.5
Release:	1
Summary:	Am I running under XeTeX?
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/ifxetex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxetex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxetex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A simple package which provides an \ifxetex conditional, so
that other code can determine that it is running under XeTeX.
The package requires the e-TeX extensions to the TeX primitive
set.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ifxetex/ifxetex.sty
%doc %{_texmfdistdir}/doc/generic/ifxetex/README
%doc %{_texmfdistdir}/doc/generic/ifxetex/ifxetex.pdf
#- source
%doc %{_texmfdistdir}/source/generic/ifxetex/ifxetex.ins
%doc %{_texmfdistdir}/source/generic/ifxetex/ifxetex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
