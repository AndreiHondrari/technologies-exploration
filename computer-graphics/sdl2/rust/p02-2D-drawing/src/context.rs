

#[derive(Default)]
pub struct AppContext {
    pub dot_x: i32,
    pub dot_y: i32,
    pub is_up: bool,
    pub is_down: bool,
    pub is_left: bool,
    pub is_right: bool,
    
    pub mouse_x: i32,
    pub mouse_y: i32,
    pub is_mouse_on: bool,
}