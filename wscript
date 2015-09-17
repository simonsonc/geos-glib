def options(ctx):
    ctx.load('compiler_cxx')
    ctx.load('gob2', tooldir='wtools')

def configure(ctx):
    ctx.load('compiler_cxx')
    ctx.env.append_value('CXXFLAGS', '-std=c++11')
    ctx.load('gob2', tooldir='wtools')
    ctx.env.append_value('GOB2FLAGS', '--no-extern-c')

    ctx.check_cfg(package='glib-2.0', args='--libs --cflags', uselib_store='GLIB2')
    ctx.check_cfg(package='', path='geos-config', args='--cclibs --cflags', uselib_store='GEOS')

def build(ctx):
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

    ctx.shlib(features='cxx', name='geos-glib', source=sources, use='GLIB2 GEOS')
