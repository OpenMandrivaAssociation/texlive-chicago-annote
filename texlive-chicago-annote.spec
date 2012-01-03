# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/chicago-annote/chicago-annote.bst
# catalog-date 2009-02-03 15:12:24 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-chicago-annote
Version:	20090203
Release:	2
Summary:	Chicago-based annotated BibTeX style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago-annote/chicago-annote.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a revision of chicagoa.bst, using the commonly-used
annote field in place of the original's annotation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
