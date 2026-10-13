Prometheus metrics
==================

Web Manager dependency
----------------------

SFTPPlus exposes process metrics in Prometheus format through the :doc:`Web Manager service <../configuration/local-manager>` at `/metrics`.
Metrics collection by Prometheus requires the Web Manager service to be enabled and running on each SFTPPlus instance being monitored.
Prometheus must be able to connect to that service.
For example, a service listening on port 10020 exposes metrics at `https://sftp.acme.com:10020/metrics`.
When using `base_url_path`, append `/metrics` to that base URL.

Authentication and permissions
------------------------------

Each scrape requires HTTP Basic authentication with an administrator's username and password.
In SFTPPlus, an **administrator** account defines the identity and permissions used to access the metrics endpoint.
For Prometheus monitoring, this account represents the automated scraper.
Create a dedicated administrator account for the scraper and configure Prometheus to use its username and password for each scrape.

Authentication uses the same methods and restrictions as Web Manager password login.
Web Manager session cookies and session tokens do not authenticate metrics requests.
The service's TLS settings also apply to metrics, including mutual TLS when configured.
A client certificate does not replace the administrator's username and password.

The administrator needs `read` permission for `/metrics`.
This permission grants access to all metrics exposed at the endpoint; metrics cannot be restricted by service.

New installations include a role with UUID `DEFAULT-METRICS-ROLE` and name `Metrics role`.
The role grants read access to `/metrics`, which covers every metric exposed by the endpoint.
Installations upgraded from an older version do not receive this role automatically.
To create it manually, configure the role as follows::

    [roles/DEFAULT-METRICS-ROLE]
    name = Metrics role
    permissions = /metrics, read

Associate this role with a dedicated administrator using the Web Manager's **Administrators** page.
Roles with empty permissions retain their existing full administrative access, including metrics.

Exposition format
-----------------

SFTPPlus exports **Prometheus Text Format 1.0.0**, encoded as UTF-8.
The response has the following HTTP header::

    Content-Type: text/plain; version=1.0.0; charset=utf-8

Each metric includes `# HELP` and `# TYPE` lines followed by its sample value.
For example::

    # HELP sftpplus_info SFTPPlus application and build metadata.
    # TYPE sftpplus_info gauge
    sftpplus_info{version="6.1.0",build="20260919",python_version="3.14.0",os="linux",architecture="x86_64",openssl_version="OpenSSL 3.5.0 8 Apr 2025"} 1.0

The endpoint does not export OpenMetrics format.
It returns Prometheus text regardless of the request's `Accept` header, including when a client requests `application/openmetrics-text`.
Configure clients to accept `text/plain`; the endpoint does not negotiate an alternative format.


Available metrics
-----------------

Metrics prefixed with `process_` use well-known Prometheus process metric names.
The `sftpplus_reactor_delay_seconds` metric measures Twisted reactor responsiveness.
Metrics prefixed with `sftpplus_` are specific to SFTPPlus.
The following metrics are available:

..  list-table::
    :header-rows: 1
    :widths: 45 10 45

    * - Metric
      - Type
      - Description
    * - `process_start_time_seconds`
      - Gauge
      - Fixed process start time in seconds since the Unix epoch.
    * - `sftpplus_info`
      - Gauge
      - Application metadata with value 1 and labels `version`, `build`, `python_version`, `os`, `architecture`, and `openssl_version`.
        One series is exposed per running SFTPPlus instance.
        The version includes development, release candidate, and trial suffixes.
        The build is the UTC build date in `YYYYMMDD` format, or `development` when no build date has been generated.
    * - `process_open_fds`
      - Gauge
      - Open file descriptors, or process handles on Windows.
    * - `process_max_fds`
      - Gauge
      - OS soft limit for open file descriptors, recorded when the Web Manager starts.
        An unlimited limit is exported as `+Inf`.
        Omitted when unavailable, including on Windows.
    * - `process_resident_memory_bytes`
      - Gauge
      - Resident process memory in bytes.
    * - `process_virtual_memory_bytes`
      - Gauge
      - Virtual process memory in bytes.
    * - `process_cpu_seconds_total`
      - Counter
      - Total user and system CPU time consumed by the process, in seconds.
        Excludes child process CPU time.
    * - `process_threads`
      - Gauge
      - Number of process threads.
    * - `sftpplus_reactor_delay_seconds`
      - Gauge
      - Delay of the most recent reactor responsiveness check, scheduled every five seconds.

Process start time, application metadata, and the supported file descriptor limit are available even when analytics is stopped.
Other metrics require the analytics resource to be running.
Process usage values are refreshed at the analytics `monitor_interval` and are omitted until the first sample is collected.
Configure the analytics `monitor_interval` to match the Prometheus `scrape_interval` so process usage data is refreshed for each scrape.
An omitted measurement is unknown or unavailable; it is not reported as zero.
A measured value of zero is still exported.
Metrics describe the local process and contain no usernames, IP addresses, or filenames.

Application metadata
--------------------

`sftpplus_info` describes the whole instance and has one series per monitored endpoint.
It is a gauge with value `1`, following the Prometheus convention for info metrics: the value marks the metadata series as present.
The version preserves the full release string, including development and trial suffixes.
The Python version includes the patch number, the operating system name is lowercase, and the architecture uses the runtime's machine identifier.
The `openssl_version` label contains the full OpenSSL version string used by SFTPPlus through pyOpenSSL.

Application metadata can be used for dashboard headers and fleet version counts, for example `count by (version) (sftpplus_info)`.

Scrape configuration
--------------------

For a manual check, use an administrator with the monitoring role::

    curl --cacert /path/to/ca.pem --user monitoring \
        https://sftpplus.example.com:10020/metrics

The command prompts for the administrator's password.
Successful requests return HTTP 200 and Prometheus text.
Missing or invalid credentials return HTTP 401; insufficient permissions return HTTP 403.

An example Prometheus scrape configuration is:

..  code-block:: yaml

    scrape_configs:
      - job_name: sftpplus
        scheme: https
        metrics_path: /metrics
        scrape_interval: 60s
        basic_auth:
          username: monitoring
          password_file: /etc/prometheus/secrets/sftpplus-password
        tls_config:
          ca_file: /etc/prometheus/certs/sftpplus-ca.pem
        static_configs:
          - targets: ['sftpplus.example.com:10020']

For mutual TLS, add `cert_file` and `key_file` to `tls_config` with the paths to the client's certificate and private key.
