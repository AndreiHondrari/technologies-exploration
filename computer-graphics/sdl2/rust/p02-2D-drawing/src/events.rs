use sdl2;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;

use crate::context::AppContext;
use crate::game;


pub fn handle_events(
    event_pump: &mut sdl2::EventPump,
    app_context: &mut AppContext,
) -> bool{
    for event in event_pump.poll_iter() {
        match event {
            Event::Quit {..} |
            Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                println!(" \n\n------ PRESSED ESCAPE ------\n\n");
                return false;
            },

            // UP
            Event::KeyDown { keycode: Some(Keycode::Up), .. } => {
                game::handle_up_press(app_context);
            },
            Event::KeyUp { keycode: Some(Keycode::Up), .. } => {
                game::handle_up_release(app_context);
            },

            // DOWN
            Event::KeyDown { keycode: Some(Keycode::Down), .. } => {
                game::handle_down_press(app_context);
            },
            Event::KeyUp { keycode: Some(Keycode::Down), .. } => {
                game::handle_down_release(app_context);
            },

            // LEFT
            Event::KeyDown { keycode: Some(Keycode::Left), .. } => {
                game::handle_left_press(app_context);
            },
            Event::KeyUp { keycode: Some(Keycode::Left), .. } => {
                game::handle_left_release(app_context);
            },

            // RIGHT
            Event::KeyDown { keycode: Some(Keycode::Right), .. } => {
                game::handle_right_press(app_context);
            },
            Event::KeyUp { keycode: Some(Keycode::Right), .. } => {
                game::handle_right_release(app_context);
            },

            // Toggle mouse
            Event::KeyDown { keycode: Some(Keycode::RightBracket), .. } => {
                game::handle_mouse_toggle(app_context);
            },

            Event::MouseMotion {x, y, ..} => {
                
                app_context.mouse_x = x;
                app_context.mouse_y = y;
            }

            // just show other presses
            Event::KeyDown {..} => {
                // println!("{:?}", event);
            }

            // default
            _ => {
                
            }
        }
    }

    true
}