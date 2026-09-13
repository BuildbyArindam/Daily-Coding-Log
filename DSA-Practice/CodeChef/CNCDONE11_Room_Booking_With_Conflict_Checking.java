/**
 * Problem: Room Booking with Conflict Checking
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD1/problems/CNCDONE11
 * Difficulty: Medium
 * Topic: Low-Level Design (LLD) — Object-Oriented Design, SOLID Principles (SRP),
 *        Interval Scheduling / Overlap Detection
 * Date: 2026-09-13
 *
 * Approach:
 * - Modeled Room and Booking as plain data-holding entities (encapsulated, immutable fields).
 * - Separated validation logic into a dedicated BookingValidator (Single Responsibility).
 * - BookingService owns the booking list and conflict-detection logic:
 *   for a new booking, checks same-room bookings for interval overlap
 *   using the classic (start1 < end2 && start2 < end1) condition.
 * - Booking is confirmed only if it passes validation AND has no time conflict.
 *
 * Time Complexity: O(n) per booking check, where n = existing bookings
 *                   (linear scan for conflicts). O(n^2) overall for n bookings.
 * Space Complexity: O(n) to store all bookings.
 *
 * Possible optimization: group bookings by roomId in a Map<String, List<Booking>>
 * or a per-room interval tree to reduce conflict-check time from O(n) to O(log n) or O(k)
 * where k = bookings for that specific room.
 */


// ------------------------------- Solution ----------------------------------


import java.util.*;

// ================= ROOM =================
/*
Encapsulation:
- Store room id
- Provide getter method
*/
class Room {

    private final String roomId;

    // Constructor
    public Room(String roomId) {
        this.roomId = roomId;
    }

    // Getter
    public String getRoomId() {
        return roomId;
    }
}


// ================= BOOKING =================
/*
Encapsulation:
- Store room, start time, and end time
- Provide getter methods
*/
class Booking {

    private final Room room;
    private final int startTime;
    private final int endTime;

    // Constructor
    public Booking(Room room, int startTime, int endTime) {
        this.room = room;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    // Getters
    public Room getRoom() {
        return room;
    }

    public int getStartTime() {
        return startTime;
    }

    public int getEndTime() {
        return endTime;
    }
}


// ================= BOOKING VALIDATOR =================
/*
Responsibility:
- Validate booking details

Validation Rules:
1. Room should not be null
2. roomId should not be null or empty
3. startTime should be >= 0
4. endTime should be greater than startTime

Methods:
- validateRoom(room)
- validateTime(startTime, endTime)
- isValid(booking)
*/
class BookingValidator {

    // Validate room
    public boolean validateRoom(Room room) {

        if (room == null) {
            return false;
        }

        String roomId = room.getRoomId();

        return roomId != null && !roomId.trim().isEmpty();
    }

    // Validate time
    public boolean validateTime(int startTime, int endTime) {

        return startTime >= 0 && endTime > startTime;
    }

    // Validate complete booking
    public boolean isValid(Booking booking) {

        if (booking == null) {
            return false;
        }

        return validateRoom(booking.getRoom())
                && validateTime(
                    booking.getStartTime(),
                    booking.getEndTime()
                );
    }
}


// ================= BOOKING SERVICE =================
/*
Responsibility:
- Manage bookings
- Validate booking before storing
- Reject conflicting bookings

Flow:
User → BookingService → BookingValidator

Booking Rules:
1. Invalid booking → "Rejected"
2. Time conflict → "Rejected"
3. Otherwise → "Confirmed"
*/
class BookingService {

    private final BookingValidator validator;
    private final List<Booking> bookings;

    // Constructor
    public BookingService(BookingValidator validator) {
        this.validator = validator;
        this.bookings = new ArrayList<>();
    }

    // Add booking
    public String addBooking(Booking booking) {

        if (!validator.isValid(booking)) {
            return "Rejected";
        }

        if (hasConflict(booking)) {
            return "Rejected";
        }

        bookings.add(booking);
        return "Confirmed";
    }

    // Check whether booking conflicts with an existing booking
    private boolean hasConflict(Booking booking) {

        for (Booking existing : bookings) {

            if (isSameRoom(booking, existing)
                    && isTimeOverlapping(booking, existing)) {
                return true;
            }
        }

        return false;
    }

    // Check whether two bookings belong to the same room
    private boolean isSameRoom(Booking booking1, Booking booking2) {

        String roomId1 = booking1.getRoom().getRoomId();
        String roomId2 = booking2.getRoom().getRoomId();

        return roomId1.equals(roomId2);
    }

    // Check time overlap
    private boolean isTimeOverlapping(Booking booking1, Booking booking2) {

        return booking1.getStartTime() < booking2.getEndTime()
                && booking2.getStartTime() < booking1.getEndTime();
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        BookingValidator validator = new BookingValidator();
        BookingService service = new BookingService(validator);

        Room room1 = new Room("A101");

        Booking b1 = new Booking(room1, 10, 12);
        Booking b2 = new Booking(room1, 11, 13);
        Booking b3 = new Booking(room1, 14, 16);

        System.out.println(service.addBooking(b1));
        System.out.println(service.addBooking(b2));
        System.out.println(service.addBooking(b3));
    }
}
