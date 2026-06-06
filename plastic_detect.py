from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Plastic-related classes from COCO dataset
plastic_classes = ["bottle", "cup"]

mode = input("Enter 'cam' for Live Camera or 'video' for Video File: ")

if mode == "cam":
    cap = cv2.VideoCapture(0)
else:
    path = input("Enter video file path: ")
    cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]

        # REAL FILTERING LOGIC
        if label in plastic_classes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,(0,255,0),2)

    cv2.imshow("Plastic Waste Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
