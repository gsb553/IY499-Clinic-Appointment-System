import java.util.Scanner;

public class ShapeManagement {
    private static Scanner input = new Scanner(System.in);
    private static ShapeList shapes = new ShapeList();

    public static void main(String[] args) {
        boolean running = true;

        while (running) {
            showMenu();
            int choice = readInt("Choose an option: ");

            switch (choice) {
                case 1:
                    addShapeMenu();
                    break;
                case 2:
                    removeShapeMenu();
                    break;
                case 3:
                    showOneShapeMenu();
                    break;
                case 4:
                    areaAndPerimeterMenu();
                    break;
                case 5:
                    System.out.println(shapes.display());
                    break;
                case 6:
                    translateAllShapesMenu();
                    break;
                case 7:
                    scaleAllShapesMenu();
                    break;
                case 0:
                    running = false;
                    System.out.println("Program closed.");
                    break;
                default:
                    System.out.println("Invalid option. Please choose again.");
                    break;
            }
        }
    }

    private static void showMenu() {
        System.out.println();
        System.out.println("Shape Management Menu");
        System.out.println("1: Add a shape");
        System.out.println("2: Remove a shape by position");
        System.out.println("3: Get information about a shape by position");
        System.out.println("4: Area and perimeter of a shape by position");
        System.out.println("5: Display all shapes");
        System.out.println("6: Translate all shapes");
        System.out.println("7: Scale all shapes");
        System.out.println("0: Quit program");
    }

    private static void addShapeMenu() {
        System.out.println();
        System.out.println("Choose shape type:");
        System.out.println("1: Rectangle");
        System.out.println("2: Square");
        System.out.println("3: Circle");
        System.out.println("4: Triangle");

        int shapeChoice = readInt("Shape option: ");

        if (shapeChoice == 1) {
            int x = readInt("Enter x coordinate: ");
            int y = readInt("Enter y coordinate: ");
            int width = readInt("Enter width: ");
            int length = readInt("Enter length: ");

            Rectangle rectangle = new Rectangle(new Coordinates(x, y), width, length);
            shapes.addShape(rectangle);
            System.out.println("Rectangle added.");

        } else if (shapeChoice == 2) {
            int x = readInt("Enter x coordinate: ");
            int y = readInt("Enter y coordinate: ");
            int side = readInt("Enter side length: ");

            Square square = new Square(new Coordinates(x, y), side);
            shapes.addShape(square);
            System.out.println("Square added.");

        } else if (shapeChoice == 3) {
            int x = readInt("Enter x coordinate: ");
            int y = readInt("Enter y coordinate: ");
            int radius = readInt("Enter radius: ");

            Circle circle = new Circle(new Coordinates(x, y), radius);
            shapes.addShape(circle);
            System.out.println("Circle added.");

        } else if (shapeChoice == 4) {
            int x1 = readInt("Enter vertex 1 x: ");
            int y1 = readInt("Enter vertex 1 y: ");
            int x2 = readInt("Enter vertex 2 x: ");
            int y2 = readInt("Enter vertex 2 y: ");
            int x3 = readInt("Enter vertex 3 x: ");
            int y3 = readInt("Enter vertex 3 y: ");

            Triangle triangle = new Triangle(
                    new Coordinates(x1, y1),
                    new Coordinates(x2, y2),
                    new Coordinates(x3, y3)
            );

            shapes.addShape(triangle);
            System.out.println("Triangle added.");

        } else {
            System.out.println("Invalid shape option.");
        }
    }

    private static void removeShapeMenu() {
        int position = readInt("Enter shape position to remove: ");
        Shape removedShape = shapes.removeShape(position - 1);

        if (removedShape == null) {
            System.out.println("No shape exists in that position.");
        } else {
            System.out.println("Shape removed.");
        }
    }

    private static void showOneShapeMenu() {
        int position = readInt("Enter shape position: ");
        Shape selectedShape = shapes.getShape(position - 1);

        if (selectedShape == null) {
            System.out.println("No shape exists in that position.");
        } else {
            System.out.println(selectedShape.display());
        }
    }

    private static void areaAndPerimeterMenu() {
        int position = readInt("Enter shape position: ");
        Shape selectedShape = shapes.getShape(position - 1);

        if (selectedShape == null) {
            System.out.println("No shape exists in that position.");
        } else {
            System.out.println("Area = " + selectedShape.getArea());
            System.out.println("Perimeter = " + selectedShape.getPerimeter());
        }
    }

    private static void translateAllShapesMenu() {
        int dx = readInt("Enter x distance: ");
        int dy = readInt("Enter y distance: ");

        shapes.translateShapes(dx, dy);
        System.out.println("All shapes translated.");
    }

    private static void scaleAllShapesMenu() {
        int factor = readInt("Enter scale factor: ");

        if (factor == 0) {
            System.out.println("Scale factor cannot be zero.");
        } else {
            System.out.println("Enter 1 to multiply or 2 to divide:");
            int scaleChoice = readInt("Scale option: ");

            if (scaleChoice == 1) {
                shapes.scale(factor, true);
                System.out.println("All shapes increased.");
            } else if (scaleChoice == 2) {
                shapes.scale(factor, false);
                System.out.println("All shapes decreased.");
            } else {
                System.out.println("Invalid scale option.");
            }
        }
    }

    private static int readInt(String message) {
        System.out.print(message);

        while (!input.hasNextInt()) {
            System.out.println("Please enter a whole number.");
            input.next();
            System.out.print(message);
        }

        return input.nextInt();
    }
}