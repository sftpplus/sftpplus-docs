.. container:: tags pull-left

    `client-side`
    `server-side`
    `security`


HIPAA and HITECH Obligations
############################

Certain organizations that interact with protected health information (PHI)
have obligations to follow HIPAA/HITECH - the **Health Insurance Portability
and Accountability Act (1996)** and the **Health Information Technology for
Economic and Clinical Health Act (2009)**.

The following illustrates a non-exhaustive list of how SFTPPlus can help meet
your organization's regulatory obligations under HIPAA/HITECH.

This guide is aimed at those involved in administering file transfer systems
in hospitals, clinics, health care and medical practice organizations
and practices either in-house or as a third party consultancy.

If you are looking for a secure file transfer software solution in other
compliance jurisdictions for the medical and health care industry, you can
still read the examples below as a guide.
For more information about what we can do for your specific requirements,
please contact the `Sales team <https://www.sftpplus.com/about/contact.html>`_.


..  contents:: :local:


Introduction
============

SFTPPlus can help organizations meet their HIPAA/HITECH obligations by
providing a centralized secure managed file transfer solution using the
`main standard file transfer protocols <https://www.sftpplus.com/product/>`_
over a wide range of supported platforms, with authentication controls and
utilizing a detailed audit trail.

Appropriate processes should be defined by the organization in order that the
obligations are met.
Such processes will vary according to the specific scenario, organization scale
and other factors.

For example, one of the key requirements revolves around the audit trail.
Please see the :doc:`page on the audit trail</guides/event-handlers>`
for more details.

Please note that readership of this page is oriented towards those with
existing familiarity to HIPAA/HITECH recommendations.


Information System Activity Review
==================================

The audit trail allows administrators to conduct a review of records of
information system activity in relation to file transfer activities.

Examples of such changes captured in the audit trail include:

1. Changes to file transfer services such as enabling a service or changing the
   listening port.
2. Changes to different identity and authentication providers of an account.
3. Changes to components that implement custom business logic for file transfer
   workflows.
4. Changes to component states such as the start / stop / failure states.
5. And more as a multitude of components make up the file transfer process.

*Corresponding HIPAA requirements:* § 164.308 (a)(ii)(D)


Access Control
==============

There are a number of components used to configure access control such as
`lock_in_home_folder` options.
Accounts can be application specific, operating system, can authenticate
against an LDAP server, or accounts can be supplied by third party identity
providers.

SFTPPlus can be configured to utilize existing policies and procedures to allow
access only to accounts that have been granted access rights.

*Corresponding HIPAA requirements:* § 164.312 (a)(1)


Unique User Identification
==========================

UUIDs are used by the SFTPPlus server to support renaming of accounts,
services, servers, and to provide a detailed audit of all activities performed
by an entity.
In this case, UUIDs can be set to specific users.

*Corresponding HIPAA requirements:* § 164.312 (a)(2)(i)


Automatic Logoff
================

A timeout can be implemented for a client connection that has been idle for a
configurable amount of time.

*Corresponding HIPAA requirements:* § 164.312 (a)(2)(iii)


Audit Control
=============

SFTPPlus logs changes to settings that pertain to the file transfer process.

Changes to components such as listening ports and protocols are tested and
logged so that changes to the configuration settings are automatically
available (before and after installation).

Since there is a number of components that can be configured when managing file
transfers - such as protocols, listening ports, user / group authentication,
event handlers, email notifications and more - there is a
:doc:`page on the audit trail</guides/event-handlers>` available for further
reading on what is available.

*Corresponding HIPAA requirements:* § 164.312 (b)


Integrity
=========

SFTPPlus logs user actions such as moving, copying, renaming or deleting files
to help organizations implement policies to protect PHI from improper changes.

*Corresponding HIPAA requirements:* § 164.312 (c)(1)(2)


Person or Entity Authentication
===============================

Users are authenticated via application-only settings or via the authentication
methods provided by the operating system.

Use of secure authentication methods such as password stored using one way
encryption method or SSH key-based authentication will also help improve
transmission security when authenticating.

Log in attempts are also included in the audit trail for further review.

*Corresponding HIPAA requirements:* § 164.312 (2)(d), § 164.308 (5)(ii)(C)


Transmission Security
=====================

Transmission settings are logged, thus validating secure transmission of PHI
(protected health information).
For example, SFTPPlus will keep a detailed log of any file transferred
(push / pulled).
This can include details about the initial transfer request
and the status of the request finalization (success / failure).

*Corresponding HIPAA requirements:* § 164.312 (e)(1)


Encryption and Decryption
=========================

SFTPPlus will work with the current encryption/decryption mechanism that is
already available on the operating system in which the software is installed.

*Corresponding HIPAA requirements:* § 164.312 (a)(2)(iv)


Encryption
==========

A number of cryptography method, protocols, and algorithms are supported by
SFTPPlus.
Please see the page on :doc:`cryptography</standards/cryptography>`
for further details.

An example of how SFTPPlus can help organizations with HIPAA/HITECH obligations
is the use of transfer method encryption to help maintain the integrity of ePHI.
Organizations can opt to use FTPS or SFTP for file transfer rather than FTP.

*Corresponding HIPAA requirements:* § 164.312 (e)(2)(ii)


Breach Notification
===================

HIPAA covered entities and their business associates are required to provide
notification following a breach of unsecured protected health information.
Similar breach notification provisions implemented and enforced by the Federal
Trade Commission (FTC), apply to vendors of personal health records and their
third party service providers, pursuant to section 13407 of the HITECH Act.

FIPS 140-2 is required by HHS guidelines to comply with the HITECH breach
notification guidelines. Further details about FIPS 140-2 and SFTPPlus is
available :doc:`in this guide<fips140-2>`.

Further details are available on `on HHS <https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html>`_.

*Corresponding HIPAA requirements:* §§ 164.400-414


Is SFTPPlus HIPAA/HITECH Compliant?
===================================

Customers are reminded that there is no certification for HIPAA/HITECH
compliance and that this page does not serve as confirmation of compliance.

SFTPPlus can help organizations with HIPAA/HITECH obligations.
SFTPPlus is an on-premise software application focusing on secure file transfer
**only**.
Data, including PHI data, is not stored, analyzed, intercepted, or recorded by
SFTPPlus.
Since SFTPPlus acts as a conduit that transports data, as such it is
not an entity considered to be a business associate as there is no need for
access to the PHI.

The SFTPPlus software provides an audit trail of events that have taken place
during the file transfer process.
These logs are stored on-premise.
Customers with HIPAA/HITECH obligations that are required to send logs to
Pro:Atria Support are encouraged to sanitize logs sent through as an additional
measure.
