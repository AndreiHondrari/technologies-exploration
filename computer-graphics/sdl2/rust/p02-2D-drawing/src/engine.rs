
use std::time::Duration;

use crate::{events, render, game, context::AppContext};

const NANOSECONDS_IN_SECOND: u32 = 1_000_000_000;
const NUMBER_OF_FRAMES: u32 = 60;

pub fn run_main_loop (
    sdl2_context: &sdl2::Sdl,
    canvas: &mut sdl2::render::Canvas<sdl2::video::Window>,
    app_context: &mut AppContext
) {

    let mut event_pump: sdl2::EventPump = sdl2_context.event_pump().unwrap();
    
    // main application loop
    loop {
        // HANDLE EVENTS
        if !events::handle_events(&mut event_pump, app_context) {
            break; // exit if continuation is not desired anymore
        }

        game::update_frame(app_context);

        render::clear(canvas);
        render::render_legend(&app_context, canvas);
        render::render_dot(app_context, canvas);

        canvas.present();
        
        std::thread::sleep(Duration::new(0, NANOSECONDS_IN_SECOND / NUMBER_OF_FRAMES));
    }
}