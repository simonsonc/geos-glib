using Geos;

int main(string[] args) {
    var geomf = GeometryFactory.get_default_instance();
    var csf = geomf.get_coordinate_sequence_factory();

    var empty = geomf.create_empty_point();
    stdout.printf("empty point: %s\n", empty.to_string());

    var cs = csf.create(1, 1);
    var coord = new Coordinate();
    cs.add(coord);
    stdout.printf("sequence: %s\n", cs.to_string());
    var point = geomf.create_point(cs);
    stdout.printf("point: %s\n", point.to_string());

    return 0;
}
