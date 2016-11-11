Import ova to VirtualBox
========================
'''
VBoxManage import <filename>.ova  --vsys 0 --eula accept  
VBoxManage list vms
>> "XXX 4.1" {some hash}
'''

Vagrant
=======
"""
vagrant package --base acef4c0a-35be-4640-a214-be135417f04d --output xxx.box 
vagrant box add xxx.box --name champbase
'''
"""
Vagrant.configure("2") do |config|
  config.vm.box = "champbase"
  # ...
end
"""