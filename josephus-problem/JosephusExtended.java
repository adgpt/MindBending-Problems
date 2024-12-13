import java.util.ArrayList;
import java.util.List;

public class JosephusExtended {
    
    // Recursive function to find the Josephus position
    public static int josephus(int n, int k) {
        // Base case: when there's only one person left
        if (n == 1) {
            return 0; // The survivor is at position 0 (zero-indexed)
        } else {
            // Recursive step: Find the position for n - 1 people and adjust for current group
            return (josephus(n - 1, k) + k) % n;
        }
    }

    // Function to simulate the elimination sequence
    public static List<Integer> eliminationSequence(int n, int k) {
        List<Integer> people = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            people.add(i); // Populate the circle with 1-based positions
        }

        List<Integer> sequence = new ArrayList<>();
        int index = 0; // Starting point

        while (people.size() > 1) {
            index = (index + k - 1) % people.size(); // Calculate the k-th position to remove
            sequence.add(people.remove(index)); // Remove and store in the elimination sequence
        }

        // Add the last remaining person to the sequence
        sequence.add(people.get(0));
        return sequence;
    }

    public static void main(String[] args) {
        // Test Case 1: Basic input
        int n = 7; // Total number of people
        int k = 3; // Every k-th person is eliminated

        // Finding the survivor using the recursive method
        int survivor = josephus(n, k) + 1; // Convert to 1-based index
        System.out.println("The survivor is at position: " + survivor);

        // Finding and displaying the elimination sequence
        List<Integer> sequence = eliminationSequence(n, k);
        System.out.println("Elimination sequence: " + sequence);

        // Test Case 2: Edge case - Only one person
        n = 1; k = 1;
        survivor = josephus(n, k) + 1;
        System.out.println("With n=1, k=1, the survivor is: " + survivor);

        // Test Case 3: Edge case - Larger circle
        n = 10; k = 2;
        survivor = josephus(n, k) + 1;
        System.out.println("With n=10, k=2, the survivor is: " + survivor);

        // Test Case 4: Edge case - k > n
        n = 5; k = 8;
        survivor = josephus(n, k) + 1;
        System.out.println("With n=5, k=8, the survivor is: " + survivor);
    }
}
