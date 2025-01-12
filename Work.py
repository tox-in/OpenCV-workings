import cv2
import numpy as np
def license_plate_annotation(image_path, output_path):
  image = cv2.imread(image_path)
  if image is None:
    raise Exception("Could not read the image")
  annotated_image = image.copy()
  height, width = image.shape[:2]
  # region of interest (ROI) for the license plate
  x1 = int(width * 0.21)
  y1 = int(height * 0.20)
  x2 = int(width * 0.78)
  y2 = int(height * 0.97)
  # Draw the green bounding box
  color = (0, 255, 0)
  thickness = 6
  cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, thickness)
  text = "RAH972U"
  text_x = int(width * 0.68)
  text_y = int(height * 0.19)
  font = cv2.FONT_HERSHEY_SIMPLEX
  font_scale = 1.9
  text_thickness = 4
  (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, text_thickness)
  padding = 8
  cv2.rectangle(annotated_image,
         (text_x - padding, text_y - text_height - padding),
         (text_x + text_width + padding, text_y + padding),
         (1, 1, 1),
         -1)

  cv2.putText(annotated_image, text, (text_x, text_y),
        font, font_scale, color, text_thickness)

  cv2.imwrite(output_path, annotated_image)
  return annotated_image
if __name__ == "__main__":
  try:
    input_image = "assignment-001-given.jpg"
    output_image = "assignment-001-result.jpg"

    result = license_plate_annotation(input_image, output_image)

    cv2.imshow('License Plate Annotation Result', result)
    print("Press any key to close the window and save the image...")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"Plate Image saved successfully as {output_image}")
  except Exception as e:
    print(f"An error occurred: {str(e)}")