{
	nixpkgs ? import <nixpkgs>,
}:

let
	pkgs = nixpkgs {};
	pythonPackages = pkgs.pythonPackages;
	callPackage = pkgs.lib.callPackageWith (pkgs // localPkgs);
	localPkgs = {
		lwes = callPackage ./nix/lwes.nix {};
		mondemand = callPackage ./nix/mondemand.nix {};
	};
in pkgs.pythonPackages.buildPythonPackage {
	pname = "mondemand";
	version = "1.0.0";
	src = ./.;
	propagatedBuildInputs = [
		localPkgs.mondemand
		pythonPackages.cffi
		pythonPackages.six
		pythonPackages.typing
	];
	nativeBuildInputs = [ pkgs.pkgconfig ];
}
