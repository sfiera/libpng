{
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
            'dependencies': [
                ':check-deps',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    '.',
                ],
            },
        },
        {
            'target_name': 'pngtest',
            'type': 'executable',
            'sources': [ 'pngtest.c' ],
            'dependencies': [
                ':check-deps',
                'libpng',
            ],
        },
    ],
}
