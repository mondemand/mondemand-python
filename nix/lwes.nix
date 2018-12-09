{ stdenv, fetchurl, perl, bison }:

stdenv.mkDerivation rec {
	name = "lwes-${version}";
	version = "1.1.2";

	src = fetchurl {
		url = "https://github.com/lwes/lwes/releases/download/${version}/lwes-${version}.tar.gz";
		sha256 = "fbd8d3bd9153a8fa6286865b4527692683e87f30cf715170fef72659fa5383bd";
	};

	buildInputs = [ perl bison ];
	enableParallelBuilding = true;

	meta = {
		description = "Light Weight Event System C library";
		homepage = http://lwes.github.io/;
		license = stdenv.lib.licenses.bsd3;
	};
}
