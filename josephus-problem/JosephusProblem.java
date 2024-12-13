import java.util.*;

public class JosephusProblem {
    
    // Recursive function to find the Josephus position
    public static int josephus(int n, int k) {
        // Base case: when there's only one person left
        if (n == 1) {
            return 0; // The survivor is at position 0 (zero-indexed)
        } else {
            // Recursive step
            return (josephus(n - 1, k) + k) % n;
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the total Number of People: ");
        int n = sc.nextInt(); // Total number of people

        System.out.println("Enter the kth position to be eliminated: ");
        int k = sc.nextInt(); // Every k-th person is eliminated

        // Finding the Josephus position
        int survivor = josephus(n, k) + 1; // +1 to convert to 1-based index
        System.out.println("The survivor is at position: " + survivor);
    }
}
