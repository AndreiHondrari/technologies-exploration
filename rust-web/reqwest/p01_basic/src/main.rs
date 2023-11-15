
use reqwest::StatusCode;

use reqwest::blocking::{
    Client,
    RequestBuilder,
    Response
};

fn main() -> Result<(), reqwest::Error> {
    println!("Hello, world!");

    let client = Client::new();
    let request_builder: RequestBuilder = client.get("http://example.com");

    let response: Response = request_builder.send()?;

    let status_code: StatusCode = response.status();
    let text: String = response.text()?;

    println!("[{:?}] {}", status_code, text);

    println!("--- GOODBYE ---");

    Ok(())
}
