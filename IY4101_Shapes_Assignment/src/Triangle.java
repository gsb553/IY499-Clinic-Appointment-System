public class Triangle extends Shape {
    private Coordinates vertex2;
    private Coordinates vertex3;

    // Constructor sets all three triangle vertices
    public Triangle(Coordinates vertex1, Coordinates vertex2, Coordinates vertex3) {
        super(3, vertex1);
        this.vertex2 = vertex2;
        this.vertex3 = vertex3;
    }

    // Returns the distance from vertex 1 to vertex 2
    private double sideA() {
        return getCoordinates().distance(vertex2);
    }

    // Returns the distance from vertex 2 to vertex 3
    private double sideB() {
        return vertex2.distance(vertex3);
    }

    // Returns the distance from vertex 3 to vertex 1
    private double sideC() {
        return vertex3.distance(getCoordinates());
    }

    // Returns the perimeter of the triangle
    public double getPerimeter() {
        return sideA() + sideB() + sideC();
    }

    // Returns the area using Heron's formula
    public double getArea() {
        double a = sideA();
        double b = sideB();
        double c = sideC();
        double s = (a + b + c) / 2;

        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }

    // Moves all three vertices
    public void translate(int dx, int dy) {
        getCoordinates().translate(dx, dy);
        vertex2.translate(dx, dy);
        vertex3.translate(dx, dy);
    }

    // Scales all three vertices
    public void scale(int factor, boolean sign) {
        getCoordinates().scale(factor, sign);
        vertex2.scale(factor, sign);
        vertex3.scale(factor, sign);
    }

    // Returns all triangle information
    public String display() {
        return "Triangle: vertex 1 (" + getCoordinates().display() + "), vertex 2 ("
                + vertex2.display() + "), vertex 3 (" + vertex3.display()
                + "), area = " + getArea() + ", perimeter = " + getPerimeter();
    }
}