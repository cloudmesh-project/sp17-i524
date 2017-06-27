# ansible-cloudmesh-client
Ansible role for installing Cloudmesh Client

# Usage

This can be used both as a role or to install Cloudmesh Client on the local machine

## Role

Add the role to your roles directory as a git submodule

```
$ git submodule add https://github.com/cloudmesh/ansible-cloudmesh-client.git roles/cloudmesh_client
```

You can now include the role in your playbook

```yaml
- name: Install Cloudmesh Client
  hosts: cloudmesh_client_hosts
  roles:
  - role: cloudmesh_client
```

## Local Machine

```
$ git clone https://github.com/cloudmesh/ansible-cloudmesh-client.git
$ cd ansible-cloudmesh-client/local
$ ./setup.sh
$ ansible-playbook -i local/inventory.txt local/site.yml
```


# Defaults

See `defaults/main.yml`.


# License

See the `LICENSE` file.


# Contributing

Contributions are welcome.

1. Please send pull requests to the `dev` branch
2. Add yourself to `CONTRIBUTORS.yml`
