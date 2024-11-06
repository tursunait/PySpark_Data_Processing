use csv::ReaderBuilder;
use reqwest::blocking::get;
use rusqlite::{params, Connection};
use std::error::Error;
use std::fs::{File, OpenOptions};
use std::io::Write;

const LOG_FILE: &str = "query_log.md";

/// A type alias for the complex return type used in `read_data`
type Record = (String, String, String, f64, f64, i64, f64, f64);

/// Struct to hold parameters for updating a record
pub struct UpdateRecordParams<'a> {
    pub gisjoin: &'a str,
    pub state: &'a str,
    pub lat_tract: f64,
    pub long_tract: f64,
    pub population: i64,
    pub adj_radiuspop_5: f64,
    pub urbanindex: f64,
}

/// Extracts data from the given URL and saves it to the specified file path.
pub fn extract(url: &str, file_path: &str) -> Result<(), Box<dyn Error>> {
    let response = get(url)?;
    let mut file = File::create(file_path)?;
    file.write_all(&response.bytes()?)?;
    println!("Data extracted to {}", file_path);
    Ok(())
}

/// Loads data from the CSV file into the SQLite database.
pub fn load_data(file_path: &str) -> Result<(), Box<dyn Error>> {
    let conn = Connection::open("urbanizationDB.db")?;

    // Drop the table if it exists and create a new one
    conn.execute("DROP TABLE IF EXISTS urbanizationDB", [])?;
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
    )?;

    // Read data from the CSV and insert it into the database
    let mut rdr = ReaderBuilder::new().from_path(file_path)?;
    for result in rdr.records() {
        let record = result?;
        conn.execute(
            "INSERT INTO urbanizationDB (statefips, state, gisjoin, lat_tract, long_tract, population, adj_radiuspop_5, urbanindex) 
            VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)",
            params![
                &record[0], 
                &record[1], 
                &record[2], 
                &record[3].parse::<f64>()?, 
                &record[4].parse::<f64>()?, 
                &record[5].parse::<i64>()?, 
                &record[6].parse::<f64>()?, 
                &record[7].parse::<f64>()?
            ],
        )?;
    }
    println!("Data loaded into SQLite database.");
    Ok(())
}

/// Logs an SQL query to a markdown file.
fn log_query(query: &str) {
    let mut file = OpenOptions::new()
        .append(true)
        .create(true)
        .open(LOG_FILE)
        .expect("Unable to open log file");
    writeln!(file, "```sql\n{}\n```\n", query).expect("Unable to write data");
}

/// Creates a record in the `urbanizationDB` table.
pub fn create_record(
    conn: &Connection,
    record: (&str, &str, &str, f64, f64, i64, f64, f64),
) -> Result<(), Box<dyn Error>> {
    conn.execute(
        "INSERT INTO urbanizationDB (statefips, state, gisjoin, lat_tract, long_tract, population, adj_radiuspop_5, urbanindex)
         VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)",
        params![
            record.0, record.1, record.2, record.3, record.4, record.5, record.6, record.7
        ],
    )?;
    log_query("INSERT INTO urbanizationDB ...");
    Ok(())
}

/// Updates a record in the `urbanizationDB` table using `UpdateRecordParams`.
pub fn update_record(conn: &Connection, params: UpdateRecordParams) -> Result<(), Box<dyn Error>> {
    let query = format!(
        "UPDATE urbanizationDB SET state = '{}', lat_tract = {}, long_tract = {}, population = {}, adj_radiuspop_5 = {}, 
         urbanindex = CASE WHEN state = 'Alabama' THEN {} ELSE urbanindex END WHERE gisjoin = '{}'",
        params.state, params.lat_tract, params.long_tract, params.population, params.adj_radiuspop_5, params.urbanindex * 0.5, params.gisjoin
    );

    conn.execute(
        "UPDATE urbanizationDB SET state = ?, lat_tract = ?, long_tract = ?, population = ?, adj_radiuspop_5 = ?, 
            urbanindex = CASE WHEN state = 'Alabama' THEN ? ELSE urbanindex END WHERE gisjoin = ?",
        params![
            params.state, 
            params.lat_tract, 
            params.long_tract, 
            params.population, 
            params.adj_radiuspop_5, 
            params.urbanindex * 0.5, 
            params.gisjoin
        ],
    )?;
    log_query(&query);
    Ok(())
}

/// Deletes a record from the `urbanizationDB` table.
pub fn delete_record(conn: &Connection, gisjoin: &str) -> Result<(), Box<dyn Error>> {
    conn.execute(
        "DELETE FROM urbanizationDB WHERE gisjoin = ?",
        params![gisjoin],
    )?;
    log_query(&format!(
        "DELETE FROM urbanizationDB WHERE gisjoin = '{}';",
        gisjoin
    ));
    Ok(())
}

/// Reads all data from the `urbanizationDB` table.
pub fn read_data(conn: &Connection) -> Result<Vec<Record>, Box<dyn Error>> {
    let mut stmt = conn.prepare("SELECT * FROM urbanizationDB")?;
    let data = stmt
        .query_map([], |row| {
            Ok((
                row.get(0)?,
                row.get(1)?,
                row.get(2)?,
                row.get(3)?,
                row.get(4)?,
                row.get(5)?,
                row.get(6)?,
                row.get(7)?,
            ))
        })?
        .collect::<Result<Vec<_>, _>>()?;

    log_query("SELECT * FROM urbanizationDB;");
    Ok(data)
}
