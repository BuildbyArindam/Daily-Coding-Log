/*
 * Problem: Design a Coupon Application System
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD1/problems/CNCDONE12
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topic: Low-Level Design (LLD) — Encapsulation, Single Responsibility Principle
 *
 * Approach:
 * Split responsibilities across three classes: Coupon (data holder),
 * CouponValidator (validation rules), and PricingService (orchestrates
 * validation + discount calculation). PricingService depends on
 * CouponValidator via constructor injection, keeping validation logic
 * decoupled and independently testable.
 *
 * Time Complexity: O(1) per applyCoupon call (fixed number of checks/arithmetic ops)
 * Space Complexity: O(1) additional space
 */


// ----------------------------- Solution ----------------------------------


import java.util.*;

// ================= COUPON =================
/*
Encapsulation:
- Store coupon details
- Provide getter methods
*/
class Coupon {

    // Private fields
    private String code;
    private double discountPercent;
    private double minimumAmount;

    // Constructor
    public Coupon(String code, double discountPercent, double minimumAmount) {
        this.code = code;
        this.discountPercent = discountPercent;
        this.minimumAmount = minimumAmount;
    }

    // Getters
    public String getCode() {
        return code;
    }

    public double getDiscountPercent() {
        return discountPercent;
    }

    public double getMinimumAmount() {
        return minimumAmount;
    }
}


// ================= COUPON VALIDATOR =================
/*
Responsibility:
- Validate coupon information
- Keep validation methods small and readable
*/
class CouponValidator {

    /*
    Validation Rules:
    - Code should not be null
    - Code should not be empty
    */
    public boolean validateCode(String code) {
        return code != null && !code.trim().isEmpty();
    }

    /*
    Validation Rules:
    - Discount percent should be greater than 0
    - Discount percent should be less than or equal to 100
    */
    public boolean validateDiscount(double discountPercent) {
        return discountPercent > 0 && discountPercent <= 100;
    }

    /*
    Validation Rules:
    - Minimum amount should not be negative
    */
    public boolean validateMinimumAmount(double minimumAmount) {
        return minimumAmount >= 0;
    }

    /*
    Validation Flow:
    1. Coupon should not be null
    2. Call all validation methods
    3. Return true only if all validations pass
    */
    public boolean isValid(Coupon coupon) {

        if (coupon == null) {
            return false;
        }

        return validateCode(coupon.getCode())
                && validateDiscount(coupon.getDiscountPercent())
                && validateMinimumAmount(coupon.getMinimumAmount());
    }
}


// ================= PRICING SERVICE =================
/*
Dependency + Flow:
- Applies coupon on cart amount
- Uses CouponValidator for validation

Flow:
User → PricingService → CouponValidator
*/
class PricingService {

    // Private CouponValidator reference
    private CouponValidator validator;

    // Constructor
    public PricingService(CouponValidator validator) {
        this.validator = validator;
    }

    /*
    Processing Flow:
    1. If cart amount <= 0
        → return original amount
    2. Validate coupon
    3. If invalid → return original amount
    4. Check minimum amount eligibility
    5. If not eligible → return original amount
    6. Otherwise apply discount
    */
    public double applyCoupon(double cartAmount, Coupon coupon) {

        if (cartAmount <= 0) {
            return cartAmount;
        }

        if (!validator.isValid(coupon)) {
            return cartAmount;
        }

        if (cartAmount < coupon.getMinimumAmount()) {
            return cartAmount;
        }

        return calculateDiscount(cartAmount, coupon.getDiscountPercent());
    }

    /*
    Helper Method:
    - Calculate final discounted amount
    */
    public double calculateDiscount(double cartAmount, double discountPercent) {

        double discountAmount = cartAmount * discountPercent / 100;

        return cartAmount - discountAmount;
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        CouponValidator validator = new CouponValidator();

        PricingService service = new PricingService(validator);

        Coupon c1 = new Coupon("SAVE10", 10, 500);

        Coupon c2 = new Coupon("", 20, 300);

        double result1 = service.applyCoupon(1000, c1);

        double result2 = service.applyCoupon(1000, c2);

        double result3 = service.applyCoupon(200, c1);

        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);
    }
}
