with import <nixpkgs> { };

let
 tl = (texlive.combine {
   inherit (texlive) scheme-small
   collectbox
   multirow
   titlesec
   soul
   realboxes
   cryptocode
   xargs
   forloop
   pbox
   varwidth
   bigfoot
   environ
   trimspaces
   comment
   mdframed
   zref
   needspace
   enumitem
   ucs
   todonotes
   cleveref
   helvetic
   ; });
in mkShell {
  buildInputs = [
      gnumake
      ghostscript
      tl
  ];
  shellHook = ''
    export PATH="$(pwd)/bin:$PATH"
  '';
}
