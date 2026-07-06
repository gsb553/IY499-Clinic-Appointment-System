public class Square extends Shape {
    private int side;

    // Constructor sets the position and side length
    public Square(Coordinates coord, int side) {
        super(4, coord);
        this.side = side;
    }

    // Returns the area of the square
    public double getArea() {
        return side * side;
    }

    // Returns the perimeter of the square
    public double getPerimeter() {
        return 4 * side;
    }

    // Scales the position and side length
    public void scale(int factor, boolean sign) {
        super.scale(factor, sign);

        if (factor != 0) {
            if (sign) {
                side = side * factor;
            } else {
                side = side / factor;
            }
        }
    }

    // Returns all square information
    public String display() {
        return "Square: position (" + getCoordinates().display() + "), side = " + side
                + ", area = " + getArea() + ", perimeter = " + getPerimeter();
    }
}