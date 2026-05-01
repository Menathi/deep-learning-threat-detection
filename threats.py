import torch
import cv2
import winsound

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Use GPU if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

# Object → Threat mapping
threat_map = {
    "person": ("Soldier", "Medium Threat"),
    "bird": ("Drone", "Low Threat"),
    "airplane": ("Fighter Jet", "High Threat"),
    "car": ("Military Vehicle", "Medium Threat"),
    "truck": ("Military Vehicle", "Medium Threat"),
    "bus": ("Military Vehicle", "Medium Threat"),
    "boat": ("Warship", "High Threat")
}

cap = cv2.VideoCapture(0)

print("Press 'q' to quit")

while True:

    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for *box, conf, cls in results.xyxy[0]:

        label = model.names[int(cls)]

        if label in threat_map:

            threat_name, threat_level = threat_map[label]

            x1, y1, x2, y2 = map(int, box)

            if threat_level == "Low Threat":
                color = (0,255,0)

            elif threat_level == "Medium Threat":
                color = (0,255,255)

            else:
                color = (0,0,255)

                # 🔊 Alarm for High Threat
                winsound.Beep(1000, 300)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

            text = threat_name + " - " + threat_level

            cv2.putText(frame, text, (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,color,2)

    cv2.imshow("Military Threat Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()