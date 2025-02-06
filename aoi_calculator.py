from visual_angle_converter import VisualAngleConverter

def calculate_aoi_size(error_degrees, screen_width_px=1920, screen_height_px=1080, 
                      screen_width_mm=530, screen_height_mm=300, distance_mm=750):
    """
    Calculate recommended AOI size based on eye tracker error in degrees.
    
    Args:
        error_degrees (float): Eye tracker error in degrees
        screen_width_px (int): Screen width in pixels
        screen_height_px (int): Screen height in pixels
        screen_width_mm (float): Screen width in millimeters
        screen_height_mm (float): Screen height in millimeters
        distance_mm (float): Viewing distance in millimeters
    
    Returns:
        dict: Dictionary containing calculations and recommendations
    """
    # Initialize converter
    converter = VisualAngleConverter(
        screen_width_pixels=screen_width_px,
        screen_height_pixels=screen_height_px,
        screen_width_mm=screen_width_mm,
        screen_height_mm=screen_height_mm,
        distance=distance_mm
    )
    
    # Calculate error in pixels
    error_pixels_horizontal = converter.visual_angle_to_pixels(error_degrees, orientation="horizontal")
    error_pixels_vertical = converter.visual_angle_to_pixels(error_degrees, orientation="vertical")
    
    # Calculate minimum AOI size (adding error margin on each side)
    min_aoi_width = error_pixels_horizontal * 2
    min_aoi_height = error_pixels_vertical * 2
    
    # Calculate visual angles for verification
    aoi_width_degrees = converter.pixels_to_visual_angle(min_aoi_width, orientation="horizontal")
    aoi_height_degrees = converter.pixels_to_visual_angle(min_aoi_height, orientation="vertical")
    
    return {
        "error_pixels": {
            "horizontal": error_pixels_horizontal,
            "vertical": error_pixels_vertical
        },
        "recommended_aoi_size": {
            "width_pixels": min_aoi_width,
            "height_pixels": min_aoi_height,
            "width_degrees": aoi_width_degrees,
            "height_degrees": aoi_height_degrees
        }
    }

if __name__ == "__main__":
    # Example usage with different error degrees
    error_degrees_list = [0.5, 1.0, 1.5, 2.0]
    
    # Print header
    print("\nAOI Size Calculations for Different Error Degrees")
    print("-" * 50)
    
    for error_deg in error_degrees_list:
        print(f"\nCalculations for {error_deg}° error:")
        results = calculate_aoi_size(error_deg)
        
        print(f"Error in pixels:")
        print(f"  Horizontal: {results['error_pixels']['horizontal']:.1f} pixels")
        print(f"  Vertical: {results['error_pixels']['vertical']:.1f} pixels")
        
        print(f"Recommended minimum AOI size:")
        print(f"  Width: {results['recommended_aoi_size']['width_pixels']:.1f} pixels")
        print(f"  Height: {results['recommended_aoi_size']['height_pixels']:.1f} pixels")
        
        print(f"Resulting AOI size in visual angles:")
        print(f"  Width: {results['recommended_aoi_size']['width_degrees']:.1f}°")
        print(f"  Height: {results['recommended_aoi_size']['height_degrees']:.1f}°")

# Example of how to use with custom screen parameters:
"""
custom_results = calculate_aoi_size(
    error_degrees=1.0,
    screen_width_px=2560,    # Your screen width in pixels
    screen_height_px=1440,   # Your screen height in pixels
    screen_width_mm=600,     # Your screen width in mm
    screen_height_mm=340,    # Your screen height in mm
    distance_mm=750         # Your viewing distance in mm
)
"""