# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.ssh.insert_key = false
  config.vbguest.auto_update = true
  config.ssh.forward_x11 = true

  config.vm.synced_folder "html", "/home/vagrant/html"

  config.vm.define "webservidor" do |web_config|
    web_config.vm.box = "ubuntu/trusty64"
    web_config.vm.hostname = "webservidor"
    web_config.vm.network "private_network", ip: "192.168.56.21"
    #web_config.vm.network "forwarded_port", guest: 80, host: 8080
    web_config.vm.synced_folder "html", "/home/vagrant/html"
    web_config.vm.provider "virtualbox" do |vb|
      vb.name = "webservidor"
      opts = ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize opts
      vb.memory = "256"
    end # of vb
    # web_config.vm.provision "shell", path: "bootstrap_web.sh"
   end # of web_config

   config.vm.define "webcliente" do |client_config|
     client_config.vm.box = "ubuntu/trusty64"
     client_config.vm.hostname = "webcliente"
     client_config.vm.network "private_network", ip: "192.168.56.11"
     client_config.vm.provider "virtualbox" do |vb|
       vb.name = "webcliente"
       opts = ["modifyvm", :id, "--natdnshostresolver1", "on"]
       vb.customize opts
       vb.memory = "256"
     end # of vb
     client_config.vm.provision "shell", path: "bootstrap-client.sh"
   end # of client_config

end # of config
