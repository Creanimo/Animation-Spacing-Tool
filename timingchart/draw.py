import xml.etree.ElementTree as ET

def create_timing_chart():
    # Initialize the SVG root element
    root = ET.Element("{http://www.w3.org/2000/svg}svg", xmlns="http://www.w3.org/2000/svg", version="1.1")

    # Set the size of the SVG canvas (adjust as needed)
    svg_width = 60
    svg_height = 600
    root.set("width", str(svg_width))
    root.set("height", str(svg_height))

    # Parameters for the timing chart
    key_frame = 1
    breakdown_frame = 9
    key2_frame = 17

    # Calculate the total number of frames (including the last keyframe)
    num_frames = key2_frame + 1
    print(f"Total number of frames: {num_frames}")

    # Calculate the spacings as percentage of the total duration
    total_duration = key2_frame - key_frame
    spacings_ease_out = [(breakdown_frame - key_frame) / total_duration]
    while breakdown_frame < key2_frame:
        spacing = spacings_ease_out[-1] / 2
        spacings_ease_out.append(spacing)
        total_duration -= int(spacing * total_duration)
        # Ensure breakdown_frame doesn't exceed key2_frame
        breakdown_frame = min(breakdown_frame + total_duration, key2_frame)

    print("Spacings for ease out:", spacings_ease_out)

    spacings_ease_in = [(key2_frame - breakdown_frame) / total_duration]
    while breakdown_frame > key_frame:
        spacing = spacings_ease_in[-1] / 2
        spacings_ease_in.append(spacing)
        total_duration -= int(spacing * total_duration)
        # Ensure breakdown_frame doesn't go below key_frame
        breakdown_frame = max(breakdown_frame - total_duration, key_frame)

    spacings_ease_in.reverse()
    print("Spacings for ease in:", spacings_ease_in)

    # Draw the vertical timing chart
    chart_height = svg_height - 20
    y_position = 10  # Starting position for drawing the chart

    for spacing in spacings_ease_out:
        rect = ET.Element("{http://www.w3.org/2000/svg}rect", x="10", y=str(y_position),
                          width="20", height=str(chart_height * spacing), fill="black")
        root.append(rect)
        y_position += chart_height * spacing

    for spacing in spacings_ease_in:
        rect = ET.Element("{http://www.w3.org/2000/svg}rect", x="40", y=str(y_position),
                          width="20", height=str(chart_height * spacing), fill="black")
        root.append(rect)
        y_position += chart_height * spacing

    # Save the SVG to a file
    tree = ET.ElementTree(root)
    tree.write("motion_timing_chart.svg", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    create_timing_chart()
