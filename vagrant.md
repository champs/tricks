
``` setup
```


``` bash
    vagrant init ubuntu/trusty64; vagrant up --provider virtualbox
    vagrant up
```

If you see this error

``` bash
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default: 
    default: Guest Additions Version: 4.3.36
    default: VirtualBox Version: 5.0
==> default: Mounting shared folders...
    default: /vagrant => /Users/champ-spare/work/vagrant_test
```

Do this

```
    vagrant plugin install vagrant-vbguest
```