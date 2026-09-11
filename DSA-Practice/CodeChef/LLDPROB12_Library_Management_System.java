/*
 * Problem: Design a Library Management System (LLD)
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDFND/problems/LLDPROB12
 * Difficulty: Medium
 * Topics: LLD, OOP Design, Encapsulation, Aggregation
 * Date Solved: 2026-09-11
 *
 * Approach:
 * Modeled the system as three classes — Book, Member, Library — following
 * OOP principles (encapsulation, association, aggregation). Book owns its
 * own issue/return state machine and validates transitions internally
 * (no double-issue, only the issuing member can return). Member depends on
 * Book to perform issue/return and logs the action. Library aggregates
 * Book objects and exposes an unmodifiable view of its collection.
 *
 * Time Complexity: O(1) for issueBook/returnBook (single object mutation);
 *                   O(1) for addBook; O(n) if scanning all books via getBooks().
 * Space Complexity: O(n) for n books stored in the Library.
 */


// ------------------------------- Solution -------------------------------


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// ================= BOOK =================
/*
Encapsulation:
- Create fields to store:
  - book id
  - issued status
  - which member currently holds the book

- Provide necessary methods to:
  - read book details
  - update issued state
*/
class Book {

    // Private fields -> Encapsulation
    private final String id;
    private boolean issued;
    private Member issuedTo;

    // Constructor
    public Book(String id) {
        this.id = id;
        this.issued = false;
        this.issuedTo = null;
    }

    // Get book id
    public String getId() {
        return id;
    }

    // Check whether book is issued
    public boolean isIssued() {
        return issued;
    }

    // Get the member who currently has the book
    public Member getIssuedTo() {
        return issuedTo;
    }

    /*
     * Issue this book to a member.
     * Returns true only when the issue is successful.
     */
    boolean issueTo(Member member) {

        // Null member -> reject safely
        if (member == null) {
            return false;
        }

        // Already issued -> reject safely
        if (issued) {
            return false;
        }

        issued = true;
        issuedTo = member;

        return true;
    }

    /*
     * Return this book.
     * Returns true only when the correct member returns it.
     */
    boolean returnBook(Member member) {

        // Null member -> reject safely
        if (member == null) {
            return false;
        }

        // Book is not issued -> reject
        if (!issued) {
            return false;
        }

        // Only the member who issued it can return it
        if (issuedTo != member) {
            return false;
        }

        issued = false;
        issuedTo = null;

        return true;
    }
}


// ================= MEMBER =================
/*
Association + Dependency:
- Each member has an id
- Member should be able to:
  - borrow (issue) a book
  - return a book

- Ensure:
  - book cannot be issued if already issued
  - proper linkage between member and book

- Print messages:
  - When issued -> "Book <id> issued to <memberId>"
  - When returned -> "Book <id> returned"
*/
class Member {

    // Private field -> Encapsulation
    private final String id;

    // Constructor
    public Member(String id) {
        this.id = id;
    }

    // Get member id
    public String getId() {
        return id;
    }

    /*
     * Member depends on Book to issue it.
     */
    public void issueBook(Book book) {

        // Null input -> do nothing
        if (book == null) {
            return;
        }

        // Issue only if Book accepts the operation
        if (book.issueTo(this)) {
            System.out.println(
                "Book " + book.getId() + " issued to " + id
            );
        }
    }

    /*
     * Member depends on Book to return it.
     */
    public void returnBook(Book book) {

        // Null input -> do nothing
        if (book == null) {
            return;
        }

        // Return only if Book accepts the operation
        if (book.returnBook(this)) {
            System.out.println(
                "Book " + book.getId() + " returned"
            );
        }
    }
}


// ================= LIBRARY =================
/*
Aggregation:
- Library should contain multiple books
- Books should exist independently

- Provide functionality to:
  - add books
  - retrieve list of books
*/
class Library {

    // Aggregation: Library contains Book objects
    private final List<Book> books;

    // Constructor
    public Library() {
        books = new ArrayList<>();
    }

    // Add book
    public void addBook(Book book) {

        // Ignore null safely
        if (book == null) {
            return;
        }

        books.add(book);
    }

    // Get books
    public List<Book> getBooks() {
        return Collections.unmodifiableList(books);
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        Library lib = new Library();

        Book b1 = new Book("B1");
        Book b2 = new Book("B2");

        lib.addBook(b1);
        lib.addBook(b2);

        Member m1 = new Member("M1");
        Member m2 = new Member("M2");

        // Normal issue
        m1.issueBook(b1);

        // Second member tries to issue same book
        // This will be rejected without crashing
        m2.issueBook(b1);

        // Wrong member tries to return book
        // This will be rejected without crashing
        m2.returnBook(b1);

        // Correct member returns book
        m1.returnBook(b1);

        // Null tests
        m1.issueBook(null);
        m1.returnBook(null);
    }
}
