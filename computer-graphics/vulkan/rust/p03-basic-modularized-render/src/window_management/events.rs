use sdl2;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;


pub fn handle_events(
    event_pump: &mut sdl2::EventPump,
    // app_context: &mut AppContext,
) -> bool{
    for event in event_pump.poll_iter() {
        match event {
            Event::Quit {..} |
            Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                println!(" \n\n------ PRESSED ESCAPE ------\n\n");
                return false;
            },

            // default
            _ => {
                
            }
        }
    }

    true
}