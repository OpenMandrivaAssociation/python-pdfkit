Name:		python-pdfkit
Version:	1.0.0
Release:	1
Summary:	Wkhtmltopdf python wrapper to convert html to pdf using the webkit
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pdfkit/
Source0:	pdfkit-1.0.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Wkhtmltopdf python wrapper to convert html to pdf using the webkit.

%files
%{py_sitedir}/*
