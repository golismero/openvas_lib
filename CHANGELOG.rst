Version 0.1.1
=============

- Added support for OpenVAS 7 and 8! (currently in beta mode).
- Support for Python 3 (in testing also)

Version 0.1.0
=============

API changes
-----------

  * Reorganized files structure
  * Simplified API
  * Properties names and types changed:
    - cve -> cves (str -> list).
    - bid -> bids (str -> list).
    - bugtraq -> bugtraqs (str -> list)
    - description -> raw description
    - cvss: str -> float

Other changes
-------------

  * A lot of bug was fixed.
  * Improved stability
  * Added 4 new properties for NVT:
    - impact
    - summary
    - affected_software
    - solution
    - vulnerability_insight
    - cvss_base_vector
  * Now, report texts are cleaned for \n, \r, \t characters. Texts are so reusable a have good readability.
  * Added many unit test.
  * Added 2 .xml report for testing.
  * Now you can use only the parser as stand alone mode with function "report_parser".

Version 0.0.1
=============

Initial release