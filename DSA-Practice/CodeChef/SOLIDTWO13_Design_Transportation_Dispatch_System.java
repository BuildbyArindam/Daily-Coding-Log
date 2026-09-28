/*
 * Platform    : CodeChef
 * Problem     : Design Transportation Dispatch System (SOLIDTWO13)
 * Link        : https://www.codechef.com/practice/course/lld/LLDSOLIDTWO/problems/SOLIDTWO13
 * Difficulty  : Medium
 * Topics      : LLD, SOLID, Polymorphism, Dependency Injection
 * Date        : 28-Sep-2026
 *
 * Approach:
 *   - TransportPartner is an interface; BikeRider, MiniTruckDriver and
 *     CargoVanDriver each implement transport(), so they are fully
 *     substitutable (Liskov Substitution / Open-Closed).
 *   - RoutePlanner has one job: generating a route (Single Responsibility).
 *   - DispatchService gets RoutePlanner via its constructor and works with
 *     any TransportPartner, so adding a new vehicle type needs no changes
 *     to existing code.
 *   - Flow: plan route -> print route -> partner.transport(destination).
 *
 * Time Complexity  : O(1) per dispatch
 * Space Complexity : O(1)
 */


// ------------------------------------ Solution ------------------------------------------------


import java.util.*;

// ================= TRANSPORT PARTNER =================
interface TransportPartner {
    void transport(String destination);
}

// ================= BIKE RIDER =================
class BikeRider implements TransportPartner {
    @Override
    public void transport(String destination) {
        System.out.println("Bike Rider dispatched to: " + destination);
    }
}

// ================= MINI TRUCK DRIVER =================
class MiniTruckDriver implements TransportPartner {
    @Override
    public void transport(String destination) {
        System.out.println("Mini Truck dispatched to: " + destination);
    }
}

// ================= CARGO VAN DRIVER =================
class CargoVanDriver implements TransportPartner {
    @Override
    public void transport(String destination) {
        System.out.println("Cargo Van dispatched to: " + destination);
    }
}

// ================= ROUTE PLANNER =================
class RoutePlanner {
    public String generateRoute(String destination) {
        return "Route planned for destination: " + destination;
    }
}

// ================= DISPATCH SERVICE =================
class DispatchService {
    private RoutePlanner routePlanner;
    public DispatchService(RoutePlanner routePlanner) {
        this.routePlanner = routePlanner;
    }
    public void processDispatch(TransportPartner partner, String destination) {
        String route = routePlanner.generateRoute(destination);
        System.out.println(route);
        partner.transport(destination);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        RoutePlanner routePlanner = new RoutePlanner();
        DispatchService service = new DispatchService(routePlanner);
        TransportPartner bikeRider = new BikeRider();
        TransportPartner miniTruck = new MiniTruckDriver();
        TransportPartner cargoVan = new CargoVanDriver();
        service.processDispatch(bikeRider, "MG Road");
        System.out.println();
        service.processDispatch(miniTruck, "Airport");
        System.out.println();
        service.processDispatch(cargoVan, "Electronic City");
    }
}
