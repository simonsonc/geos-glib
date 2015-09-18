using Geos;

int main(string[] args) {
    var geomf = GeometryFactory.get_default_instance();
    var csf = geomf.get_coordinate_sequence_factory();

    var empty = geomf.create_empty_point();
    stdout.printf("empty point: %s\n", empty.to_string());

    var point_cs = csf.create();
    point_cs.add(new Coordinate.with_xy(1.0, 2.0));
    var point = geomf.create_point(point_cs);
    stdout.printf("point: %s\n", point.to_string());

    var cs = csf.create();
    cs.add(new Coordinate.with_xy(5.0, 3.0));
    cs.add(new Coordinate.with_xy(6.0, 3.0));
    cs.add(new Coordinate.with_xy(6.0, 4.0));
    cs.add(new Coordinate.with_xy(5.0, 3.0));

    stdout.printf("sequence: %s\n", cs.to_string());

    var linestring = geomf.create_line_string(cs);
    stdout.printf("linestring: %s\n", linestring.to_string());

    var linearring = geomf.create_linear_ring(cs);
    stdout.printf("linearing: %s\n", linearring.to_string());

    return 0;
}
