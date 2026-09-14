/**
 * Problem   : Design Stock Reordering System
 * Platform  : CodeChef
 * Link      : https://www.codechef.com/practice/course/lld/LLDCLEANCD3/problems/CNCDTH10
 * Date      : 2026-09-15
 * Difficulty: Medium
 * Topics    : Low-Level Design, Object-Oriented Design, SOLID Principles
 *
 * Approach:
 * - Separated concerns into two classes: Product (data holder) and
 *   InventoryService (business logic — validation, cost calculation,
 *   stock update, status determination, summary generation).
 * - processRestock() orchestrates the workflow by delegating each step
 *   to a small, single-purpose helper method (validate -> calculate ->
 *   update -> summarize -> print), keeping it readable and testable.
 *
 * Complexity:
 * - Time  : O(1) — fixed number of validation/arithmetic operations per restock call
 * - Space : O(1) — no auxiliary data structures used
 */


// ------------------------------- Solution -------------------------------------


import java.util.*;

// ================= PRODUCT =================
/*
Responsibilities:
- Store product information
- Maintain inventory stock
*/
class Product {

    /*
    TODO:
    Create encapsulated fields for:
    - product name using 'name'
    - current stock using 'currentStock'
    */
    private String name;
    private int currentStock;


    /*
    TODO:
    Initialize product details
    */
    public Product(String name, int currentStock) {
        this.name = name;
        this.currentStock = currentStock;
    }

    /*
    TODO:
    Return product name
    */
    public String getName() {
        return name;
    }

    /*
    TODO:
    Return current stock
    */
    public int getCurrentStock() {
        return currentStock;
    }

    /*
    TODO:
    Update current stock
    */
    public void setCurrentStock(int currentStock) {
        this.currentStock = currentStock;
    }
}


// ================= INVENTORY SERVICE =================
/*
Responsibilities:
- Process inventory restock workflow
- Validate inventory data
- Calculate restock expenses
- Update inventory stock
- Generate final summary
*/
class InventoryService {

    /*
    TODO:
    Validate product information

    Rules:
    - product name cannot be null or empty
    - current stock cannot be negative

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validateProduct(Product product) {

        if (product == null) {
            throw new IllegalArgumentException("Product cannot be null.");
        }

        if (product.getName() == null || product.getName().isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty.");
        }

        if (product.getCurrentStock() < 0) {
            throw new IllegalArgumentException("Current stock cannot be negative.");
        }
    }

    /*
    TODO:
    Validate restock quantity

    Rules:
    - quantity must be greater than 0

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validateRestockQuantity(int quantity) {

        if (quantity <= 0) {
            throw new IllegalArgumentException(
                "Restock quantity must be greater than 0."
            );
        }
    }

    /*
    TODO:
    Validate pricing information

    Rules:
    - price per unit must be greater than 0

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validatePricePerUnit(double pricePerUnit) {

        if (pricePerUnit <= 0) {
            throw new IllegalArgumentException(
                "Price per unit must be greater than 0."
            );
        }
    }

    /*
    TODO:
    Verify supplier availability

    Rules:
    - supplier must be available

    If validation fails:
    - throw IllegalArgumentException
    */
    public void checkSupplierAvailability(boolean supplierAvailable) {

        if (!supplierAvailable) {
            throw new IllegalArgumentException(
                "Supplier is not available."
            );
        }
    }

    /*
    TODO:
    Calculate final restock expense

    Formula:
    - quantity * pricePerUnit

    Return:
    - total restock expense
    */
    public double calculateRestockCost(int quantity, double pricePerUnit) {
        return quantity * pricePerUnit;
    }

    /*
    TODO:
    Update inventory stock after restocking

    Steps:
    - add restock quantity to current stock
    - update product stock

    Return:
    - updated stock quantity
    */
    public int updateStock(Product product, int restockQuantity) {

        int updatedStock = product.getCurrentStock() + restockQuantity;

        product.setCurrentStock(updatedStock);

        return updatedStock;
    }

    /*
    TODO:
    Determine inventory status

    Return:
    - "STABLE" for healthy inventory
    - "LOW_STOCK" for low inventory
    */
    public String determineInventoryStatus(int updatedStock) {

        if (updatedStock >= 50) {
            return "STABLE";
        }

        return "LOW_STOCK";
    }

    /*
    TODO:
    Generate formatted inventory summary

    Use below format exactly:

    Product: Keyboard
    Updated Stock: 60
    Inventory Status: STABLE
    Total Restock Cost: 20000.0

    Return:
    - formatted summary string
    */
    public String generateSummary(
            Product product,
            int updatedStock,
            double totalCost,
            String status) {

        return "Product: " + product.getName() + "\n"
             + "Updated Stock: " + updatedStock + "\n"
             + "Inventory Status: " + status + "\n"
             + "Total Restock Cost: " + totalCost;
    }

    /*
    TODO:
    Print final formatted inventory summary
    */
    public void printSummary(String summary) {

        System.out.println(summary);
    }

    /*
    TODO:
    Execute complete inventory restock workflow

    Expected Flow:
    1. validate product
    2. validate restock quantity
    3. validate pricing information
    4. check supplier availability
    5. calculate restock expense
    6. update stock
    7. determine inventory status
    8. generate summary
    9. print summary

    Important:
    - keep this method small and readable
    - delegate work to helper methods
    */
    public void processRestock(
            Product product,
            int restockQuantity,
            double pricePerUnit,
            boolean supplierAvailable) {

        validateProduct(product);
        validateRestockQuantity(restockQuantity);
        validatePricePerUnit(pricePerUnit);
        checkSupplierAvailability(supplierAvailable);

        double totalCost =
            calculateRestockCost(restockQuantity, pricePerUnit);

        int updatedStock =
            updateStock(product, restockQuantity);

        String status =
            determineInventoryStatus(updatedStock);

        String summary =
            generateSummary(product, updatedStock, totalCost, status);

        printSummary(summary);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        Product product = new Product("Keyboard", 20);

        InventoryService service = new InventoryService();

        service.processRestock(product, 40, 500, true);
    }
}
