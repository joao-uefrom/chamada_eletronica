import mediapipe as mp

from detection import utils


class Tensors:
    def __init__(self):
        mp_face_detection = mp.solutions.face_detection
        self.face_detection = mp_face_detection.FaceDetection(0.75)

    def detect(self, image):
        rgb = utils.bgr2rgb(image)

        results = self.face_detection.process(rgb)
        positions = []

        if results.detections:
            for detection in results.detections:
                rbb = detection.location_data.relative_bounding_box
                h, w = image.shape[:2]

                positions.append([
                    int(rbb.xmin * w),  # x
                    int(rbb.ymin * h),  # y
                    int(rbb.width * w),  # width
                    int(rbb.height * h),  # height
                    detection.score[0]  # score
                ])

        return positions
