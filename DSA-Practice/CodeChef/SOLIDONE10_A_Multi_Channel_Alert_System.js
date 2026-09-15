/**
 * Problem   : Design A Multi Channel Alert System
 * Platform  : CodeChef
 * Link      : https://www.codechef.com/practice/course/lld/LLDSOLIDONE/problems/SOLIDONE10
 * Date      : 2026-09-15
 * Difficulty: Medium
 * Topics    : LLD, SOLID Principles (SRP, OCP), Strategy Pattern
 *
 * Approach:
 * - Defined a NotificationSender interface as a common strategy contract.
 * - EmailNotification, SMSNotification, and PushNotification each implement
 *   their own send() logic, so new channels can be added without touching
 *   existing code (Open/Closed Principle).
 * - NotificationService depends only on the NotificationSender abstraction
 *   and delegates the actual sending via polymorphism, then logs a record
 *   to NotificationHistory (kept as a separate class per SRP).
 *
 * Complexity:
 * - Time  : O(1) per processNotification() call (send + log are constant time);
 *           O(n) to print full history, where n = number of records.
 * - Space : O(n) to store n history records.
 */


// -------------------------- Solution ------------------------------------------


import java.util.*;

// ================= NOTIFICATION SENDER =================

interface NotificationSender {

    void send(String recipient, String message);
}


// ================= EMAIL NOTIFICATION =================

class EmailNotification implements NotificationSender {

    @Override
    public void send(String recipient, String message) {
        System.out.println("EMAIL sent to " + recipient + ": " + message);
    }
}


// ================= SMS NOTIFICATION =================

class SMSNotification implements NotificationSender {

    @Override
    public void send(String recipient, String message) {
        System.out.println("SMS sent to " + recipient + ": " + message);
    }
}


// ================= PUSH NOTIFICATION =================

class PushNotification implements NotificationSender {

    @Override
    public void send(String recipient, String message) {
        System.out.println("PUSH sent to " + recipient + ": " + message);
    }
}


// ================= NOTIFICATION HISTORY =================

class NotificationHistory {

    private List<String> records;

    public NotificationHistory() {
        records = new ArrayList<>();
    }

    public void addRecord(String record) {
        records.add(record);
    }

    public void printHistory() {
        System.out.println("=== Notification History ===");

        for (String record : records) {
            System.out.println(record);
        }
    }
}


// ================= NOTIFICATION SERVICE =================

class NotificationService {

    private NotificationHistory history;

    public NotificationService(NotificationHistory history) {
        this.history = history;
    }
    public void processNotification(
            NotificationSender sender,
            String recipient,
            String message,
            String channel) {

        // 1. Send notification using polymorphism
        sender.send(recipient, message);

        // 2. Create history record
        String record = channel + " -> " + recipient;

        // 3. Store history record
        history.addRecord(record);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        NotificationHistory history = new NotificationHistory();

        NotificationService service = new NotificationService(history);

        NotificationSender email = new EmailNotification();

        NotificationSender sms = new SMSNotification();

        NotificationSender push = new PushNotification();

        service.processNotification(
                email,
                "codechef@gmail.com",
                "Order Placed",
                "EMAIL"
        );

        service.processNotification(
                sms,
                "9876543210",
                "OTP Generated",
                "SMS"
        );

        service.processNotification(
                push,
                "DEVICE_101",
                "Payment Successful",
                "PUSH"
        );

        System.out.println();

        history.printHistory();
    }
}
