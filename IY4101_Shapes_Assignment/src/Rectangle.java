public class Rectangle extends Shape {
    private int width;
    private int length;

    // Constructor sets the position, width and length
    public Rectangle(Coordinates coord, int width, int length) {
        super(4, coord);
        this.width = width;
        this.length = length;
    }

    // Returns the area of the rectangle
    @Override
    public double getArea() {
        return width * length;
    }

    // Returns the perimeter of the rectangle
    @Override
    public double getPerimeter() {
        return (2 * width) + (2 * length);
    }

    // Scales the position, width and length
    @Override
    public void scale(int factor, boolean sign) {
        if (factor != 0) {
            super.scale(factor, sign);

            if (sign) {
                width = width * factor;
                length = length * factor;
            } else {
                width = width / factor;
                length = length / factor;
            }
        }
    }

    // Returns all rectangle information
    @Override
    public String display() {
        return "Rectangle: position (" + getCoordinates().display() + "), width = " + width
                + ", length = " + length + ", area = " + getArea()
                + ", perimeter = " + getPerimeter();
    }
}