/**
 * Problem: Design Logistics Fleet Management System
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDSOLIDONE/problems/SOLIDONE11
 * Date: 2026-09-21
 * Difficulty: Medium
 * Topics: Strategy Pattern, SOLID Principles, Polymorphism / Abstraction via Interfaces, Object-Oriented Design (OOD)
 *
 * Approach:
 * Defined a common DeliveryPartner interface with a deliver() method, then implemented
 * it separately for Bike, Truck, and Drone partners. A DeliveryService class depends only
 * on the DeliveryPartner abstraction and delegates the delivery call to whichever
 * implementation is passed in — this follows the Strategy pattern and keeps the design
 * open for extension (new partner types) without modifying existing code (Open/Closed
 * Principle).
 *
 * Time Complexity: O(1) per delivery call
 * Space Complexity: O(1) (excluding partner objects, which are O(1) each)
 */


// ---------------------------------------- Solution -------------------------------------


import java.util.*;

// ================= DELIVERY PARTNER =================

interface DeliveryPartner {

    void deliver(String packageName);
}

// ================= BIKE PARTNER =================

class BikePartner implements DeliveryPartner {
    @Override
    public void deliver(String packageName) {
        System.out.println("Bike Partner delivered package: " + packageName);
    }
}

// ================= TRUCK PARTNER =================

class TruckPartner implements DeliveryPartner {
    @Override
    public void deliver(String packageName) {
        System.out.println("Truck Partner delivered package: " + packageName);
    }
}

// ================= DRONE PARTNER =================

class DronePartner implements DeliveryPartner {
    @Override
    public void deliver(String packageName) {
        System.out.println("Drone Partner delivered package: " + packageName);
    }
}

// ================= DELIVERY SERVICE =================

class DeliveryService {
    public void processDelivery(DeliveryPartner partner, String packageName) {
        partner.deliver(packageName);
    }
}

public class Codechef {

    public static void main(String[] args) {

        DeliveryService service = new DeliveryService();

        DeliveryPartner bike = new BikePartner();

        DeliveryPartner truck = new TruckPartner();

        DeliveryPartner drone = new DronePartner();

        service.processDelivery(bike, "Mobile Phone");

        service.processDelivery(truck, "Washing Machine");

        service.processDelivery(drone, "Medicine Box");
    }
}
