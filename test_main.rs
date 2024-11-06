use rusqlite::Connection;
use urbanization_rs::db_operations; // Assuming db_operations is in lib.rs or a module accessible from the root

const TEST_DB: &str = "test_urbanizationDB.db";

/// Sets up a new database connection for testing
fn setup_test_db() -> Connection {
    let conn = Connection::open(TEST_DB).expect("Failed to open test database");
    conn.execute("DROP TABLE IF EXISTS urbanizationDB", []).unwrap();
    conn.execute(
        "CREATE TABLE urbanizationDB (
            statefips TEXT,
            state TEXT,
            gisjoin TEXT,
            lat_tract REAL,
            long_tract REAL,
            population INTEGER,
            adj_radiuspop_5 REAL,
            urbanindex REAL
        )",
        [],
    ).unwrap();
    conn
}

/// Tests the extraction of data
#[test]
fn test_extract_data() {
    let url = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/urbanization-index/urbanization-census-tract.csv";
    let file_path = "tests/test_data.csv";
    
    let result = db_operations::extract(url, file_path);
    assert!(result.is_ok(), "Failed to extract data");
}

/// Tests loading CSV data into the database
#[test]
fn test_load_data() {
    let conn = setup_test_db();
    let file_path = "tests/test_data.csv";
    
    let result = db_operations::load_data(file_path);
    assert!(result.is_ok(), "Failed to load data into database");
}

/// Tests creating a record in the database
#[test]
fn test_create_record() {
    let conn = setup_test_db();
    let record = ("01", "Alabama", "G0100010", 34.0, -86.0, 10000, 200.0, 0.8);
    
    let result = db_operations::create_record(&conn, record);
    assert!(result.is_ok(), "Failed to create record in database");
}

/// Tests reading data from the database
#[test]
fn test_read_data() {
    let conn = setup_test_db();
    let record = ("01", "Alabama", "G0100010", 34.0, -86.0, 10000, 200.0, 0.8);
    db_operations::create_record(&conn, record).expect("Failed to create record for read test");
    
    let data = db_operations::read_data(&conn).expect("Failed to read data");
    assert!(!data.is_empty(), "No data found in database");
}

/// Tests updating a record in the database
#[test]
fn test_update_record() {
    let conn = setup_test_db();
    let record = ("01", "Alabama", "G0100010", 34.0, -86.0, 10000, 200.0, 0.8);
    db_operations::create_record(&conn, record).expect("Failed to create record for update test");

    let result = db_operations::update_record(&conn, "G0100010", "Alabama", 34.1, -86.1, 10001, 201.0, 0.9);
    assert!(result.is_ok(), "Failed to update record in database");
}

/// Tests deleting a record from the database
#[test]
fn test_delete_record() {
    let conn = setup_test_db();
    let record = ("01", "Alabama", "G0100010", 34.0, -86.0, 10000, 200.0, 0.8);
    db_operations::create_record(&conn, record).expect("Failed to create record for delete test");

    let result = db_operations::delete_record(&conn, "G0100010");
    assert!(result.is_ok(), "Failed to delete record in database");
}
