/**
 * Problem: Design Student Result Processing System
 * Platform: CodeChef
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD2/problems/CNCDTWO12
 * Date: 2026-09-14
 * Difficulty: Medium
 * Topic: Object-Oriented Design (LLD) — Encapsulation, Single Responsibility Principle
 *
 * Approach:
 * Modeled the domain as three classes with clear separation of concerns:
 *   - Subject: holds name + marks (data only)
 *   - Student: holds name + list of Subjects
 *   - ResultService: stateless service that computes totals, valid-subject
 *     count, average, pass/fail status, and formats the summary — all logic
 *     is delegated to small single-purpose methods, orchestrated by
 *     processResult().
 * Negative marks are treated as invalid and excluded from both the total
 * and the subject count used for averaging.
 *
 * Time Complexity: O(n) per student, where n = number of subjects
 *                  (single pass for total, single pass for valid count)
 * Space Complexity: O(n) to store each student's subject list; O(1) extra
 *                   space in ResultService itself
 */


// ----------------------------- Solution --------------------------------------


import java.util.*;

// ================= SUBJECT =================
/*
Responsibilities:
- Store subject name
- Store subject marks
*/
class Subject {

    /*
    Create encapsulated fields for:
    - subject name using 'name'
    - subject marks using 'marks'
    */
    private String name;
    private int marks;

    /*
    Initialize subject details
    */
    public Subject(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }

    /*
    Return subject name
    */
    public String getName() {
        return name;
    }

    /*
    Return subject marks
    */
    public int getMarks() {
        return marks;
    }
}


// ================= STUDENT =================
/*
Responsibilities:
- Store student name
- Store student subjects
*/
class Student {

    /*
    Create encapsulated fields for:
    - student name using 'name'
    - subject list using 'subjects'

    Important:
    - use List for storing subjects
    */
    private String name;
    private List<Subject> subjects;

    /*
    Initialize:
    - student name
    - empty subject list
    */
    public Student(String name) {
        this.name = name;
        this.subjects = new ArrayList<>();
    }

    /*
    Return student name
    */
    public String getName() {
        return name;
    }

    /*
    Return subject list
    */
    public List<Subject> getSubjects() {
        return subjects;
    }
}


// ================= RESULT SERVICE =================
/*
Responsibilities:
- Process student result
- Calculate total marks
- Count valid subjects
- Calculate average marks
- Determine final result
- Generate summary
*/
class ResultService {

    /*
    Calculate and return total marks of all valid subjects

    Rules:
    - ignore negative marks
    */
    public int calculateTotalMarks(Student student) {
        int totalMarks = 0;

        for (Subject subject : student.getSubjects()) {
            if (subject.getMarks() >= 0) {
                totalMarks += subject.getMarks();
            }
        }

        return totalMarks;
    }

    /*
    Count and return valid subjects

    Rules:
    - only subjects with marks >= 0 are valid
    */
    public int countValidSubjects(Student student) {
        int validSubjects = 0;

        for (Subject subject : student.getSubjects()) {
            if (subject.getMarks() >= 0) {
                validSubjects++;
            }
        }

        return validSubjects;
    }

    /*
    Calculate and return average marks

    Rules:
    - avoid division by zero
    - return 0 when subject count is 0

    Formula:
    totalMarks / subjectCount
    */
    public double calculateAverageMarks(int totalMarks, int subjectCount) {
        if (subjectCount == 0) {
            return 0;
        }

        return (double) totalMarks / subjectCount;
    }

    /*
    Determine final result

    Rules:
    - average >= 40 -> PASS
    - otherwise -> FAIL
    */
    public String determineResult(double average) {
        if (average >= 40) {
            return "PASS";
        }

        return "FAIL";
    }

    /*
    Generate formatted result summary as given below

    Return format:
    Student: Rahul
    Average: 70.0
    Status: PASS

    Hint:
    - Use string concatenation
    */
    public String generateSummary(Student student, double average, String status) {
        return "Student: " + student.getName()
                + "\nAverage: " + average
                + "\nStatus: " + status;
    }

    /*
    Print final summary
    */
    public void printResult(String summary) {
        System.out.println(summary);
    }

    /*
    Execute complete result processing flow

    Expected Flow:
    1. calculate total marks
    2. count valid subjects
    3. calculate average marks
    4. determine final result
    5. generate summary
    6. print final summary

    Important:
    - keep this method small and readable
    - delegate work to helper methods
    */
    public void processResult(Student student) {
        int totalMarks = calculateTotalMarks(student);

        int subjectCount = countValidSubjects(student);

        double average = calculateAverageMarks(totalMarks, subjectCount);

        String status = determineResult(average);

        String summary = generateSummary(student, average, status);

        printResult(summary);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        Subject math = new Subject("Math", 80);

        Subject science = new Subject("Science", 60);

        Subject english = new Subject("English", 70);

        Student student = new Student("Rahul");

        student.getSubjects().add(math);

        student.getSubjects().add(science);

        student.getSubjects().add(english);

        ResultService resultService = new ResultService();

        resultService.processResult(student);
    }
}
