{
 nixpkgs ? import <nixpkgs> {},
}:

let

  inherit (nixpkgs) pkgs;

  python = pkgs.pythonFull;
  deps   = with pkgs; [ which libffi ];
  pypkgs = with pkgs.pythonPackages; [ virtualenv pip ];

in

pkgs.stdenv.mkDerivation {
  name = "ansible-cloudmesh-client";
  buildInputs = [ python ] ++  deps ++ pypkgs;
  shellHook = ''
    test -d venv || virtualenv venv
    source venv/bin/activate
    which ansible >/dev/null 2>&1 || pip install ansible
  '';
}
