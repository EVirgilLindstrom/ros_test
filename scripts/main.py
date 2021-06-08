import rospy
from sensor_msgs.msg import CompressedImage
import cv2
from cv_bridge import CvBridge


class ImageReader:
    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node('image_reader', anonymous=True)
        rospy.loginfo("Initializing Node")
        rospy.Subscriber("cam1/image_raw/compressed", CompressedImage, self.imageCB)
        rospy.loginfo("Subscriber set up to cam1/image_raw/compressed")
        rospy.spin()

    def imageCB(self, data):
        cvimg = self.bridge.compressed_imgmsg_to_cv2(data)
        cvimg = self.detect(cvimg)

        resimg = cv2.resize(cvimg, (960, 540))
        cv2.imshow("image",resimg)
        cv2.waitKey(1)

    def detect(self, cv_image):
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, 10, 0.7, 10)
        numCorners = corners.shape[0]
        rospy.loginfo("%i number of corners found" %numCorners)
        for i in range(corners.shape[0]):
            cv2.circle(cv_image, (int(corners[i,0,0]), int(corners[i,0,1])), 40, (0, 0, 0), 5)
        return cv_image
        


if __name__ == "__main__":
    imagenode = ImageReader()