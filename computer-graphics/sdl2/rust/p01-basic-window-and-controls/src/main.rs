use std::time::Duration;

use sdl2;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;

const STEP: i16 = 51;
const INITIAL_RED: i16 = STEP;

fn main() {
    println!("Hello, world!");

    // get sdl context
    let sdl2_context: sdl2::Sdl = sdl2::init().unwrap();

    // get video
    let video_subsystem: sdl2::VideoSubsystem = sdl2_context.video().unwrap();

    // make window
    let window_builder: sdl2::video::WindowBuilder = video_subsystem.window("something", 500, 300);

    let window: sdl2::video::Window = window_builder.build().unwrap();

    let mut canvas: sdl2::render::Canvas<sdl2::video::Window> = window.into_canvas().build().unwrap();
    canvas.set_draw_color(sdl2::pixels::Color::RGB(INITIAL_RED as u8, 0, 0));
    canvas.clear();
    canvas.present();

    let mut event_pump: sdl2::EventPump = sdl2_context.event_pump().unwrap();

    let addcolor = |x: i16| (if (x+STEP) <= 255 {x+STEP} else {255}) as u8 as i16;
    let subcolor = |x: i16| (if (x-STEP) >= 0 {x-STEP} else {0}) as u8 as i16;

    let mut r: i16 = INITIAL_RED;
    let mut g: i16 = 0;
    let mut b: i16 = 0;

    'running: loop {
        // HANDLE EVENTS
        for event in event_pump.poll_iter() {
            let mut is_color_changed = false;
            
            match event {
                Event::Quit {..} |
                Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                    println!(" \n\n------ PRESSED ESCAPE ------\n\n");
                    break 'running;
                },

                // red events
                Event::KeyDown { keycode: Some(Keycode::Kp7), .. } => {
                    println!(" * PRESSED KEYPAD 7");
                    r = addcolor(r);
                    is_color_changed = true;
                },
                Event::KeyDown { keycode: Some(Keycode::Kp4), .. } => {
                    println!(" * PRESSED KEYPAD 4");
                    r = subcolor(r);
                    is_color_changed = true;
                },
                
                // green events
                Event::KeyDown { keycode: Some(Keycode::Kp8), .. } => {
                    println!(" * PRESSED KEYPAD 8");
                    g = addcolor(g);
                    is_color_changed = true;
                },
                Event::KeyDown { keycode: Some(Keycode::Kp5), .. } => {
                    println!(" * PRESSED KEYPAD 5");
                    g = subcolor(g);
                    is_color_changed = true;
                },

                // blue events
                Event::KeyDown { keycode: Some(Keycode::Kp9), .. } => {
                    println!(" * PRESSED KEYPAD 9");
                    b = addcolor(b);
                    is_color_changed = true;
                },
                Event::KeyDown { keycode: Some(Keycode::Kp6), .. } => {
                    println!(" * PRESSED KEYPAD 6");
                    b = subcolor(b);
                    is_color_changed = true;
                },

                _ => {

                }
            }

            if is_color_changed {
                println!(" § R {:3} G {:3} B {:3}", r, g, b);
                canvas.set_draw_color(sdl2::pixels::Color::RGB(r as u8, g as u8, b as u8));
                canvas.clear();
                canvas.present();
            }
        }
        
        ::std::thread::sleep(Duration::new(0, 10_000_000u32 / 60));
    }

}
