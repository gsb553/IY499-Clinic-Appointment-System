public class Circle extends Shape {
    private int radius;

    // Constructor sets the position and radius
    public Circle(Coordinates coord, int radius) {
        super(0, coord);
        this.radius = radius;
    }

    // Returns the area of the circle
    public double getArea() {
        return Math.PI * radius * radius;
    }

    // Returns the perimeter of the circle
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    // Scales the position and radius
    public void scale(int factor, boolean sign) {
        super.scale(factor, sign);

        if (factor != 0) {
            if (sign) {
                radius = radius * factor;
            } else {
                radius = radius / factor;
            }
        }
    }

    // Returns all circle information
    public String display() {
        return "Circle: position (" + getCoordinates().display() + "), radius = " + radius
                + ", area = " + getArea() + ", perimeter = " + getPerimeter();
    }
}