import java.util.Scanner;

public class PatientPriority {
    // Class constant for hospital zip code
    private static final String HOSPITAL_ZIP = "12345";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int patientsProcessed = 0;
        int highestPriorityScore = 0;

        printIntroduction();

        while (true) {
            String patientName = getPatientName(scanner);
            if (patientName.equalsIgnoreCase("quit")) {
                printStatistics(patientsProcessed, highestPriorityScore);
                System.out.println("Goodbye!");
                break;
            }

            int priorityScore = collectPatientInformation(scanner);
            patientsProcessed++;

            if (priorityScore > highestPriorityScore) {
                highestPriorityScore = priorityScore;
            }

            printPatientPriority(patientName, priorityScore);
        }
        scanner.close();
    }

    public static void printIntroduction() {
        System.out.println("Hello! We value you and your time, so we will help you prioritize which patients to see next!");
    }

    public static String getPatientName(Scanner scanner) {
        System.out.print("Please enter the next patient's name or 'quit' to end the program: ");
        return scanner.next();
    }

    public static int collectPatientInformation(Scanner scanner) {
        int age;
        String zipCode;
        String inNetwork;
        int painLevel;
        double temperature;

        System.out.print("Patient's age: ");
        age = scanner.nextInt();

        zipCode = getValidZipCode(scanner);

        System.out.print("Is our hospital 'in network' for the patient's insurance? ");
        inNetwork = scanner.next();

        System.out.print("Patient pain level (1-10): ");
        painLevel = getValidPainLevel(scanner);

        System.out.print("Patient temperature (in degrees Fahrenheit): ");
        temperature = scanner.nextDouble();

        return calculatePriority(age, zipCode, inNetwork, painLevel, temperature);
    }

    public static int calculatePriority(int age, String zipCode, String inNetwork, int painLevel, double temperature) {
        int priorityScore = 100; // Base score

        // Age
        if (age < 12 || age >= 75) {
            priorityScore += 50;
        }

        // Zip code
        if (zipCode.charAt(0) == HOSPITAL_ZIP.charAt(0)) {
            priorityScore += 25;
            if (zipCode.charAt(1) == HOSPITAL_ZIP.charAt(1)) {
                priorityScore += 15;
            }
        }

        // In network
        if (inNetwork.equalsIgnoreCase("yes") || inNetwork.equalsIgnoreCase("y")) {
            priorityScore += 33;
        }

        // Pain level
        if (painLevel < 7) {
            priorityScore += painLevel + 10;
        } else {
            priorityScore += painLevel + 70;
        }

        // Temperature
        if (temperature > 99.5) {
            priorityScore += 8;
        }

        return priorityScore;
    }

    public static void printPatientPriority(String name, int score) {
        String priorityCategory;
        if (score >= 270) {
            priorityCategory = "high priority";
            System.out.println("We have determined this patient is " + priorityCategory + ",");
            System.out.println("and it is advised to call an appropriate medical provider ASAP.\n");
        } else if (score >= 164) {
            priorityCategory = "medium priority";
            System.out.println("We have determined this patient is " + priorityCategory + ".");
            System.out.println("Please assign an appropriate medical provider to their case");
            System.out.println("and check back in with the patient's condition in a little while.\n");
        } else {
            priorityCategory = "low priority";
            System.out.println("We have determined this patient is " + priorityCategory + ".");
            System.out.println("Please put them on the waitlist for when a medical provider becomes available.\n");
        }
    }

    public static void printStatistics(int patientsProcessed, int highestPriorityScore) {
        System.out.println("Statistics for the day:");
        System.out.println("Total number of patients processed: " + patientsProcessed);
        System.out.println("Priority score of the highest priority patient processed: " + highestPriorityScore);
    }

    public static String getValidZipCode(Scanner scanner) {
        String zipCode;
        do {
            System.out.print("Patient's zip code: ");
            zipCode = scanner.next();
        } while (!isValidZipCode(zipCode));
        return zipCode;
    }

    public static boolean isValidZipCode(String zipCode) {
        return zipCode.length() == 5 && zipCode.matches("\\d+");
    }

    public static int getValidPainLevel(Scanner scanner) {
        int painLevel;
        do {
            System.out.print("Patient pain level (1-10): ");
            painLevel = scanner.nextInt();
        } while (painLevel < 1 || painLevel > 10);
        return painLevel;
    }
}
