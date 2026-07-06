public abstract class Shape {
    private Coordinates position;
    private int sides;

    // Constructor used by all shapes
    public Shape(int noOfSides, Coordinates coord) {
        sides = noOfSides;
        position = coord;
    }

    // Returns the coordinate position of the shape
    public Coordinates getCoordinates() {
        return position;
    }

    // Returns the number of sides
    public int getSides() {
        return sides;
    }

    // Changes the coordinate position
    public void setCoordinates(Coordinates newCoord) {
        position = newCoord;
    }

    // Moves the shape by moving its coordinates
    public void translate(int dx, int dy) {
        position.translate(dx, dy);
    }

    // Scales the shape position
    public void scale(int factor, boolean sign) {
        position.scale(factor, sign);
    }

    // These methods must be written in the child classes
    public abstract double getArea();

    public abstract double getPerimeter();

    public abstract String display();
}