/*
 * Platform   : CodeChef
 * Problem    : Design Smart Restaurant Management System
 * Link       : https://www.codechef.com/practice/course/lld/LLDSOLIDTWO/problems/SOLIDTWO11
 * Difficulty : Medium
 * Topics     : LLD, OOP, SOLID (Interface Segregation), Dependency Inversion
 * Date       : 28-Sep-2026
 *
 * Approach:
 *   Split the restaurant roles into small, focused interfaces (Chef, Waiter,
 *   Cashier, OrderTaker) so no class is forced to implement methods it doesn't
 *   use (ISP). RestaurantWaiter implements both Waiter and OrderTaker since
 *   it does both jobs. RestaurantService depends only on these abstractions
 *   (DIP) and runs the workflow: take order -> prepare -> serve -> pay.
 *
 * Time Complexity  : O(1) per workflow run
 * Space Complexity : O(1)
 */


// ------------------------------------- Solution -------------------------------------------


import java.util.*;

// ================= CHEF =================
interface Chef {
    void prepareFood(String itemName);
}

// ================= WAITER =================
interface Waiter {
    void serveFood(String itemName);
}

// ================= CASHIER =================
interface Cashier {
    void processPayment(double amount);
}

// ================= ORDER TAKER =================
interface OrderTaker {
    void takeOrder(String itemName);
}

// ================= RESTAURANT CHEF =================
class RestaurantChef implements Chef {
    @Override
    public void prepareFood(String itemName) {
        System.out.println("Chef prepared: " + itemName);
    }
}

// ================= RESTAURANT WAITER =================
class RestaurantWaiter implements Waiter, OrderTaker {
    @Override
    public void takeOrder(String itemName) {
        System.out.println("Order taken: " + itemName);
    }
    @Override
    public void serveFood(String itemName) {
        System.out.println("Waiter served: " + itemName);
    }
}

// ================= RESTAURANT CASHIER =================
class RestaurantCashier implements Cashier {
    @Override
    public void processPayment(double amount) {
        System.out.println("Payment processed: " + amount);
    }
}

// ================= RESTAURANT SERVICE =================
class RestaurantService {
    public void processRestaurantWorkflow(OrderTaker orderTaker,
                                          Chef chef,
                                          Waiter waiter,
                                          Cashier cashier,
                                          String itemName,
                                          double amount) {
        orderTaker.takeOrder(itemName);
        chef.prepareFood(itemName);
        waiter.serveFood(itemName);
        cashier.processPayment(amount);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        OrderTaker orderTaker = new RestaurantWaiter();
        Chef chef = new RestaurantChef();
        Waiter waiter = new RestaurantWaiter();
        Cashier cashier = new RestaurantCashier();
        RestaurantService service = new RestaurantService();
        service.processRestaurantWorkflow(
            orderTaker,
            chef,
            waiter,
            cashier,
            "Pizza",
            450
        );
    }
}
