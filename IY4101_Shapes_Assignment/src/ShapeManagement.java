import java.util.Scanner;

public class ShapeManagement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int choice = -1;

        while (choice != 0) {
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
            System.out.print("Choose an option: ");

            if (input.hasNextInt()) {
                choice = input.nextInt();
            } else {
                System.out.println("Please enter a number.");
                input.next();
                choice = -1;
            }

            switch (choice) {
                case 0:
                    System.out.println("Program closed.");
                    break;
                default:
                    System.out.println("This menu option will be completed later.");
                    break;
            }
        }

        input.close();
    }
}