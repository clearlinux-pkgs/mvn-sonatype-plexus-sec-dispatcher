#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-sonatype-plexus-sec-dispatcher
Version  : 1.3
Release  : 1
URL      : https://repo1.maven.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.jar
Source0  : https://repo1.maven.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.jar
Source1  : https://repo1.maven.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.pom
Source2  : https://repo1.maven.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.4/plexus-sec-dispatcher-1.4.jar
Source3  : https://repo1.maven.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.4/plexus-sec-dispatcher-1.4.pom
Source4  : https://repo1.maven.org/maven2/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3/nexus-staging-maven-plugin-1.6.3.jar
Source5  : https://repo1.maven.org/maven2/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3/nexus-staging-maven-plugin-1.6.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-sonatype-plexus-sec-dispatcher-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-sonatype-plexus-sec-dispatcher package.
Group: Data

%description data
data components for the mvn-sonatype-plexus-sec-dispatcher package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.jar
/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.pom
/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4/plexus-sec-dispatcher-1.4.jar
/usr/share/java/.m2/repository/org/sonatype/plexus/plexus-sec-dispatcher/1.4/plexus-sec-dispatcher-1.4.pom
/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3/nexus-staging-maven-plugin-1.6.3.jar
/usr/share/java/.m2/repository/org/sonatype/plugins/nexus-staging-maven-plugin/1.6.3/nexus-staging-maven-plugin-1.6.3.pom