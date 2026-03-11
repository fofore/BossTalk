{ pkgs }: {
  deps = [
    pkgs.python311Packages.pip
    pkgs.python311Packages.flask
    pkgs.python311Packages.flask-cors
  ];
}
