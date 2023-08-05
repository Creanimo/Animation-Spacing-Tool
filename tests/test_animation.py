import unittest
from animation import frame

class Test_Frame(unittest.TestCase):

    def test_Error_FrameNumberRequiresInt(self):
        with self.assertRaises(TypeError):
            frame.Frame(frameNumber="invalid", keyType="key", easeType="easeOut")

    def test_Error_KeyTypeInvalid(self):
        with self.assertRaises(ValueError):
            frame.Frame(frameNumber=1, keyType="invalid_key", easeType="easeOut")

    def test_Error_EaseTypeInvalid(self):
        with self.assertRaises(ValueError):
            frame.Frame(frameNumber=1, keyType="key", easeType="invalid")

    def test_Error_MotionIDRequiresInt(self):
        with self.assertRaises(TypeError):
            frame.Frame(frameNumber=1, keyType="key", easeType="easeOut", motionID="invalid")

    def test_Error_Frame_SpacingCountRequiresInt(self):
        with self.assertRaises(TypeError):
            frame.Frame(frameNumber=1, keyType="key", easeType="easeOut", spacingCount="invalid")

    def test_Valid_FrameCreationInbetween(self):
        # Test a valid frame creation for inbetweens
        f = frame.Frame(frameNumber=3, keyType="inbetween", easeType=None, motionID=10, spacingCount=5, easeVal=0.5)
        self.assertEqual(f.frameNumber, 3)
        self.assertEqual(f.keyType, "inbetween")
        self.assertEqual(f.easeType, None)
        self.assertEqual(f.motionID, 10)
        self.assertEqual(f.spacingCount, 5)
        self.assertEqual(f.easeVal, 0.5)

    def test_Valid_FrameCreationKey(self):
        # Test a valid frame creation for keys
        f = frame.Frame(frameNumber=1, keyType="key", easeType="easeOut", motionID=2)
        self.assertEqual(f.frameNumber, 1)
        self.assertEqual(f.keyType, "key")
        self.assertEqual(f.easeType, "easeOut")
        self.assertEqual(f.motionID, 2)
        self.assertEqual(f.spacingCount, None)
        self.assertEqual(f.easeVal, None)

if __name__ == '__main__':
    unittest.main()