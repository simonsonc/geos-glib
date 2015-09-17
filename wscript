def options(ctx):
    ctx.load('compiler_c')
    ctx.load('compiler_cxx')
    ctx.load('gob2', tooldir='wtools')
    ctx.load('local_rpath', tooldir='wtools')
    ctx.load('vala')

def configure(ctx):
    ctx.load('compiler_c')
    ctx.load('compiler_cxx')
    ctx.load('vala')
    ctx.load('local_rpath', tooldir='wtools')
    ctx.env.append_value('CXXFLAGS', '-std=c++11')
    ctx.load('gob2', tooldir='wtools')
    ctx.env['GOB2FLAGS'] = ['--for-cpp', '--no-extern-c', '--no-lines', '--no-self-alias']

    ctx.check_cfg(package='glib-2.0', args='--libs --cflags', uselib_store='GLIB2')
    ctx.check_cfg(package='', path='geos-config', args='--cclibs --cflags', uselib_store='GEOS')

def build(bld):
    sources='''
    src/geos-coordinate.gob
    src/geos-coordinatesequence.gob
    src/geos-coordinatesequencefactory.gob
    src/geos-geometry.gob
    src/geos-geometrycollection.gob
    src/geos-geometryfactory.gob
    src/geos-linestring.gob
    src/geos-linearring.gob
    src/geos-multipoint.gob
    src/geos-point.gob
    src/geos-polygon.gob
    src/geos-polygonizer.gob
    '''

    bld.shlib(features='cxx cxxshlib',
	target='geos-glib',
        source=sources,
        includes = 'src',
        export_includes = 'src',
        use='GLIB2 GEOS')

    bld.add_group()
    bld_files = """
        src/geos-coordinate.cc
        src/geos-coordinate.h
        src/geos-coordinatesequence.cc
        src/geos-coordinatesequence.h
        src/geos-coordinatesequencefactory.cc
        src/geos-coordinatesequencefactory.h
        src/geos-geometry.cc
        src/geos-geometry.h
        src/geos-geometrycollection.cc
        src/geos-geometrycollection.h
        src/geos-geometryfactory.cc
        src/geos-geometryfactory.h
        src/geos-linestring.cc
        src/geos-linestring.h
        src/geos-linearring.cc
        src/geos-linearring.h
        src/geos-multipoint.cc
        src/geos-multipoint.h
        src/geos-point.cc
        src/geos-point.h
        src/geos-polygon.cc
        src/geos-polygon.h
        src/geos-polygonizer.cc
        src/geos-polygonizer.h
    """
    bld(name         = 'geos-glib-gir',
        #source       = src_dir.ant_glob("*.cc") + src_dir.ant_glob('src/*.h') + bld.path.ant_glob("src/*.h"),
        source       = [bld.path.find_or_declare(x) for x in bld_files.split()],
        #source = bld_files,
        target       = 'Geos-1.0.gir',
        install_path = '${LIBDIR}/girepository-1.0',
        rule         = 'g-ir-scanner --warn-all -n Geos --nsversion=1.0'
        ' --no-libtool ' +
        (' --pkg=%s' % 'glib-2.0') +
        (' --pkg-export=%s' % "geos-glib") +
        (' -I%s' % bld.path.find_dir('src').bldpath()) +
        (' -I%s' % bld.path.find_dir('src').srcpath()) +
        (' -L%s' % bld.path) +
        ' --library=geos-glib'
        ' --include=GObject-2.0'
        ' --c-include="geos-glib.h"'
        ' -o ${TGT} ${SRC}')

    bld(name         = 'geos-glib-typelib',
        after        = 'Geos-glib-gir',
        source       = 'Geos-1.0.gir',
        target       = 'Geos-1.0.typelib',
        install_path = '${LIBDIR}/girepository-1.0',
        rule         = 'g-ir-compiler ${SRC} -o ${TGT}')

    bld.add_group()
    bld(name="geos-glib-vapi",
        target = 'geos-glib.vapi',
        after = 'geos-glib-gir',
        source = 'Geos-1.0.gir',
        rule = 'vapigen --library geos-glib ${SRC}')

    bld.add_group()
    bld.recurse('demo')
