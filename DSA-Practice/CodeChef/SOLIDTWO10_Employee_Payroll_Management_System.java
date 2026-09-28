/*
 * Problem   : Design Employee Payroll Management System
 * Platform  : CodeChef (LLD - SOLID Principles II)
 * Link      : https://www.codechef.com/practice/course/lld/LLDSOLIDTWO/problems/SOLIDTWO10
 * Difficulty: Medium
 * Topic     : LLD, SOLID, OOP, Strategy Pattern, Dependency Injection
 * Date      : 2026-09-28
 *
 * Approach:
 *   Each responsibility gets its own class so the design follows SOLID:
 *   - Employee            : holds employee data only (SRP)
 *   - SalaryCalculator    : abstraction for salary rules; StandardSalaryCalculator
 *                           adds a fixed 5000 allowance (OCP: new rules = new class)
 *   - TaxCalculator       : abstraction for tax rules; StandardTaxCalculator
 *                           applies 10% (OCP, LSP)
 *   - PayslipGenerator    : formats the payslip only (SRP)
 *   - PayrollService      : orchestrates the flow and depends on interfaces,
 *                           with the calculators injected per call (DIP)
 *   Flow: base salary -> final salary -> tax -> net salary -> payslip.
 *
 * Time Complexity : O(1) per employee processed
 * Space Complexity: O(1)
 */


// ------------------------------------ Solution ---------------------------------------------------


import java.util.*;

// ================= EMPLOYEE =================
class Employee {
    private String employeeId;
    private String employeeName;
    private double baseSalary;
    public Employee(String employeeId, String employeeName, double baseSalary) {
        this.employeeId = employeeId;
        this.employeeName = employeeName;
        this.baseSalary = baseSalary;
    }
    public String getEmployeeId() {
        return employeeId;
    }
    public String getEmployeeName() {
        return employeeName;
    }
    public double getBaseSalary() {
        return baseSalary;
    }
}

// ================= SALARY CALCULATOR =================
interface SalaryCalculator {
    double calculateSalary(double baseSalary);
}

// ================= STANDARD SALARY CALCULATOR =================
class StandardSalaryCalculator implements SalaryCalculator {
    @Override
    public double calculateSalary(double baseSalary) {
        return baseSalary + 5000;
    }
}

// ================= TAX CALCULATOR =================
interface TaxCalculator {
    double calculateTax(double salary);
}

// ================= STANDARD TAX CALCULATOR =================
class StandardTaxCalculator implements TaxCalculator {
    @Override
    public double calculateTax(double salary) {
        return salary * 0.10;
    }
}

// ================= PAYSLIP GENERATOR =================
class PayslipGenerator {
    public String generatePayslip(Employee employee, double finalSalary, double tax) {
        double netSalary = finalSalary - tax;
        return "Employee ID: " + employee.getEmployeeId() + "\n"
             + "Employee Name: " + employee.getEmployeeName() + "\n"
             + "Final Salary: " + finalSalary + "\n"
             + "Tax Deducted: " + tax + "\n"
             + "Net Salary: " + netSalary;
    }
}

// ================= PAYROLL SERVICE =================
class PayrollService {
    private PayslipGenerator payslipGenerator;
    public PayrollService(PayslipGenerator payslipGenerator) {
        this.payslipGenerator = payslipGenerator;
    }
    public void processPayroll(Employee employee,
                               SalaryCalculator salaryCalculator,
                               TaxCalculator taxCalculator) {
        double finalSalary = salaryCalculator.calculateSalary(employee.getBaseSalary());
        double tax = taxCalculator.calculateTax(finalSalary);
        String payslip = payslipGenerator.generatePayslip(
                employee,
                finalSalary,
                tax
        );
        System.out.println(payslip);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        Employee employee = new Employee("EMP101", "Rahul", 50000);
        SalaryCalculator salaryCalculator = new StandardSalaryCalculator();
        TaxCalculator taxCalculator = new StandardTaxCalculator();
        PayslipGenerator payslipGenerator = new PayslipGenerator();
        PayrollService payrollService = new PayrollService(payslipGenerator);
        payrollService.processPayroll(employee, salaryCalculator, taxCalculator);
    }
}
