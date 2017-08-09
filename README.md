# IAFC - Internet Archive to Fedora Commons

Mirror an Internet Archive item into a local Fedora Commons repository (proof of concept)

Required: python3.6 + [internetarchive](https://github.com/jjjake/internetarchive) + [pyfc4](https://github.com/ghukill/pyfc4)

## Install Fedora Repository 4

To install Fedora Repository follow the [Quick Start](https://wiki.duraspace.org/display/FEDORA4x/Quick+Start), and set the env:

    $ export FEDORA=http://localhost:8080/rest

## Install IAFC

    $ git clone https://github.com/atomotic/iafc
    $ cd iafc; pip3 install -r requirements.txt

## Run

    $ python3 iafc.py {IA_ITEM}

eg. _https://archive.org/details/TheWebAsHistory_ ➜ `python3 iafc.py TheWebAsHistory`

## Play

$ curl [http://localhost:8080/rest/TheWebAsHistory](http://i.imgur.com/IJiFsqy.png)


    @prefix premis:  <http://www.loc.gov/premis/rdf/v1#> .
    @prefix test:  <info:fedora/test/> .
    @prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsi:  <http://www.w3.org/2001/XMLSchema-instance> .
    @prefix xmlns:  <http://www.w3.org/2000/xmlns/> .
    @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix fedora:  <http://fedora.info/definitions/v4/repository#> .
    @prefix xml:  <http://www.w3.org/XML/1998/namespace> .
    @prefix ebucore:  <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#> .
    @prefix ldp:  <http://www.w3.org/ns/ldp#> .
    @prefix xs:  <http://www.w3.org/2001/XMLSchema> .
    @prefix fedoraconfig:  <http://fedora.info/definitions/v4/config#> .
    @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
    @prefix dc:  <http://purl.org/dc/elements/1.1/> .

    <http://localhost:8080/rest/TheWebAsHistory>
            rdf:type               fedora:Container ;
            rdf:type               fedora:Resource ;
            dc:contributor         "alison.major@ucl.ac.uk"^^<http://www.w3.org/2001/XMLSchema#string> ;
            fedora:lastModifiedBy  "bypassAdmin"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:date                "2017-03-06"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:title               "The Web As History"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:language            "eng"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "Digital humanities"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "Archive"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "history"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "Communication"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "geocities"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "World Wide Web"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:subject             "internet"^^<http://www.w3.org/2001/XMLSchema#string> ;
            fedora:createdBy       "bypassAdmin"^^<http://www.w3.org/2001/XMLSchema#string> ;
            fedora:created         "2017-08-09T08:09:54.405Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
            fedora:lastModified    "2017-08-09T08:14:56.827Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
            dc:creator             " Niels Brügger; Ralph Schroeder, UCL Press"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:identifier          "ark:/13960/t46q76004"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:identifier          "http://archive.org/details/TheWebAsHistory"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:relation            "opensource"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:type                "texts"^^<http://www.w3.org/2001/XMLSchema#string> ;
            dc:description         "The World Wide Web has now been in use for more than 20 years. From early browsers to today’s principal source of information, entertainment and much else, the Web is an integral part of our daily lives, to the extent that some people believe ‘if it’s not online, it doesn’t exist.’ While this statement is not entirely true, it is becoming increasingly accurate, and reflects the Web’s role as an indispensable treasure trove. It is curious, therefore, that historians and social scientists have thus far made little use of the Web to investigate historical patterns of culture and society, despite making good use of letters, novels, newspapers, radio and television programmes, and other pre-digital artefacts.\n This volume argues that now is the time to ask what we have learnt from the Web so far. The 12 chapters explore this topic from a number of interdisciplinary angles – through histories of national web spaces and case studies of different government and media domains – as well as an introduction that provides an overview of this exciting new area of research."^^<http://www.w3.org/2001/XMLSchema#string> ;
            rdf:type               ldp:RDFSource ;
            rdf:type               ldp:Container ;
            fedora:writable        "true"^^<http://www.w3.org/2001/XMLSchema#boolean> ;
            fedora:hasParent       <http://localhost:8080/rest/> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History.gif> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History.pdf> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History_abbyy.gz> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History_djvu.txt> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History_djvu.xml> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History_jp2.zip> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/The-Web-as-History_scandata.xml> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/TheWebAsHistory_archive.torrent> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/TheWebAsHistory_files.xml> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/TheWebAsHistory_meta.sqlite> ;
            ldp:contains           <http://localhost:8080/rest/TheWebAsHistory/files/TheWebAsHistory_meta.xml> .



TODO:

* resource versioning
* pcdm model?

