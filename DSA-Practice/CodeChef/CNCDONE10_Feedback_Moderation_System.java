/**
 * Problem   : Feedback Moderation & Flagging System
 * Platform  : CodeChef
 * Link      : https://www.codechef.com/practice/course/lld/LLDCLEANCD1/problems/CNCDONE10
 * Date      : 2026-09-12
 * Difficulty: Medium
 * Topics    : Low-Level Design (LLD), Object-Oriented Design, SOLID - Single Responsibility Principle
 *
 * Approach:
 * - User: simple immutable-style data holder for a submitter's name.
 * - Feedback: holds message, rating, and the associated User.
 * - FeedbackValidator: isolates all validation rules (name, message content/length,
 *   rating > 0) behind small single-purpose methods, combined in isValid().
 * - FeedbackService: orchestrates validation then applies business rules
 *   (rating < 3 -> Flagged, else -> Approved) to decide feedback status.
 * - Demonstrates separation of concerns: validation logic is decoupled from
 *   the service/decision logic, making each class independently testable.
 *
 * Time Complexity : O(m) per submitFeedback call, where m = length of feedback message
 *                    (dominated by the three regex scans in validateMessage).
 * Space Complexity: O(1) extra space (excluding input storage).
 */


// ----------------------------------- Solution -----------------------------------


import java.util.*;

// ================= USER =================
/*
Encapsulation:
- Store user name
- Provide getter
*/
class User {

    // Private field
    private String name;

    // Constructor
    public User(String name) {
        this.name = name;
    }

    // Getter
    public String getName() {
        return name;
    }
}


// ================= FEEDBACK =================
/*
Encapsulation:
- Store message, rating, and user
*/
class Feedback {

    // Private fields
    private String message;
    private int rating;
    private User user;

    // Constructor
    public Feedback(String message, int rating, User user) {
        this.message = message;
        this.rating = rating;
        this.user = user;
    }

    // Getters
    public String getMessage() {
        return message;
    }

    public int getRating() {
        return rating;
    }

    public User getUser() {
        return user;
    }
}


// ================= VALIDATOR =================
/*
Responsibility:
- Validate feedback data
- Each method handles ONE rule
*/
class FeedbackValidator {

    // Check user + name not null/empty
    public boolean validateName(User user) {

        if (user == null) {
            return false;
        }

        String name = user.getName();

        return name != null && !name.trim().isEmpty();
    }

    // Check:
    // - not null
    // - length >= 10
    // - no words: spam, fake, scam
    public boolean validateMessage(String message) {

        if (message == null) {
            return false;
        }

        if (message.length() < 10) {
            return false;
        }

        String lowerMessage = message.toLowerCase();

        if (lowerMessage.matches(".*\\bspam\\b.*")) {
            return false;
        }

        if (lowerMessage.matches(".*\\bfake\\b.*")) {
            return false;
        }

        if (lowerMessage.matches(".*\\bscam\\b.*")) {
            return false;
        }

        return true;
    }

    // Rating must be > 0
    public boolean validateRating(int rating) {
        return rating > 0;
    }

    // Combine all validations
    // Also handle null feedback here
    public boolean isValid(Feedback feedback) {

        if (feedback == null) {
            return false;
        }

        return validateName(feedback.getUser())
                && validateMessage(feedback.getMessage())
                && validateRating(feedback.getRating());
    }
}


// ================= SERVICE =================
/*
Flow:
User → FeedbackService → FeedbackValidator
*/
class FeedbackService {

    // Private validator
    private FeedbackValidator validator;

    // Constructor
    public FeedbackService(FeedbackValidator validator) {
        this.validator = validator;
    }

    public String submitFeedback(Feedback feedback) {

        // 1. Validation
        if (!validator.isValid(feedback)) {
            return "Rejected";
        }

        // 2. Rating-based decision
        if (feedback.getRating() < 3) {
            return "Flagged";
        }

        // 3. Valid feedback with rating >= 3
        return "Approved";
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        FeedbackValidator validator = new FeedbackValidator();
        FeedbackService service = new FeedbackService(validator);

        User u1 = new User("John");
        Feedback f1 = new Feedback(
                "This product is amazing and useful",
                5,
                u1
        );

        User u2 = new User("John");
        Feedback f2 = new Feedback(
                "Very bad service overall",
                2,
                u2
        );

        User u3 = new User("");
        Feedback f3 = new Feedback(
                "spam content here",
                4,
                u3
        );

        System.out.println(service.submitFeedback(f1));
        System.out.println(service.submitFeedback(f2));
        System.out.println(service.submitFeedback(f3));
    }
}
