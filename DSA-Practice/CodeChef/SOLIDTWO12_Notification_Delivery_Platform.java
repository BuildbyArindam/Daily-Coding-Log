/*
 * Problem    : Design A Notification Delivery Platform
 * Platform   : CodeChef (LLD > SOLID Principles II)
 * Link       : https://www.codechef.com/practice/course/lld/LLDSOLIDTWO/problems/SOLIDTWO12
 * Difficulty : Medium
 * Topics     : LLD, SOLID, OOP, Interfaces, Polymorphism
 * Date       : 2026-09-28
 *
 * Approach:
 *   NotificationSender is an interface with Email, SMS and Push implementations.
 *   NotificationService depends only on that abstraction (DIP), so adding a new
 *   channel means adding a class, not editing the service (OCP). Every sender
 *   is substitutable for the interface (LSP). NotificationHistory has one job,
 *   storing delivery records (SRP), and is injected into the service.
 *
 * Time Complexity  : O(1) per notification sent; O(n) to print history of n records
 * Space Complexity : O(n) for n stored history records
 */


// ----------------------------------------- Solution -------------------------------------------------


import java.util.*;

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
    public void processNotification(NotificationSender sender,
                                    String recipient,
                                    String message,
                                    String channel) {
        sender.send(recipient, message);
        String record = channel + " -> " + recipient;
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
