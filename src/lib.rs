extern crate regex;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use regex::Regex;
use std::collections::HashMap;

/// Finds the multiplier within a couple of lines that dollar is mentioned
#[pyfunction]
pub fn find_multiplier(table_header: Vec<String>) -> u32 {
    // hasmap to connect the words to numbers
    let mult_conversion: HashMap<String, u32> = [
        ("THOUSAND".to_string(), 1000),
        ("MILLION".to_string(), 1000000),
        ("BILLION".to_string(), 1000000000),
    ]
    .iter()
    .cloned()
    .collect();

    // dollar search terms for finding within the header
    let dollar_search = Regex::new(r"DOLLAR|USD|\$").unwrap();

    // find the line within the header that contains the dollar term
    let mut line_index = None;
    for (x, line) in table_header.iter().enumerate() {
        let line_upper = line.to_uppercase();
        if dollar_search.is_match(&line_upper) {
            line_index = Some(x);
            break;
        }
    }
    // if dollar is found within the index then find the number multiplier nearby
    if let Some(index) = line_index {
        for mult in mult_conversion.keys() {
            if table_header.iter().enumerate().any(|(x, line)| {
                x >= index - 1 && x <= index + 2 && line.to_uppercase().contains(mult)
            }) {
                return mult_conversion[mult];
            }
        }
    }
    // if multiplier is not found, return 1
    return 1;
}

#[pymodule]
fn librust_vs_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(find_multiplier))?;

    Ok(())
}
