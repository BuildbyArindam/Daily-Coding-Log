/*
 * Problem: Design A Resume Builder System
 * Platform: CodeChef (LLD Practice Course)
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD3/problems/CNCDTH12
 * Date: 2026-09-15
 * Difficulty: Medium
 * Topics: Low Level Design, SOLID Principles (Single Responsibility Principle),
 *         Separation of Concerns, Object Composition
 *
 * Approach:
 * Split the resume-building process into single-purpose classes instead of one
 * god object. Candidate holds data only; ResumeValidator checks required fields;
 * one Formatter class per section (Personal/Education/Skills/Experience) builds
 * that section's string; ResumePrinter handles output. Main wires everything
 * together and concatenates the formatted sections into the final resume.
 * This keeps each class independently testable/extensible (e.g. add a new
 * section or swap the printer without touching validation or formatting logic).
 *
 * Time Complexity: O(1) — fixed number of fields, each formatted in O(1)
 *                   (O(n) if you count string length n of concatenated fields)
 * Space Complexity: O(n) — proportional to total length of stored candidate fields
 */


// --------------------------- Solution -----------------------------------------


import java.util.*;

// ================= CANDIDATE =================
/*
Responsibilities:
- Store candidate information
- Maintain candidate details
*/
class Candidate {

    // Encapsulated fields
    private String name;
    private String education;
    private String skills;
    private String experience;

    /*
    Initialize candidate details
    */
    public Candidate(
            String name,
            String education,
            String skills,
            String experience
    ) {
        this.name = name;
        this.education = education;
        this.skills = skills;
        this.experience = experience;
    }

    /*
    Return candidate name
    */
    public String getName() {
        return name;
    }

    /*
    Return education details
    */
    public String getEducation() {
        return education;
    }

    /*
    Return skills information
    */
    public String getSkills() {
        return skills;
    }

    /*
    Return experience details
    */
    public String getExperience() {
        return experience;
    }
}


// ================= RESUME VALIDATOR =================
/*
Responsibilities:
- Validate candidate information
*/
class ResumeValidator {

    /*
    Validate candidate information

    Rules:
    - candidate name cannot be null or empty
    - education details cannot be null or empty
    - skills cannot be null or empty
    - experience details cannot be null or empty

    If validation fails:
    - throw IllegalArgumentException
    */
    public void validate(Candidate candidate) {

        if (candidate == null) {
            throw new IllegalArgumentException("Candidate cannot be null");
        }

        if (candidate.getName() == null || candidate.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("Candidate name cannot be null or empty");
        }

        if (candidate.getEducation() == null || candidate.getEducation().trim().isEmpty()) {
            throw new IllegalArgumentException("Education details cannot be null or empty");
        }

        if (candidate.getSkills() == null || candidate.getSkills().trim().isEmpty()) {
            throw new IllegalArgumentException("Skills cannot be null or empty");
        }

        if (candidate.getExperience() == null || candidate.getExperience().trim().isEmpty()) {
            throw new IllegalArgumentException("Experience details cannot be null or empty");
        }
    }
}


// ================= PERSONAL DETAILS FORMATTER =================
/*
Responsibilities:
- Format personal details section
*/
class PersonalDetailsFormatter {

    /*
    Generate formatted personal details section

    Use below format exactly:

    Name: Rahul

    Return:
    - formatted personal details string
    */
    public String format(Candidate candidate) {
        return "Name: " + candidate.getName();
    }
}


// ================= EDUCATION FORMATTER =================
/*
Responsibilities:
- Format education section
*/
class EducationFormatter {

    /*
    Generate formatted education section

    Use below format exactly:

    Education: B.Tech Computer Science

    Return:
    - formatted education string
    */
    public String format(Candidate candidate) {
        return "Education: " + candidate.getEducation();
    }
}


// ================= SKILLS FORMATTER =================
/*
Responsibilities:
- Format skills section
*/
class SkillsFormatter {

    /*
    Generate formatted skills section

    Use below format exactly:

    Skills: Java, SQL

    Return:
    - formatted skills string
    */
    public String format(Candidate candidate) {
        return "Skills: " + candidate.getSkills();
    }
}


// ================= EXPERIENCE FORMATTER =================
/*
Responsibilities:
- Format experience section
*/
class ExperienceFormatter {

    /*
    Generate formatted experience section

    Use below format exactly:

    Experience: 2 Years

    Return:
    - formatted experience string
    */
    public String format(Candidate candidate) {
        return "Experience: " + candidate.getExperience();
    }
}


// ================= RESUME PRINTER =================
/*
Responsibilities:
- Print final formatted resume
*/
class ResumePrinter {

    /*
    Print final formatted resume
    */
    public void printResume(String resume) {
        System.out.println(resume);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        Candidate candidate =
                new Candidate(
                        "Rahul",
                        "B.Tech Computer Science",
                        "Java, SQL",
                        "2 Years"
                );

        ResumeValidator validator = new ResumeValidator();

        PersonalDetailsFormatter personalFormatter = new PersonalDetailsFormatter();

        EducationFormatter educationFormatter = new EducationFormatter();

        SkillsFormatter skillsFormatter = new SkillsFormatter();

        ExperienceFormatter experienceFormatter = new ExperienceFormatter();

        ResumePrinter printer = new ResumePrinter();

        validator.validate(candidate);

        String personalDetails = personalFormatter.format(candidate);

        String education = educationFormatter.format(candidate);

        String skills = skillsFormatter.format(candidate);

        String experience = experienceFormatter.format(candidate);

        String resume =
                personalDetails +
                "\n" +
                education +
                "\n" +
                skills +
                "\n" +
                experience;

        printer.printResume(resume);
    }
}
