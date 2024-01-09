
use std::time::Duration;

use crate::window_management::events;

const NANOSECONDS_IN_SECOND: u32 = 1_000_000_000;
const NUMBER_OF_FRAMES: u32 = 60;

pub fn run_main_loop (
    sdl2_context: &sdl2::Sdl,
) {

    let mut event_pump: sdl2::EventPump = sdl2_context.event_pump().unwrap();
    
    // main application loop
    loop {
        // HANDLE EVENTS
        if !events::handle_events(&mut event_pump) {
            break; // exit if continuation is not desired anymore
        }
        
        std::thread::sleep(Duration::new(0, NANOSECONDS_IN_SECOND / NUMBER_OF_FRAMES));
    }
}