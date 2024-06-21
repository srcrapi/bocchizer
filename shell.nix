{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3Packages.virtualenv
    pkgs.tk
    pkgs.python3Packages.flask
    pkgs.python3Packages.pywebview
    pkgs.python3Packages.selenium
    pkgs.python3Packages.pandas
    pkgs.python3Packages.webdriver-manager 
    pkgs.python3Packages.tkinter
    pkgs.python3Packages.pycairo
    pkgs.python3Packages.typing-extensions
  ];

  shellHook = ''
    echo "Ambiente configurado para desenvolvimento com Python, Flask e Tkinter"
  '';
}
