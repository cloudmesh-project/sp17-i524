#!/usr/bin/env bash

distribution=$(lsb_release -is)
release=$(lsb_release -rs)

PKG_INSTALL=''

case $distribution in
    Ubuntu)
        case $release in
            16.04)
                PKG_INSTALL='apt install'
                sudo $PKG_INSTALL -y python-minimal ansible
                ;;
            *)
                ;;
        esac
        ;;
    *)
        echo "ERROR: Unsupported distribution $distribution"
        exit 1
        ;;
esac

