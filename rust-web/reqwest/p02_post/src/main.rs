use std::collections::HashMap;

use reqwest::StatusCode;

use reqwest::blocking::{Client, Request, RequestBuilder, Response};

fn main() -> Result<(), reqwest::Error> {
    println!("Hello, world!");

    let client = Client::new();
    let request_builder: RequestBuilder = client.post("http://localhost:9999");

    let mut data: HashMap<&str, &str> = HashMap::new();
    data.insert("this", "111");
    data.insert("that", "222");

    let request: Request = request_builder.json(&data).build().unwrap();

    let response: Response = client.execute(request).unwrap();

    let status_code: StatusCode = response.status();
    let text: String = response.text()?;

    println!("[{:?}] {}", status_code, text);

    println!("--- GOODBYE ---");

    Ok(())
}
