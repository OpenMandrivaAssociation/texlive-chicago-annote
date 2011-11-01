Name:		texlive-chicago-annote
Version:	20090203
Release:	1
Summary:	Chicago-based annotated BibTeX style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago-annote/chicago-annote.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This is a revision of chicagoa.bst, using the commonly-used
annote field in place of the original's annotation.

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
%{_texmfdistdir}/bibtex/bst/chicago-annote/chicago-annote.bst
%doc %{_texmfdistdir}/doc/bibtex/chicago-annote/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
