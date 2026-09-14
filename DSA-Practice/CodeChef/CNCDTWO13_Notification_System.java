/**
 * Problem: Design a Notification System
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD2/problems/CNCDTWO13
 * Date: 2026-09-14
 * Difficulty: Medium
 * Topics: Low-Level Design, OOP - Polymorphism, Strategy Pattern
 *
 * Approach:
 * - Defined a common `Notification` interface with a single send(String) contract.
 * - EmailNotification, SMSNotification, and PushNotification each implement
 *   Notification independently, encapsulating their own send behavior.
 * - Client code (main) depends only on the Notification abstraction and
 *   iterates over a List<Notification>, so new channels can be added later
 *   without touching existing classes (Open/Closed Principle).
 *
 * Time Complexity: O(n) — n = number of notifications sent, each send() is O(1)
 * Space Complexity: O(n) — for storing n Notification objects in the list
 */


// --------------------------------- Solution -----------------------------------------


import java.util.*;

// ================= NOTIFICATION =================
/*
Abstraction:
- Define a common contract for all notification types
*/
interface Notification {

    // Send a message
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
