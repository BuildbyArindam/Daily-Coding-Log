/**
 * Problem: Report Generation System Refactor
 * Link: https://www.codechef.com/practice/course/lld/LLDCLEANCD2/problems/CNCDTWO10
 * Date: 2026-09-13
 * Topic: SOLID Principles (Single Responsibility Principle) / OOP Design
 *
 * Approach:
 * Refactored a monolithic report generator into 4 single-responsibility classes:
 *  - DataProvider: owns and validates report data, exposes filtered queries
 *  - ReportFormatter: converts raw entries into styled multiline text
 *  - ReportRenderer: handles output/display concerns
 *  - ReportService: orchestrates the pipeline (load -> validate -> filter -> format -> style -> render)
 * Each class depends only on what it needs; ReportService is injected with
 * collaborators via constructor (manual DI), keeping it decoupled from
 * concrete data/formatting/rendering logic.
 *
 * Time Complexity: O(n) — n = number of report entries (single pass for
 * filterData, single pass for formatData; loadData copy is also O(n)).
 * Space Complexity: O(n) — filtered list + StringBuilder buffer scale with
 * the number of matching entries.
 */


// ------------------------------ Solution -----------------------------


import java.util.*;

// ================= DATA PROVIDER =================
/*
Responsibilities:
- Store report entries
- Manage internally stored report data
- Validate report data
- Filter matching report entries
*/
class DataProvider {

    // Store report entries internally using a List
    private List<String> reportEntries;


    /*
    Initialize sample report data using
    these exact entries:

    - Monthly Sales Report
    - Employee Attendance
    - Sales Forecast
    */
    public DataProvider() {
        reportEntries = new ArrayList<>();

        reportEntries.add("Monthly Sales Report");
        reportEntries.add("Employee Attendance");
        reportEntries.add("Sales Forecast");
    }

    /*
    Return all report entries
    */
    public List<String> loadData() {
        return new ArrayList<>(reportEntries);
    }

    /*
    Return true if report data exists
    Return false otherwise
    */
    public boolean validateData() {
        return !reportEntries.isEmpty();
    }

    /*
    Return matching report entries
    from internally stored report data

    Rules:
    - filtering must be case-insensitive
    - return matching entries only
    - store filtered entries inside a new List
    */
    public List<String> filterData(String criteria) {

        List<String> filteredEntries = new ArrayList<>();

        if (criteria == null) {
            return filteredEntries;
        }

        String keyword = criteria.toLowerCase();

        for (String entry : reportEntries) {
            if (entry.toLowerCase().contains(keyword)) {
                filteredEntries.add(entry);
            }
        }

        return filteredEntries;
    }
}


// ================= REPORT FORMATTER =================
/*
Responsibilities:
- Format report content
- Apply report styling
*/
class ReportFormatter {

    /*
    Convert report entries into formatted multiline text

    Example:
    Entry1
    Entry2

    Hint:
    - Use StringBuilder for building multiline content
    */
    public String formatData(List<String> data) {

        StringBuilder formattedContent = new StringBuilder();

        for (String entry : data) {
            formattedContent.append(entry).append("\n");
        }

        return formattedContent.toString();
    }

    /*
    Add report decorations and separators

    Use the prewritten structure below
    and place formatted content in between.

    Note: Do not modify prewritten "styledContent"

    Finally:
    - return the complete styled report string
    */
    public String applyStyles(String content) {

        String styledContent =
                "====================\n"
              + "REPORT\n"
              + "====================\n"
              + content
              + "====================";

        return styledContent;
    }
}


// ================= REPORT RENDERER =================
/*
Responsibilities:
- Render final report output
*/
class ReportRenderer {

    /*
    Display final formatted report content

    Hint:
    - Use console output
    */
    public void render(String formattedContent) {
        System.out.println(formattedContent);
    }
}


// ================= REPORT SERVICE =================
/*
Responsibilities:
- Coordinate complete report generation flow
- Delegate work to helper classes
*/
class ReportService {

    // Store required helper objects
    private DataProvider dataProvider;
    private ReportFormatter reportFormatter;
    private ReportRenderer reportRenderer;


    /*
    Initialize all helper objects using constructor
    */
    public ReportService(
            DataProvider dataProvider,
            ReportFormatter reportFormatter,
            ReportRenderer reportRenderer
    ) {
        this.dataProvider = dataProvider;
        this.reportFormatter = reportFormatter;
        this.reportRenderer = reportRenderer;
    }

    /*
    Execute report generation flow

    Expected Sequence:
    1. load report data
    2. validate report data
    3. filter matching report entries
    4. format filtered data
    5. apply report styling
    6. render final report

    Important:
    - Use helper classes for each responsibility
    - Do NOT place all logic inside this method

    Filter Criteria:
    - Use "sales" for filtering report entries
    */
    public void generateReport() {

        // 1. Load report data
        List<String> data = dataProvider.loadData();

        // 2. Validate report data
        if (!dataProvider.validateData()) {
            System.out.println("No report data available.");
            return;
        }

        // 3. Filter matching report entries
        List<String> filteredData =
                dataProvider.filterData("sales");

        // 4. Format filtered data
        String formattedContent =
                reportFormatter.formatData(filteredData);

        // 5. Apply report styling
        String styledContent =
                reportFormatter.applyStyles(formattedContent);

        // 6. Render final report
        reportRenderer.render(styledContent);
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        // Create helper objects
        DataProvider dataProvider =
                new DataProvider();

        ReportFormatter reportFormatter =
                new ReportFormatter();

        ReportRenderer reportRenderer =
                new ReportRenderer();

        // Create ReportService object
        ReportService reportService =
                new ReportService(
                        dataProvider,
                        reportFormatter,
                        reportRenderer
                );

        // Execute report generation flow
        reportService.generateReport();
    }
}
