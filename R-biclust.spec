%bcond_with bootstrap
%global packname  biclust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.2
Release:          1
Summary:          BiCluster Algorithms
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/biclust_1.0.2.tar.gz
Requires:         R-MASS R-grid R-colorspace R-lattice R-methods
%if %{without bootstrap}
Requires:         R-flexclust R-isa2 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS
BuildRequires:    R-grid R-colorspace R-lattice R-methods
%if %{without bootstrap}
BuildRequires:    R-flexclust R-isa2
%endif

%description
The main function biclust provides several algorithms to find biclusters
in two-dimensional data: Cheng and Church, Spectral, Plaid Model, Xmotifs
and Bimax. In addition, the package provides methods for data
preprocessing (normalization and discretisation), visualisation, and
validation of bicluster solutions.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

