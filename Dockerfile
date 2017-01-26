FROM nixos/nix

RUN nix-env \
    -iA nixpkgs.texlive.combined.scheme-full \
    -iA nixpkgs.gnumake \
    -iA nixpkgs.python2Full

VOLUME /data
WORKDIR /data
CMD make
