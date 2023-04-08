{ pkgs }: {
    deps = [
        pkgs.python310
        pkgs.ffmpeg
    ];
    env = {
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
    ];
  };
}