/*
 * Problem    : Design Smart Warehouse Fulfillment System
 * Platform   : CodeChef (LLD Design course)
 * Link       : https://www.codechef.com/practice/course/lld/LLDDESIGN/problems/DESIGNPR10
 * Difficulty : Hard
 * Topics     : LLD, Design Patterns (Builder, Strategy, State, Facade)
 * Date       : 28-Sep-2026
 *
 * Approach:
 *   Low-level design combining four patterns:
 *   - Builder  : PackageBuilder constructs an immutable WarehousePackage step by step.
 *   - Strategy : PackagingStrategy (Standard / Fragile) selects the packing behavior at runtime.
 *   - State    : ShipmentState (Prepared -> Shipped -> Delivered) models the shipment lifecycle.
 *   - Facade   : WarehouseFacade hides the packing + fulfillment workflow behind one
 *                processPackage() call.
 *
 * Time Complexity  : O(1) per package (fixed number of steps: pack + 3 state transitions)
 * Space Complexity : O(1) (no collections; only the package object and small state objects)
 */


// ---------------------------------- Solution -------------------------------------------------


import java.util.*;

// ================= WAREHOUSE PACKAGE =================
class WarehousePackage {
    private String packageId;
    private String itemName;
    private double weight;
    public WarehousePackage(String packageId, String itemName, double weight) {
        this.packageId = packageId;
        this.itemName = itemName;
        this.weight = weight;
    }
    public String getPackageId() {
        return packageId;
    }
    public String getItemName() {
        return itemName;
    }
    public double getWeight() {
        return weight;
    }
}

// ================= PACKAGE BUILDER =================
class PackageBuilder {
    private String packageId;
    private String itemName;
    private double weight;
    public PackageBuilder setPackageId(String packageId) {
        this.packageId = packageId;
        return this;
    }
    public PackageBuilder setItemName(String itemName) {
        this.itemName = itemName;
        return this;
    }
    public PackageBuilder setWeight(double weight) {
        this.weight = weight;
        return this;
    }
    public WarehousePackage build() {
        return new WarehousePackage(packageId, itemName, weight);
    }
}

// ================= PACKAGING STRATEGY =================
interface PackagingStrategy {
    void pack(WarehousePackage warehousePackage);
}

// ================= STANDARD PACKAGING =================
class StandardPackaging implements PackagingStrategy {
    @Override
    public void pack(WarehousePackage warehousePackage) {
        System.out.println(
                "Standard packaging applied for: "
                        + warehousePackage.getItemName()
        );
    }
}

// ================= FRAGILE PACKAGING =================
class FragilePackaging implements PackagingStrategy {
    @Override
    public void pack(WarehousePackage warehousePackage) {
        System.out.println(
                "Fragile packaging applied for: "
                        + warehousePackage.getItemName()
        );
    }
}

// ================= SHIPMENT STATE =================
interface ShipmentState {
    void handle(WarehousePackage warehousePackage);
}

// ================= PREPARED STATE =================
class PreparedState implements ShipmentState {
    @Override
    public void handle(WarehousePackage warehousePackage) {
        System.out.println(
                "Shipment Prepared: "
                        + warehousePackage.getPackageId()
        );
    }
}

// ================= SHIPPED STATE =================
class ShippedState implements ShipmentState {
    @Override
    public void handle(WarehousePackage warehousePackage) {
        System.out.println(
                "Shipment Shipped: "
                        + warehousePackage.getPackageId()
        );
    }
}

// ================= DELIVERED STATE =================
class DeliveredState implements ShipmentState {
    @Override
    public void handle(WarehousePackage warehousePackage) {
        System.out.println(
                "Shipment Delivered: "
                        + warehousePackage.getPackageId()
        );
    }
}

// ================= FULFILLMENT SERVICE =================
class FulfillmentService {
    public void fulfill(WarehousePackage warehousePackage,
                        ShipmentState shipmentState) {

        shipmentState.handle(warehousePackage);
    }
}

// ================= WAREHOUSE FACADE =================
class WarehouseFacade {
    private FulfillmentService fulfillmentService;
    public WarehouseFacade(FulfillmentService fulfillmentService) {
        this.fulfillmentService = fulfillmentService;
    }
    public void processPackage(WarehousePackage warehousePackage,
                               PackagingStrategy packagingStrategy) {
        packagingStrategy.pack(warehousePackage);
        fulfillmentService.fulfill(
                warehousePackage,
                new PreparedState()
        );
        fulfillmentService.fulfill(
                warehousePackage,
                new ShippedState()
        );
        fulfillmentService.fulfill(
                warehousePackage,
                new DeliveredState()
        );
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        WarehousePackage warehousePackage =
                new PackageBuilder()
                        .setPackageId("PKG101")
                        .setItemName("Laptop")
                        .setWeight(2.5)
                        .build();
        PackagingStrategy packagingStrategy = new FragilePackaging();
        FulfillmentService fulfillmentService = new FulfillmentService();
        WarehouseFacade warehouseFacade = new WarehouseFacade(fulfillmentService);
        warehouseFacade.processPackage(warehousePackage, packagingStrategy);
    }
}
