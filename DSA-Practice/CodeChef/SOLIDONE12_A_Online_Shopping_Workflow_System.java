/**
 * Problem   : Design A Online Shopping Workflow System
 * Platform  : CodeChef (LLD/SOLID Practice Course)
 * Link      : https://www.codechef.com/practice/course/lld/LLDSOLIDONE/problems/SOLIDONE12
 * Date      : 2026-09-21
 * Difficulty: Medium
 * Topics    : Low-Level Design, SOLID Principles (SRP, OCP, DIP), Strategy Pattern, Dependency Injection
 *
 * Approach:
 * Modeled the order workflow using interface-based strategies so each concern
 * (payment, notification, delivery) can vary independently without modifying
 * OrderService — satisfies Open/Closed and Dependency Inversion.
 *   - PaymentMethod, NotificationSender, DeliveryPartner: interfaces, each with
 *     one or more concrete strategies (CreditCard/UPI, Email/SMS, Bike).
 *   - InvoiceGenerator: single-responsibility class for invoice text.
 *   - OrderService: orchestrates the workflow by depending only on the
 *     interfaces, injected at call time (constructor/method injection).
 *
 * Time Complexity  : O(1) — fixed sequence of operations per order (no loops/recursion)
 * Space Complexity : O(1) — constant extra space per order processed
 */


// ------------------------------------ Solution ------------------------------------------


import java.util.*;

// ================= ORDER =================
class Order {
    private String orderId;
    private String productName;
    private double amount;
    public Order(String orderId, String productName, double amount) {
        this.orderId = orderId;
        this.productName = productName;
        this.amount = amount;
    }
    public String getOrderId() {
        return orderId;
    }
    public String getProductName() {
        return productName;
    }
    public double getAmount() {
        return amount;
    }
}

// ================= PAYMENT METHOD =================
interface PaymentMethod {
    void pay(double amount);
}

// ================= CREDIT CARD PAYMENT =================
class CreditCardPayment implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("Credit Card payment processed: " + amount);
    }
}

// ================= UPI PAYMENT =================
class UpiPayment implements PaymentMethod {
    @Override
    public void pay(double amount) {
        System.out.println("UPI payment processed: " + amount);
    }
}

// ================= NOTIFICATION SENDER =================
interface NotificationSender {
    void send(String message);
}

// ================= EMAIL NOTIFICATION =================
class EmailNotification implements NotificationSender {
    @Override
    public void send(String message) {
        System.out.println("EMAIL: " + message);
    }
}

// ================= SMS NOTIFICATION =================
class SMSNotification implements NotificationSender {
    @Override
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}

// ================= DELIVERY PARTNER =================
interface DeliveryPartner {
    void deliver(String productName);
}

// ================= BIKE DELIVERY PARTNER =================
class BikeDeliveryPartner implements DeliveryPartner {
    @Override
    public void deliver(String productName) {
        System.out.println("Bike Delivery assigned for: " + productName);
    }
}

// ================= INVOICE GENERATOR =================
class InvoiceGenerator {
    public String generateInvoice(Order order) {
        return "Order ID: " + order.getOrderId()
                + "\nProduct: " + order.getProductName()
                + "\nAmount: " + order.getAmount();
    }
}

// ================= ORDER SERVICE =================
class OrderService {
    private InvoiceGenerator invoiceGenerator;
    public OrderService(InvoiceGenerator invoiceGenerator) {
        this.invoiceGenerator = invoiceGenerator;
    }
    public void processOrder(Order order,
                             PaymentMethod paymentMethod,
                             NotificationSender notificationSender,
                             DeliveryPartner deliveryPartner) {
        paymentMethod.pay(order.getAmount());
        notificationSender.send("Order placed successfully");
        deliveryPartner.deliver(order.getProductName());
        String invoice = invoiceGenerator.generateInvoice(order);
        System.out.println();
        System.out.println(invoice);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        Order order = new Order("ORD101", "Laptop", 50000);
        PaymentMethod paymentMethod = new CreditCardPayment();
        NotificationSender notificationSender = new EmailNotification();
        DeliveryPartner deliveryPartner = new BikeDeliveryPartner();
        InvoiceGenerator invoiceGenerator = new InvoiceGenerator();
        OrderService service = new OrderService(invoiceGenerator);
        service.processOrder(order, paymentMethod, notificationSender, deliveryPartner);
    }
}
