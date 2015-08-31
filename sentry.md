#Configure Sentry server.




#Configure Sentry DSN
settings.py - SENTRY_DSN

#command line interface
```
sentry --config=.sentry/sentry.conf.py createsuperuser
sentry --config=.sentry/sentry.conf.py repair --owner=<some_username>
```
