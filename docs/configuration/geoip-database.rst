IP geolocation database
=======================

SFTPPlus uses a bundled database to identify the estimated country and autonomous system (AS) associated with public IPv4 and IPv6 addresses.
The Web Manager activity log displays this information for newly recorded events.
Event handlers can access it through `account.peer.country_code`, `account.peer.asn_number`, and `account.peer.asn_name`.
Private addresses and addresses without matching information have empty values.
IP geolocation is an estimate and does not identify a person's location.

Lookups run locally and do not send IP addresses to an external service.
The database uses the `user-country` and `origin-asn` datasets from `ip-location-db <https://github.com/sapics/ip-location-db>`_, published under the `PDDL v1.0 licence <https://opendatacommons.org/licenses/pddl/1-0/>`_.
The bundled database is updated with each new SFTPPlus release.
Existing activity log entries retain their recorded information.
