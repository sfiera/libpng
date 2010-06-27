{
    'target_defaults': {
        'xcode_settings': {
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
            'SDKROOT': 'macosx10.4',
            'GCC_VERSION': '4.0',
            'ARCHS': 'ppc x86_64 i386',
            'WARNING_CFLAGS': [
                '-Wall',
                '-Wendif-labels',
            ],
        },
    },
    'targets': [
        {
            'target_name': 'libpng',
            'type': '<(library)',
            'sources': [
                'png.c',
                'pngset.c',
                'pngget.c',
                'pngrutil.c',
                'pngtrans.c',
                'pngwutil.c',
                'pngread.c',
                'pngrio.c',
                'pngwio.c',
                'pngwrite.c',
                'pngrtran.c',
                'pngwtran.c',
                'pngmem.c',
                'pngerror.c',
                'pngpread.c',
            ],
            'link_settings': {
                'libraries': [
                    '/usr/lib/libz.dylib',
                ],
            },
        },
        {
            'target_name': 'pngtest',
            'type': 'executable',
            'sources': [ 'pngtest.c' ],
            'dependencies': [
                'libpng',
            ],
        },
    ],
}
