import java.util.ArrayList;

public class ShapeList {
    private ArrayList<Shape> listOfShapes;

    // Constructor creates an empty list of shapes
    public ShapeList() {
        listOfShapes = new ArrayList<Shape>();
    }

    // Adds a shape to the list
    public void addShape(Shape s) {
        listOfShapes.add(s);
    }

    // Translates all shapes in the list
    public void translateShapes(int dx, int dy) {
        for (int i = 0; i < listOfShapes.size(); i++) {
            listOfShapes.get(i).translate(dx, dy);
        }
    }

    // Returns a shape at a position if it exists
    public Shape getShape(int pos) {
        if (pos >= 0 && pos < listOfShapes.size()) {
            return listOfShapes.get(pos);
        } else {
            System.out.println("No shape exists at that position.");
            return null;
        }
    }

    // Removes a shape at a position if it exists
    public Shape removeShape(int pos) {
        if (pos >= 0 && pos < listOfShapes.size()) {
            return listOfShapes.remove(pos);
        } else {
            System.out.println("No shape exists at that position.");
            return null;
        }
    }

    // Returns the area of a shape at a position
    public double area(int pos) {
        Shape selectedShape = getShape(pos);

        if (selectedShape != null) {
            return selectedShape.getArea();
        } else {
            return 0;
        }
    }

    // Scales all shapes in the list
    public void scale(int factor, boolean sign) {
        for (int i = 0; i < listOfShapes.size(); i++) {
            listOfShapes.get(i).scale(factor, sign);
        }
    }

    // Returns the perimeter of a shape at a position
    public double perimeter(int pos) {
        Shape selectedShape = getShape(pos);

        if (selectedShape != null) {
            return selectedShape.getPerimeter();
        } else {
            return 0;
        }
    }

    // Returns the number of shapes in the list
    public int getNumberOfShapes() {
        return listOfShapes.size();
    }

    // Returns information about every shape
    public String display() {
        String output = "";

        if (listOfShapes.size() == 0) {
            output = "There are no shapes in the list.";
        } else {
            for (int i = 0; i < listOfShapes.size(); i++) {
                output = output + "Position " + i + ": " + listOfShapes.get(i).display() + "\n";
            }
        }

        return output;
    }
}