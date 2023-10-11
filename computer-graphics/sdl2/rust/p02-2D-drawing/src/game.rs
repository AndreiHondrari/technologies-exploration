
use crate::context::AppContext;



// UP
pub fn handle_up_press(app_context: &mut AppContext) {
    println!("UP PRESS");
    app_context.is_up = true;
}

pub fn handle_up_release(app_context: &mut AppContext) {
    println!("UP RELEASE");
    app_context.is_up = false;
}

// DOWN
pub fn handle_down_press(app_context: &mut AppContext) {
    println!("DOWN PRESS");
    app_context.is_down = true;
}

pub fn handle_down_release(app_context: &mut AppContext) {
    println!("DOWN RELEASE");
    app_context.is_down = false;
}
// LEFT
pub fn handle_left_press(app_context: &mut AppContext) {
    println!("LEFT PRESS");
    app_context.is_left = true;
}

pub fn handle_left_release(app_context: &mut AppContext) {
    println!("LEFT RELEASE");
    app_context.is_left = false;
}

// RIGHT
pub fn handle_right_press(app_context: &mut AppContext) {
    println!("RIGHT PRESS");
    app_context.is_right = true;
}

pub fn handle_right_release(app_context: &mut AppContext) {
    println!("RIGHT RELEASE");
    
    app_context.is_right = false;
}

pub fn handle_mouse_toggle(app_context: &mut AppContext) {
    println!("TOGGLE MOUSE");
    app_context.is_mouse_on = !app_context.is_mouse_on;
}

// game frame update
pub fn update_frame(app_context: &mut AppContext) {

    const STEP_SPEED: i32 = 5;

    if app_context.is_mouse_on {
        app_context.dot_x = app_context.mouse_x;
        app_context.dot_y = app_context.mouse_y;
    } else {
        if app_context.is_up {
            app_context.dot_y -= STEP_SPEED;
        }
    
        if app_context.is_down {
            app_context.dot_y += STEP_SPEED;
        }
    
        if app_context.is_left {
            app_context.dot_x -= STEP_SPEED;
        }
    
        if app_context.is_right {
            app_context.dot_x += STEP_SPEED;
        }
    }   
    
}
