/*
 * Problem: Design a Car System
 * Link: https://www.codechef.com/practice/course/lld/LLDUML/problems/UMLLLD12
 * Platform: CodeChef
 * Date: 2026-09-12
 * Difficulty: Medium
 * Topics: Low Level Design, Composition, Encapsulation
 *
 * Approach:
 * Car "has-a" Engine (composition) — Engine is instantiated inside Car's
 * constructor rather than injected, so Engine's lifecycle is fully owned
 * and controlled by Car. Car exposes start()/stop() and delegates the
 * actual work to Engine, keeping engine internals encapsulated.
 *
 * Time Complexity: O(1) — fixed number of method calls, no loops/recursion
 * Space Complexity: O(1) — one Engine instance per Car, no extra data structures
 */


// -------------------------- Solution ---------------------------------


import java.util.*;

// ================= ENGINE =================
/*
Provides engine functionality
*/
class Engine {

    // Engine starts
    void start() {
        System.out.println("Engine started");
    }

    // Engine stops
    void stop() {
        System.out.println("Engine stopped");
    }
}


// ================= CAR =================
/*
Composition:
- Car owns Engine
- Engine should be created internally
- Car delegates work to Engine
*/
class Car {

    // Car has-a Engine (composition)
    private Engine engine;

    // Constructor creates Engine internally
    public Car() {
        engine = new Engine();
    }

    // Delegate start to Engine
    public void start() {
        engine.start();
    }

    // Delegate stop to Engine
    public void stop() {
        engine.stop();
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        Car car = new Car();

        car.start();
        car.stop();
    }
}
