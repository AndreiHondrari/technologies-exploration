
use sdl2;

mod engine;
mod events;
mod render;
mod context;
mod game;

use context::AppContext;


fn main() {
    println!("navigate ze dot");

    // get sdl context
    let sdl2_context: sdl2::Sdl = sdl2::init().unwrap();

    // get video
    let video_subsystem: sdl2::VideoSubsystem = sdl2_context.video().unwrap();

    // make window
    let window_builder: sdl2::video::WindowBuilder = video_subsystem.window("dot navigation", 700, 700);

    let window: sdl2::video::Window = window_builder.build().unwrap();

    let mut canvas: sdl2::render::Canvas<sdl2::video::Window> = window.into_canvas().build().unwrap();
    render::setup(&mut canvas);

    let mut app_context: AppContext = AppContext{
        dot_x: 350,
        dot_y: 350,
        ..AppContext::default()
    };
    engine::run_main_loop(&sdl2_context, &mut canvas, &mut app_context);
}
