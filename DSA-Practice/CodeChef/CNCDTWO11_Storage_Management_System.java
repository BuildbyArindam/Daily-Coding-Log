/**
 * Problem   : Design a Storage Management System
 * Platform  : CodeChef
 * Link      : https://www.codechef.com/practice/course/lld/LLDCLEANCD2/problems/CNCDTWO11
 * Date      : 2026-09-14
 * Difficulty: Medium
 * Topic     : Low Level Design (LLD) - Strategy Pattern / Dependency Injection / Interface Abstraction
 *
 * Approach:
 * - Defined a Storage interface (save, load, clear) so any storage backend
 *   can be swapped in without changing consumer code.
 * - MemoryStorage and BackupStorage are two interchangeable implementations,
 *   each holding their own internal list.
 * - StorageService depends only on the Storage abstraction (constructor
 *   injection) and delegates all operations to it - this is the core
 *   Strategy/DI pattern being tested here.
 * - Invalid input (null / empty / blank strings) is filtered at the
 *   storage-implementation level before insertion.
 *
 * Complexity:
 * - save()  : O(1) amortized (ArrayList append)
 * - load()  : O(1) (returns reference to internal list; O(n) if a defensive copy is made)
 * - clear() : O(n) (ArrayList#clear walks the list to null out references)
 * - Space   : O(n) where n = number of stored entries
 */


// ---------------------------------- Solution ----------------------------------------


import java.util.*;

// ================= STORAGE =================
/*
Responsibilities:
- Define common storage operations
*/
interface Storage {

    /*
    TODO:
    Store valid data
    */
    void save(String data);

    /*
    TODO:
    Return stored data list
    */
    List<String> load();

    /*
    TODO:
    Remove all stored data
    */
    void clear();
}


// ================= MEMORY STORAGE =================
/*
Responsibilities:
- Store data using in-memory list
*/
class MemoryStorage implements Storage {

    /*
    TODO:
    Create internal list for storing data
    */
    private List<String> dataList;


    /*
    TODO:
    Initialize storage list
    */
    public MemoryStorage() {
        dataList = new ArrayList<>();
    }

    /*
    TODO:
    Store valid data

    Rules:
    - ignore null values
    - ignore empty strings
    */
    public void save(String data) {
        if (data != null && !data.trim().isEmpty()) {
            dataList.add(data);
        }
    }

    /*
    TODO:
    Return stored data
    */
    public List<String> load() {
        return dataList;
    }

    /*
    TODO:
    Clear stored data
    */
    public void clear() {
        dataList.clear();
    }
}


// ================= BACKUP STORAGE =================
/*
Responsibilities:
- Store backup data using separate in-memory list
*/
class BackupStorage implements Storage {

    /*
    TODO:
    Create backup storage list
    */
    private List<String> backupList;


    /*
    TODO:
    Initialize backup storage list
    */
    public BackupStorage() {
        backupList = new ArrayList<>();
    }

    /*
    TODO:
    Store valid backup data

    Rules:
    - ignore null values
    - ignore empty strings
    */
    public void save(String data) {
        if (data != null && !data.trim().isEmpty()) {
            backupList.add(data);
        }
    }

    /*
    TODO:
    Return backup data
    */
    public List<String> load() {
        return backupList;
    }

    /*
    TODO:
    Clear backup data
    */
    public void clear() {
        backupList.clear();
    }
}


// ================= STORAGE SERVICE =================
/*
Responsibilities:
- Coordinate storage operations
- Delegate operations to storage abstraction
*/
class StorageService {

    /*
    TODO:
    Store Storage abstraction reference
    */
    private Storage storage;


    /*
    TODO:
    Initialize storage object using constructor
    */
    public StorageService(Storage storage) {
        this.storage = storage;
    }

    /*
    TODO:
    Delegate save operation
    */
    public void saveData(String data) {
        storage.save(data);
    }

    /*
    TODO:
    Delegate load operation
    */
    public List<String> loadData() {
        return storage.load();
    }

    /*
    TODO:
    Delegate clear operation
    */
    public void clearStorage() {
        storage.clear();
    }
}


// ================= MAIN =================
public class Codechef {

    public static void main(String[] args) {

        // Create storage implementation
        Storage storage =
                new MemoryStorage();

        // Create service object
        StorageService storageService =
                new StorageService(storage);

        // Store sample data
        storageService.saveData("Report A");
        storageService.saveData("Monthly Summary");

        // Invalid data is ignored
        storageService.saveData(null);
        storageService.saveData("");
        storageService.saveData("   ");

        // Load and print data
        System.out.println(
                storageService.loadData()
        );

        // Clear storage
        storageService.clearStorage();

        // Print data after clearing
        System.out.println(
                storageService.loadData()
        );


        // ================= BACKUP STORAGE EXAMPLE =================
        Storage backupStorage =
                new BackupStorage();

        StorageService backupService =
                new StorageService(backupStorage);

        backupService.saveData("Backup Entry");
        backupService.saveData("Monthly Summary");

        System.out.println(
                backupService.loadData()
        );

        backupService.clearStorage();

        System.out.println(
                backupService.loadData()
        );
    }
}
