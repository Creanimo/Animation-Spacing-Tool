import unittest
from animation import frame as f
from animation import layer as l

class Test_Frame(unittest.TestCase):

    def test_Error_FrameNumberRequiresInt(self):
        with self.assertRaises(TypeError):
            f.Frame(frameNumber="invalid", keyType="key", easeType="easeOut")

    def test_Error_KeyTypeInvalid(self):
        with self.assertRaises(ValueError):
            f.Frame(frameNumber=1, keyType="invalid_key", easeType="easeOut")

    def test_Error_EaseTypeInvalid(self):
        with self.assertRaises(ValueError):
            f.Frame(frameNumber=1, keyType="key", easeType="invalid")

    def test_Error_MotionIDRequiresInt(self):
        with self.assertRaises(TypeError):
            f.Frame(frameNumber=1, keyType="key", easeType="easeOut", motionID="invalid")

    def test_Error_Frame_SpacingCountRequiresInt(self):
        with self.assertRaises(TypeError):
            f.Frame(frameNumber=1, keyType="key", easeType="easeOut", spacingCount="invalid")

    def test_Valid_FrameCreationInbetween(self):
        # Test a valid frame creation for inbetweens
        testframe = f.Frame(frameNumber=3, keyType="inbetween", easeType=None, motionID=10, spacingCount=5, easeVal=0.5)
        self.assertEqual(testframe.frameNumber, 3)
        self.assertEqual(testframe.keyType, "inbetween")
        self.assertEqual(testframe.easeType, None)
        self.assertEqual(testframe.motionID, 10)
        self.assertEqual(testframe.spacingCount, 5)
        self.assertEqual(testframe.easeVal, 0.5)

    def test_Valid_FrameCreationKey(self):
        # Test a valid frame creation for keys
        testframe = f.Frame(frameNumber=1, keyType="key", easeType="easeOut", motionID=2)
        self.assertEqual(testframe.frameNumber, 1)
        self.assertEqual(testframe.keyType, "key")
        self.assertEqual(testframe.easeType, "easeOut")
        self.assertEqual(testframe.motionID, 2)
        self.assertEqual(testframe.spacingCount, None)
        self.assertEqual(testframe.easeVal, None)

class Test_Layer(unittest.TestCase):

    def test_invalid_name(self):
        # Test if an invalid name raises a TypeError
        name = 123  # Integer instead of a string
        frames = []
        with self.assertRaises(TypeError):
            layer = l.Layer(name, frames)

    def test_invalid_frames_type(self):
        # Test if an invalid frames type raises a TypeError
        name = "Layer1"
        frames = "not_a_list"
        with self.assertRaises(TypeError):
            layer = l.Layer(name, frames)

    def test_invalid_frames_item_type(self):
        # Test if an invalid item in the frames list raises a TypeError
        name = "Layer1"
        frames = [f.Frame(frameNumber=1, keyType="key"), f.Frame(frameNumber=2, keyType="inbetween"), "not_a_frame"]
        with self.assertRaises(TypeError):
            layer = l.Layer(name, frames)

    def test_valid_LayerCreation(self):
        # Test if a valid list of frames passes without raising an error
        name = "Layer1"
        frames = [f.Frame(frameNumber=1, keyType="key"), f.Frame(frameNumber=2, keyType="inbetween")]
        layer = l.Layer(name, frames)
        self.assertEqual(layer.frames, frames)

if __name__ == '__main__':
    unittest.main()