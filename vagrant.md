setup
-----

``` bash
    vagrant init ubuntu/trusty64; vagrant up --provider virtualbox
    vagrant up
    vagrant ssh
```


vagrant file
------------
```
  config.vm.network :private_network, ip: "192.168.0.59"
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "dev.champ.com"
  config.vm.provision :shell, :path => "vagrant-setup/bootstrap-postgres.sh"
  config.hostsupdater.aliases = ["dev.champ.com", "devchamp.local"]
```

provision file
--------------
```
sudo apt-get install apache2
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

``` ssh
    vagrant plugin install vagrant-vbguest
    vagrant reload
```

If you dont see the share folder, do this

```
sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions
```

useful link

[vagrant hostupdater](https://github.com/cogitatio/vagrant-hostsupdater) will update /etc/hosts 

[ref articles](https://24ways.org/2014/what-is-vagrant-and-why-should-i-care/)

[postgres base](https://github.com/jackdb/pg-app-dev-vm)