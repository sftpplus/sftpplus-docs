Web Administration Console
##########################

..  contents:: :local:


Introduction
============

SFTPPlus provides a web-based administration console / GUI which can be used to configure and operate the SFTPPlus server.

By default, the interface is available over HTTPS on port 10020.


Reverse Proxy / API Gateway integration
=======================================

The administration page can be served via any frontend, be it a reverse HTTP proxy or a load balancer.

The frontend can be configured using any domain name (FQDN), port number, or URL path.
Any standard HTTP reverse-proxy or load balancer will work.
We successfully tested the integration of SFTPPlus with NGINX, HAProxy, and the AWS and Azure application load balancers.

When the SFTPPlus web-based administration console is configured as the backend, it can bind a different port number than the one used by the frontend.

For example, your load balancer can listen on port 443, while SFTPPlus listens on port 10443 behind it.

For HTML cross-site security, it is required to configure the list of sites used via the proxy frontend.
This is done using the `accepted_origins` configuration options.

For example, if you are accessing SFTPPlus via a proxy/load balancer using URLs like `https://admin.gw.example.com` or `https://gw.example.com:10443`, you need to configure SFTPPlus as follows::

    [services/DEFAULT-MANAGER]
    port = 10020
    type: manager
    accepted_origins = admin.gw.example.com, gw.example.com:10443

By default, the SFTPPlus web management uses HTTPS and redirects all HTTP requests to HTTPS.

However, sometimes it is desirable to allow SFTPPlus to fully operate over HTTP, for example on a secured internal network or over VPN.
It is important to make sure that the unsecured port is available only over secured networks.
This can be enforced using a firewall.

To allow unsecure operation over HTTP, you can configure the SFTPPlus management port as follows::

    [services/DEFAULT-MANAGER]
    port = 10019
    type: _manager_unsecured


Reverse proxy examples
======================

SFTPPlus works with any standard HTTP proxy.
For reference, we provide a few examples of configuring 3rd party proxy servers
to act as a frontend for the SFTPPlus web admin console below.

To focus on the SFTPPlus related configuration options,
the HTTPS/SSL/TLS configuration options are not included in these examples.

For these examples,
the frontend is available as `https://admin.gw.example.com:10443/lm/admin`,
while SFTPPlus is accessed in the background as `http://192.167.12.34:10019`.
The following SFTPPlus manager service configuration is required
to accept HTTP connections on port 10019 and expect proxied connections
for the `admin.gw.example.com:10443` website via the `/lm/admin` subpath::

    [services/DEFAULT-MANAGER]
    port = 10010
    type: _manager_unsecured
    accepted_origins = admin.gw.example.com:10443
    base_url_path = /lm/admin


NGINX
-----

Below is an example for the NGINX `location` configuration.
The general core server configuration section is not included in this example,
in order to highlight the SFTPPlus reverse proxy specific configuration::

    location /lm/admin {

        # Add a slash to the URL via redirection
        # and stop doing a reverse proxy.
        if ($request_uri ~ /lm/admin$) {
            return 301 /lm/admin/;
        }

        # Reverse proxy /lm/admin to /
        rewrite /lm/admin/(.*) /$1 break;
        # Make sure there is no trailing slash.
        proxy_pass http://192.167.12.34:10019;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }


HAProxy
-------

Below is an example of HAproxy configuration::

    frontend sftpplusAdmin
        bind *:8080
        mode http
        use_backend adminReverseProxy if { path /lm/admin } || { path_beg /lm/admin/ }

    backend adminReverseProxy
        balance roundrobin
        mode http
        option forwardfor

        # Add a slash so that the paths are always relative.
        http-request redirect scheme http append-slash if { path -m str /lm/admin }

        # In the background any request to /lm/admin is done to / (root).
        http-request replace-path /lm\/admin(/)?(.*) /\2

        server adminServer1 192.167.12.34:10019 check
