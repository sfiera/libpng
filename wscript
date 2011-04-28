# -*- mode: python -*-

DEFAULTS = {
    "cflags": "-Wall -Werror",
    "arch": "x86_64 i386 ppc",
}

def common(ctx):
    ctx.load("compiler_c")
    ctx.load("platforms", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="z", uselib_store="libpng/system/libz")

def build(bld):
    common(bld)

    bld.stlib(
        target="libpng/libpng",
        source=[
            "png.c",
            "pngset.c",
            "pngget.c",
            "pngrutil.c",
            "pngtrans.c",
            "pngwutil.c",
            "pngread.c",
            "pngrio.c",
            "pngwio.c",
            "pngwrite.c",
            "pngrtran.c",
            "pngwtran.c",
            "pngmem.c",
            "pngerror.c",
            "pngpread.c",
        ],
        includes=".",
        export_includes=".",
        use=[
            "libpng/common",
            "libpng/system/libz",
        ],
        **DEFAULTS
    )

    bld.program(
        target="libpng/pngtest",
        source="pngtest.c",
        use=[
            "libpng/common",
            "libpng/libpng",
        ],
        **DEFAULTS
    )
