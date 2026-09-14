/*
 * Problem: Design A Customer Loyalty Evaluation
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD3/problems/CNCDTH11
 * Date: 2026-09-15
 * Difficulty: Medium
 * Topic: Low-Level Design (LLD), OOP Design, SOLID (Single Responsibility)
 *
 * Approach:
 * Split responsibilities across two classes — Customer (data holder) and
 * LoyaltyService (business logic). LoyaltyService validates inputs, computes
 * a loyalty score from purchase amount and reward points, maps the score to
 * a membership tier and reward eligibility, then builds and prints a summary.
 * The public processLoyaltyEvaluation() method orchestrates the workflow by
 * delegating each step to a small, single-purpose helper method.
 *
 * Time Complexity: O(1) — fixed number of arithmetic/comparison operations
 * Space Complexity: O(1) — constant extra space (no data structures scale with input)
 */


// ----------------------------- Solution ----------------------------------


import java.util.*;

// ================= CUSTOMER =================
/*
Responsibilities:
- Store customer information
- Maintain customer details
*/
class Customer {

    /*
    Create encapsulated field for:
    - customer name using 'name'
    */
    private String name;

    /*
    Initialize customer details
    */
    public Customer(String name) {
        this.name = name;
    }

    /*
    Return customer name
    */
    public String getName() {
        return name;
    }
}


// ================= LOYALTY SERVICE =================
/*
Responsibilities:
- Process customer loyalty workflow
- Validate loyalty data
- Calculate loyalty score
- Generate final loyalty summary
*/
class LoyaltyService {

    /*
    Validate customer information

    Rules:
    - customer name cannot be null or empty

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validateCustomer(Customer customer) {

        if (customer == null) {
            throw new IllegalArgumentException("Customer cannot be null.");
        }

        if (customer.getName() == null || customer.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("Customer name cannot be null or empty.");
        }
    }

    /*
    Validate purchase amount

    Rules:
    - purchase amount must be greater than 0

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validatePurchaseAmount(double totalPurchaseAmount) {

        if (totalPurchaseAmount <= 0) {
            throw new IllegalArgumentException("Purchase amount must be greater than 0.");
        }
    }

    /*
    Validate reward points

    Rules:
    - reward points cannot be negative

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validateRewardPoints(int rewardPoints) {

        if (rewardPoints < 0) {
            throw new IllegalArgumentException("Reward points cannot be negative.");
        }
    }

    /*
    Calculate loyalty score

    Formula:
    - (totalPurchaseAmount / 100) + rewardPoints

    Return:
    - loyalty score
    */
    public double calculateLoyaltyScore(double totalPurchaseAmount, int rewardPoints) {

        return (totalPurchaseAmount / 100) + rewardPoints;
    }

    /*
    Determine membership category

    Return:
    - "PLATINUM" if loyalty score >= 90
    - "GOLD" if loyalty score >= 75
    - otherwise return "SILVER"
    */
    public String determineMembershipCategory(double loyaltyScore) {

        if (loyaltyScore >= 90) {
            return "PLATINUM";
        } else if (loyaltyScore >= 75) {
            return "GOLD";
        } else {
            return "SILVER";
        }
    }

    /*
    Determine reward eligibility

    Return:
    - "ELIGIBLE" if loyalty score >= 80
    - otherwise return "NOT_ELIGIBLE"
    */
    public String determineRewardEligibility(double loyaltyScore) {

        if (loyaltyScore >= 80) {
            return "ELIGIBLE";
        } else {
            return "NOT_ELIGIBLE";
        }
    }

    /*
    Generate formatted loyalty summary

    Use below format exactly:

    Customer: Rahul
    Loyalty Score: 130.0
    Membership Category: PLATINUM
    Reward Eligibility: ELIGIBLE

    Return:
    - formatted summary string
    */
    public String generateSummary(
            Customer customer,
            double loyaltyScore,
            String category,
            String eligibility) {

        return "Customer: " + customer.getName() + "\n"
                + "Loyalty Score: " + loyaltyScore + "\n"
                + "Membership Category: " + category + "\n"
                + "Reward Eligibility: " + eligibility;
    }

    /*
    Print final formatted loyalty summary
    */
    public void printSummary(String summary) {

        System.out.println(summary);
    }

    /*
    Execute complete loyalty evaluation workflow

    Expected Flow:
    1. validate customer
    2. validate purchase amount
    3. validate reward points
    4. calculate loyalty score
    5. determine membership category
    6. determine reward eligibility
    7. generate summary
    8. print summary

    Important:
    - keep this method small and readable
    - delegate work to helper methods
    */
    public void processLoyaltyEvaluation(
            Customer customer,
            double totalPurchaseAmount,
            int rewardPoints) {

        validateCustomer(customer);
        validatePurchaseAmount(totalPurchaseAmount);
        validateRewardPoints(rewardPoints);

        double loyaltyScore =
                calculateLoyaltyScore(totalPurchaseAmount, rewardPoints);

        String category =
                determineMembershipCategory(loyaltyScore);

        String eligibility =
                determineRewardEligibility(loyaltyScore);

        String summary =
                generateSummary(customer, loyaltyScore, category, eligibility);

        printSummary(summary);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        Customer customer = new Customer("Rahul");

        LoyaltyService service = new LoyaltyService();

        service.processLoyaltyEvaluation(customer, 8000, 50);
    }
}
