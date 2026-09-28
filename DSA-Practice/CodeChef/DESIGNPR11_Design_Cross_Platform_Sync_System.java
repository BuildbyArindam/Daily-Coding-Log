/*
 * Problem    : Design Cross-Platform Sync System
 * Platform   : CodeChef (LLD course)
 * Difficulty : Hard
 * Topics     : LLD, Adapter, Strategy, Facade, OOP
 * Link       : https://www.codechef.com/practice/course/lld/LLDDESIGN/problems/DESIGNPR11
 * Date       : 28-09-2026
 *
 * Approach:
 *   - Adapter (CRMAdapter) wraps the incompatible ExternalCRM behind the
 *     common ExternalSourceAdapter interface, so new sources plug in easily.
 *   - Strategy (FullSyncStrategy / IncrementalSyncStrategy) makes the sync
 *     algorithm swappable at runtime.
 *   - SyncManager fetches data via the adapter and delegates to the strategy.
 *   - SyncFacade exposes a single executeSync() entry point to the client.
 *
 * Time Complexity  : O(1) per sync call (excluding the external fetch cost)
 * Space Complexity : O(1) extra space
 */


// -------------------------------------- Solution ----------------------------------------------


import java.util.*;

// ================= EXTERNAL CRM =================
class ExternalCRM {
    public String fetchCustomerData() {
        return "Customer Data From CRM";
    }
}

// ================= EXTERNAL SOURCE ADAPTER =================
interface ExternalSourceAdapter {
    String getData();
}

// ================= CRM ADAPTER =================
class CRMAdapter implements ExternalSourceAdapter {
    private ExternalCRM externalCRM;
    public CRMAdapter(ExternalCRM externalCRM) {
        this.externalCRM = externalCRM;
    }
    @Override
    public String getData() {
        return externalCRM.fetchCustomerData();
    }
}

// ================= SYNC STRATEGY =================
interface SyncStrategy {
    void synchronize(String data);
}

// ================= FULL SYNC STRATEGY =================
class FullSyncStrategy implements SyncStrategy {
    @Override
    public void synchronize(String data) {
        System.out.println("Full Sync Completed: " + data);
    }
}

// ================= INCREMENTAL SYNC STRATEGY =================
class IncrementalSyncStrategy implements SyncStrategy {
    @Override
    public void synchronize(String data) {
        System.out.println("Incremental Sync Completed: " + data);
    }
}

// ================= SYNC MANAGER =================
class SyncManager {
    public void synchronize(ExternalSourceAdapter adapter, SyncStrategy strategy) {
        String data = adapter.getData();
        strategy.synchronize(data);
    }
}

// ================= SYNC FACADE =================
class SyncFacade {
    private SyncManager syncManager;
    public SyncFacade(SyncManager syncManager) {
        this.syncManager = syncManager;
    }
    public void executeSync(ExternalSourceAdapter adapter, SyncStrategy strategy) {
        syncManager.synchronize(adapter, strategy);
    }
}

// ================= MAIN =================
public class Codechef {
    public static void main(String[] args) {
        ExternalCRM externalCRM = new ExternalCRM();
        ExternalSourceAdapter adapter = new CRMAdapter(externalCRM);
        SyncStrategy strategy = new FullSyncStrategy();
        SyncManager syncManager = new SyncManager();
        SyncFacade syncFacade = new SyncFacade(syncManager);
        syncFacade.executeSync(adapter, strategy);
    }
}
