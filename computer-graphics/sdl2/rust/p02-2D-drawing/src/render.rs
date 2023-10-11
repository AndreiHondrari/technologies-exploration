
use sdl2::pixels::Color;
use sdl2::rect::Rect;

use crate::context::AppContext;

pub fn setup(canvas: &mut sdl2::render::Canvas<sdl2::video::Window>) {
    // let logical_size_result = canvas.set_logical_size(1000, 1000);
    // if logical_size_result.is_err() {
    //     println!("LS problem: {:?}", logical_size_result);
    // }

    let logical_size = canvas.logical_size();
    println!("logical size: {:?}", logical_size);

    let viewport = canvas.viewport();
    println!("viewport: {:?}", viewport);
    
    let scale_result = canvas.set_scale(1.0, 1.0);
    if scale_result.is_err() {
        println!("scale error {:?}", scale_result.unwrap_err());
    }
}


pub fn clear(canvas: &mut sdl2::render::Canvas<sdl2::video::Window>) {
    canvas.set_draw_color(sdl2::pixels::Color::RGB(0, 0, 0));
    canvas.clear();
}

pub fn render_legend(app_context: &AppContext, canvas: &mut sdl2::render::Canvas<sdl2::video::Window>) {
    canvas.set_draw_color(
        if app_context.is_mouse_on { 
            Color::RGB(0, 255, 0) 
        } 
        else {
            Color::RGB(255, 0, 0)
        }
    );

    let mouse_indicator = Rect::new(680, 10, 10, 10);

    let result1 = canvas.draw_rect(mouse_indicator);
    let result2 = canvas.fill_rect(mouse_indicator);

    for result in [result1, result2] {
        if result.is_err() {
            println!("mouse_indicator problem: {:?}", result.unwrap_err())
        }
    }
}

static DOT_SIZE: u32 = 20;
static HALF_DOT_SIZE: i32 = (DOT_SIZE as i32) / 2;

pub fn render_dot(app_context: &AppContext, canvas: &mut sdl2::render::Canvas<sdl2::video::Window>) {
    // set the color of the dot
    canvas.set_draw_color(Color::RGB(255, 0, 0));

    let dot = Rect::new(
        app_context.dot_x - HALF_DOT_SIZE, 
        app_context.dot_y - HALF_DOT_SIZE,
        DOT_SIZE, 
        DOT_SIZE
    );

    let result1 = canvas.draw_rect(dot);
    let result2 = canvas.fill_rect(dot);

    for result in [result1, result2] {
        if result.is_err() {
            println!("dot problem: {:?}", result.unwrap_err())
        }
    }
}