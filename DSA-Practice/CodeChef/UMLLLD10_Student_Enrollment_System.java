/*
 * Problem: Student Enrollment System
 * Platform: CodeChef (LLD/UML Practice)
 * Link: https://www.codechef.com/practice/course/lld/LLDUML/problems/UMLLLD10?folder=%2Fhome%2Fchef%2Fworkspace
 * Date: 2026-09-11
 * Difficulty: Medium
 * Topics: LLD, OOP, Encapsulation, Association
 *
 * Approach:
 * - Student: pure data holder (encapsulated id/name with getters + updateName).
 * - Course: owns its student list; exposes addStudent/removeStudent/getStudentCount
 *           so enrollment state lives with the Course, not the caller.
 * - CourseService: stateless coordinator. Validates (null checks) before delegating
 *           to Course.addStudent(), then logs the enrollment. Keeps business flow
 *           (validate -> record) separate from data storage (Course) and data
 *           definition (Student).
 * - Flow: Student -> CourseService -> Course
 *
 * Time Complexity: O(1) per enrollCourse() call
 *   - validateEnrollment(): O(1) null checks
 *   - recordEnrollment(): O(1) amortized ArrayList.add()
 * Space Complexity: O(n) where n = total students enrolled across all courses
 *   (each Course holds a List<Student> for its own roster)
 */


// ------------------------------- Solution -------------------------------------


import java.util.*;

// ================= STUDENT =================
/*
Encapsulation:
- Store id and name
- Provide getter methods
- Allow updating name
*/
class Student {

    private String id;
    private String name;

    // Constructor
    public Student(String id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    // Update name
    public void updateName(String name) {
        this.name = name;
    }
}


// ================= COURSE =================
/*
Association:
- A course contains multiple students
- Course should manage its own student list

Provide:
- addStudent()
- removeStudent()
- getStudentCount()
*/
class Course {

    private String courseId;
    private String title;
    private List<Student> students;

    // Constructor
    public Course(String courseId, String title) {
        this.courseId = courseId;
        this.title = title;
        this.students = new ArrayList<>();
    }

    // Add student to course
    public void addStudent(Student student) {
        students.add(student);
    }

    // Remove student from course
    public void removeStudent(Student student) {
        students.remove(student);
    }

    // Get number of students
    public int getStudentCount() {
        return students.size();
    }

    // Get course ID
    public String getCourseId() {
        return courseId;
    }
}


// ================= COURSE SERVICE =================
/*
Dependency + Flow Control:
- Acts as coordinator
- Should NOT store data

Responsibilities:
- enroll student into course
- validate enrollment
- record enrollment

recordEnrollment():
- Should print:
  "Student <id> enrolled in Course <courseId>"

Flow:
Student → CourseService → Course
*/
class CourseService {

    // Enroll student into course
    public void enrollCourse(Student student, Course course) {
        if (validateEnrollment(student, course)) {
            recordEnrollment(student, course);
        }
    }

    // Validate enrollment
    public boolean validateEnrollment(Student student, Course course) {
        if (student == null || course == null) {
            return false;
        }

        return true;
    }

    // Record enrollment
    public void recordEnrollment(Student student, Course course) {
        course.addStudent(student);
        System.out.println(
            "Student " + student.getId() + " enrolled in Course " + course.getCourseId()
        );
    }
}


// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {

        Student s1 = new Student("S1", "Alice");
        Student s2 = new Student("S2", "Bob");

        Course c1 = new Course("C1", "Math");

        CourseService service = new CourseService();

        service.enrollCourse(s1, c1);
        service.enrollCourse(s2, c1);
    }
}
