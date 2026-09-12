/**
 * Problem     : Design a Notification System
 * Platform    : CodeChef
 * Link        : https://www.codechef.com/practice/course/lld/LLDUML/problems/UMLLLD13?folder=%2Fhome%2Fchef%2Fworkspace
 * Difficulty  : Medium
 * Topics      : Low Level Design (LLD), Object-Oriented Design (OOD), Design Patterns → Strategy Pattern, SOLID Principles (Open/Closed, Interface Segregation)
 * Date Solved : 2026-09-12
 *
 * Approach:
 * Defined a common `Notification` interface with a single `send(String message)`
 * contract. EmailNotification, SMSNotification, and PushNotification each provide
 * their own concrete implementation (polymorphism over conditionals). The client
 * (main) holds a List<Notification> and invokes send() uniformly without knowing
 * the concrete type — this is effectively the Strategy pattern applied to
 * notification channels, and keeps the design open for extension (e.g. adding
 * WhatsAppNotification later needs no change to existing classes -> Open/Closed
 * Principle).
 *
 * Time Complexity  : O(n) — n = number of notifications sent, each send() is O(1)
 * Space Complexity : O(n) — for storing n Notification objects in the list
 */


// ------------------------------- Solution -------------------------------------


import java.util.*;

// ================= NOTIFICATION =================
/*
Abstraction:
- Define a common contract for all notification types
*/
interface Notification {

    void send(String message);
}


// ================= EMAIL NOTIFICATION =================
/*
Implements Notification:
- Should send message as Email
- The send() method should print a message (e.g., "Email: <message>")
*/
class EmailNotification implements Notification {

    @Override
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}


// ================= SMS NOTIFICATION =================
/*
Implements Notification:
- Should send message as SMS
- The send() method should print a message (e.g., "SMS: <message>")
*/
class SMSNotification implements Notification {

    @Override
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}


// ================= PUSH NOTIFICATION =================
/*
Implements Notification:
- Should send message as Push Notification
- The send() method should print a message (e.g., "Push: <message>")
*/
class PushNotification implements Notification {

    @Override
    public void send(String message) {
        System.out.println("Push: " + message);
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        List<Notification> notifications = new ArrayList<>();

        notifications.add(new EmailNotification());
        notifications.add(new SMSNotification());
        notifications.add(new PushNotification());

        for (Notification n : notifications) {
            n.send("Hello");
        }
    }
}
