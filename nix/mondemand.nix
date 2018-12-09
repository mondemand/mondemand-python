{ stdenv, fetchurl, lwes, perl, pkgconfig }:

stdenv.mkDerivation rec {
	name = "mondemand-${version}";
	version = "4.4.2";

	src = fetchurl {
		url = "https://github.com/mondemand/mondemand/releases/download/${version}/mondemand-${version}.tar.gz";
		sha256 = "b137bd25cdd7f6b8cf4314af62c9b6706a35b845901dde2f1a62bb847684c9f9";
	};

	buildInputs = [ perl pkgconfig ];
	propagatedBuildInputs = [ lwes ];
	enableParallelBuilding = true;

	meta = {
		description = "Mondemand C library";
		homepage = http://mondemand.github.io;
		license = stdenv.lib.licenses.bsd3;
	};
}
