/*
 * Platform   : CodeChef
 * Problem    : Design IoT Device Manager
 * Link       : https://www.codechef.com/practice/course/lld/LLDDESIGN/problems/DESIGNPR13
 * Difficulty : Hard
 * Date       : 03-Oct-2026
 * Topics     : Low-Level Design, Factory, Command, State, Observer
 *
 * Approach:
 *   - Factory (DeviceFactory) creates Device objects.
 *   - Command (UpdateCommand / FirmwareUpdateCommand) encapsulates the update action.
 *   - State (DeviceState: Online, Maintenance) models device lifecycle behavior.
 *   - Observer (MonitoringObserver / HealthMonitor) is notified about device events.
 *   - FleetManager orchestrates: execute update -> online state -> notify observer
 *     -> maintenance state.
 *
 * Time Complexity  : O(1) per manageDevice call
 * Space Complexity : O(1)
 */


// ---------------------------------------- Solution --------------------------------------------------


import java.util.*;

// ================= DEVICE =================
class Device {
    private String deviceId;
    private String deviceName;
    public Device(String deviceId,
                  String deviceName) {
        this.deviceId = deviceId;
        this.deviceName = deviceName;
    }
    public String getDeviceId() {
        return deviceId;
    }
    public String getDeviceName() {
        return deviceName;
    }
}

// ================= DEVICE FACTORY =================
class DeviceFactory {
    public Device createDevice(String deviceId,
                               String deviceName) {

        return new Device(deviceId, deviceName);
    }
}

// ================= UPDATE COMMAND =================
interface UpdateCommand {
    void execute(Device device);
}

// ================= FIRMWARE UPDATE COMMAND =================
class FirmwareUpdateCommand implements UpdateCommand {
    @Override
    public void execute(Device device) {
        System.out.println(
                "Firmware updated for device: "
                + device.getDeviceId()
        );
    }
}

// ================= DEVICE STATE =================
interface DeviceState {
    void handle(Device device);
}

// ================= ONLINE STATE =================
class OnlineState implements DeviceState {
    @Override
    public void handle(Device device) {
        System.out.println(
                "Device Online: "
                + device.getDeviceId()
        );
    }
}

// ================= MAINTENANCE STATE =================
class MaintenanceState implements DeviceState {
    @Override
    public void handle(Device device) {
        System.out.println(
                "Device Maintenance: "
                + device.getDeviceId()
        );
    }
}

// ================= MONITORING OBSERVER =================
interface MonitoringObserver {
    void update(Device device);
}

// ================= HEALTH MONITOR =================
class HealthMonitor implements MonitoringObserver {
    @Override
    public void update(Device device) {
        System.out.println(
                "Health Monitor Alert For: "
                + device.getDeviceId()
        );
    }
}

// ================= FLEET MANAGER =================
class FleetManager {
    private MonitoringObserver monitoringObserver;
    public FleetManager(
            MonitoringObserver monitoringObserver
    ) {
        this.monitoringObserver = monitoringObserver;
    }
    public void manageDevice(Device device,
                             UpdateCommand updateCommand) {
        updateCommand.execute(device);
        DeviceState onlineState = new OnlineState();
        onlineState.handle(device);
        monitoringObserver.update(device);
        DeviceState maintenanceState = new MaintenanceState();
        maintenanceState.handle(device);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        DeviceFactory deviceFactory = new DeviceFactory();
        Device device =
                deviceFactory.createDevice(
                        "DEV101",
                        "Smart Sensor"
                );
        UpdateCommand updateCommand =
                new FirmwareUpdateCommand();
        MonitoringObserver observer =
                new HealthMonitor();
        FleetManager fleetManager =
                new FleetManager(
                        observer
                );
        fleetManager.manageDevice(
                device,
                updateCommand
        );
    }
}
