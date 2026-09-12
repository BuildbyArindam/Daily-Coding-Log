/*
 * Problem: Design a User Login System
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDUML/problems/UMLLLD11
 * Date: 2026-09-12
 * Difficulty: Medium
 * Topics: Low-Level Design (LLD), OOP Design, Encapsulation, Authentication Systems
 *
 * Approach:
 * - Model the system with 3 classes: User (data holder), Database (credential
 *   store + validation), AuthService (orchestrates login by delegating to Database).
 * - User encapsulates username/password with getters only (no setters -> immutable-ish).
 * - Database owns a HashMap<username, password> and exposes a single validateUser()
 *   method so credential-checking logic stays in one place.
 * - AuthService depends on Database (composition) and exposes login() as the
 *   public-facing entry point, keeping User decoupled from validation logic.
 *
 * Time Complexity: O(1) average per login() call (HashMap get/containsKey)
 * Space Complexity: O(n) where n = number of registered users stored in Database
 */


// ----------------------------- Solution ----------------------------------


import java.util.*;

// ================= USER =================
/*
Encapsulation:
- Store username and password
- Provide getter methods
*/
class User {

    private String username;
    private String password;

    // Constructor
    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // Getters
    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }
}


// ================= DATABASE =================
/*
Responsibility:
- Stores multiple user credentials
- Maintains username → password mapping
- Validates username and password
*/
class Database {

    // Store credentials
    private Map<String, String> users;

    // Constructor - preload valid users
    public Database() {
        users = new HashMap<>();

        // Preloaded valid user
        users.put("admin", "1234");
    }

    // Validate username and password
    public boolean validateUser(String username, String password) {

        // Null inputs are invalid
        if (username == null || password == null) {
            return false;
        }

        // Check username and corresponding password
        return users.containsKey(username)
                && users.get(username).equals(password);
    }
}


// ================= AUTH SERVICE =================
/*
Dependency + Flow:
- Handles login process
- Uses Database for validation

Flow:
User → AuthService → Database
*/
class AuthService {

    // Private Database reference
    private Database db;

    // Constructor
    public AuthService(Database db) {
        this.db = db;
    }

    // Login method
    public boolean login(String username, String password) {

        // AuthService coordinates with Database
        return db.validateUser(username, password);
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        Database db = new Database();
        AuthService auth = new AuthService(db);

        User u1 = new User("admin", "1234");
        User u2 = new User("guest", "wrong");

        System.out.println(auth.login(u1.getUsername(), u1.getPassword())
                ? "Login Successful" : "Login Failed");

        System.out.println(auth.login(u2.getUsername(), u2.getPassword())
                ? "Login Successful" : "Login Failed");
    }
}
