public class Coordinates {
    private int x;
    private int y;

    // Constructor sets the x and y coordinates
    public Coordinates(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // Returns the x coordinate
    public int getX() {
        return x;
    }

    // Returns the y coordinate
    public int getY() {
        return y;
    }

    // Calculates the distance between this coordinate and another coordinate
    public double distance(Coordinates p) {
        int xDifference = x - p.getX();
        int yDifference = y - p.getY();

        return Math.sqrt((xDifference * xDifference) + (yDifference * yDifference));
    }

    // Moves the coordinate by dx and dy
    public void translate(int dx, int dy) {
        x = x + dx;
        y = y + dy;
    }

    // Multiplies or divides the coordinates by the factor
    public void scale(int factor, boolean sign) {
        if (factor == 0) {
            System.out.println("Scale factor cannot be zero.");
        } else {
            if (sign) {
                x = x * factor;
                y = y * factor;
            } else {
                x = x / factor;
                y = y / factor;
            }
        }
    }

    // Returns the coordinate information as a String
    public String display() {
        return "X = " + x + ", Y = " + y;
    }
}