/*
 * Platform   : CodeChef
 * Problem    : Design Modular Computer Assembly System (DESIGNPR12)
 * Link       : https://www.codechef.com/practice/course/lld/LLDDESIGN/problems/DESIGNPR12
 * Difficulty : Hard
 * Topics     : Low-Level Design, Builder, Factory, Decorator
 * Date       : 2026-10-03
 *
 * Approach:
 *  - Builder (ComputerBuilder): constructs a Computer step by step with
 *    chained setters for CPU, RAM and storage.
 *  - Factory (ComponentFactory): centralizes component creation so callers
 *    don't build components directly.
 *  - Decorator (PerformanceDecorator): wraps a ComputerConfiguration to
 *    layer upgrades onto BasicConfiguration without modifying it.
 *  - AssemblyService: composes the factory and configuration to assemble
 *    the computer and print the result.
 *
 * Time Complexity  : O(1), a constant number of operations (O(d) for d stacked decorators)
 * Space Complexity : O(1), a fixed number of objects (O(d) for d decorators)
 */


// --------------------------------------- Solution ------------------------------------------------


import java.util.*;

// ================= COMPUTER =================
class Computer {
    private String cpu;
    private String ram;
    private String storage;
    public Computer(String cpu,
                    String ram,
                    String storage) {
        this.cpu = cpu;
        this.ram = ram;
        this.storage = storage;
    }
    public String getCpu() {
        return cpu;
    }
    public String getRam() {
        return ram;
    }
    public String getStorage() {
        return storage;
    }
}

class ComputerBuilder {
    private String cpu;
    private String ram;
    private String storage;
    public ComputerBuilder setCpu(String cpu) {
        this.cpu = cpu;
        return this;
    }
    public ComputerBuilder setRam(String ram) {
        this.ram = ram;
        return this;
    }
    public ComputerBuilder setStorage(String storage) {
        this.storage = storage;
        return this;
    }
    public Computer build() {
        return new Computer(cpu, ram, storage);
    }
}

// ================= COMPONENT FACTORY =================
class ComponentFactory {
    public String createComponent(String componentName) {
        return "Component Created: " + componentName;
    }
}

// ================= COMPUTER CONFIGURATION =================
interface ComputerConfiguration {
    String getDescription();
}

// ================= BASIC CONFIGURATION =================
class BasicConfiguration implements ComputerConfiguration {
    @Override
    public String getDescription() {
        return "Basic Computer";
    }
}

// ================= PERFORMANCE DECORATOR =================
class PerformanceDecorator implements ComputerConfiguration {
    private ComputerConfiguration computerConfiguration;
    public PerformanceDecorator(
            ComputerConfiguration computerConfiguration
    ) {
        this.computerConfiguration = computerConfiguration;
    }
    @Override
    public String getDescription() {
        return computerConfiguration.getDescription()
                + " + Performance Upgrade";
    }
}

// ================= ASSEMBLY SERVICE =================
class AssemblyService {
    private ComponentFactory componentFactory;
    public AssemblyService(
            ComponentFactory componentFactory
    ) {
        this.componentFactory = componentFactory;
    }
    public void assembleComputer(
            Computer computer,
            ComputerConfiguration configuration
    ) {
        String componentResult =
                componentFactory.createComponent(computer.getCpu());
        System.out.println(componentResult);
        System.out.println(configuration.getDescription());
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        Computer computer =
                new ComputerBuilder()
                        .setCpu("Intel i7")
                        .setRam("16GB")
                        .setStorage("1TB SSD")
                        .build();
        ComputerConfiguration configuration =
                new PerformanceDecorator(
                        new BasicConfiguration()
                );
        ComponentFactory componentFactory =
                new ComponentFactory();
        AssemblyService assemblyService =
                new AssemblyService(
                        componentFactory
                );
        assemblyService.assembleComputer(
                computer,
                configuration
        );
    }
}
