# -*- mode: python -*-

def common(ctx):
    ctx.load("compiler_c")
    ctx.load("platforms", "ext/waf-sfiera")
    ctx.load("test", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="z", uselib_store="libpng/system/libz")
    cnf.check(lib="m", uselib_store="libpng/system/libm")

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
        cflags="-Wall -Werror",
        includes=".",
        export_includes=".",
        use=[
            "libpng/system/libm",
            "libpng/system/libz",
        ],
    )

    bld.platform(
        target="libpng/libpng",
        platform="darwin",
        arch="x86_64 i386 ppc",
    )

    bld.program(
        target="libpng/pngtest",
        source="pngtest.c",
        cflags="-Wall -Werror",
        use="libpng/libpng",
    )

    bld.platform(
        target="libpng/pngtest",
        platform="darwin",
        arch="x86_64 i386 ppc",
    )
